# 導入對應資料庫
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="secret_key")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class NameUpdateRequest(BaseModel):
    new_name: str

@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signup")
async def signup(request: Request, name: str = Form(None), username: str = Form(None), password: str = Form(None)):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="12345678",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        if not name or not username or not password:
            return RedirectResponse(url="/", status_code=303)
        cursor.execute("SELECT username FROM member where username=%s", (username,))
        if cursor.fetchone():
            return RedirectResponse(url="/error?message=Repeated username", status_code=303)
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        conn.commit()
        cursor.execute("SELECT id, name FROM member WHERE username = %s", (username,))
        user_record = cursor.fetchone()
        if user_record:
            request.session["SIGNED_IN"] = True
            request.session["USER_ID"] = user_record[0]
            request.session["NAME"] = user_record[1]
        return RedirectResponse(url="/", status_code=303) #修改 url="/member"
    except Exception as e:
        conn.rollback()
        print(f"Database Error: {e}")
        return RedirectResponse(url="/error?message=Failed signup", status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號、密碼", status_code=303)
    try:
        conn = mysql.connector.connect(
            user="root",
            password="12345678",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM member WHERE username = %s AND password = %s", (username, password))
        user_record = cursor.fetchone()
        if user_record:
            request.session["SIGNED_IN"] = True
            request.session["USER_ID"] = user_record[0]
            request.session["USERNAME"] = username
            request.session["NAME"] = user_record[1]
            return RedirectResponse(url="/member", status_code=303)
        else:
            return RedirectResponse(url="/error?message=Username or password is not correct", status_code=303)
    except Exception as e:
        print(f"Database Error: {e}")
        return RedirectResponse(url="/error?message=Failed signin", status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.get("/member")
async def get_member_page(request: Request):
    if "SIGNED_IN" not in request.session or not request.session["SIGNED_IN"]:
        return RedirectResponse(url="/", status_code=303)
    user_id = request.session.get("USER_ID")
    name = request.session.get("NAME")  # 確保從Session中獲取NAME
    try:
        conn = mysql.connector.connect(
            user="root",
            password="12345678",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT member.username, message.content FROM message INNER JOIN member ON message.member_id = member.id")
        messages = cursor.fetchall()
    except Exception as e:
        print(f"Database Error: {e}")
        return RedirectResponse(url="/error?message=Failed to retrieve messages", status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return templates.TemplateResponse("member.html", {"request": request, "name": name, "messages": messages})

@app.get("/error", response_class=HTMLResponse)
async def get_error_page(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.get("/signout")
async def signout(request: Request):
    request.session.pop("SIGNED_IN", None)
    request.session.pop("USER_ID", None)
    request.session.pop("USERNAME", None)
    request.session.pop("NAME", None)
    return RedirectResponse(url="/", status_code=303)

@app.post("/createMessage")
async def create_message(request: Request, content: str = Form(None)):
    if "SIGNED_IN" not in request.session or not request.session["SIGNED_IN"]:
        return RedirectResponse(url="/member", status_code=303)
    user_id = request.session.get("USER_ID")
    if not user_id:
        return RedirectResponse(url="/error?message=Database error", status_code=400)
    try:
        conn = mysql.connector.connect(
            user="root",
            password="12345678",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        conn.rollback()
        return RedirectResponse(url="/error?message=Database error", status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return RedirectResponse(url="/member", status_code=303)

#week7
@app.get("/api/member", response_class=JSONResponse)
async def get_member_info(username: str):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="12345678",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, username FROM member WHERE username = %s", (username,))
        user_record = cursor.fetchone()
        if user_record:
            return JSONResponse(content={"data": user_record})
        else:
            return JSONResponse(content={"data": None})
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        raise JSONResponse(content={"data":None},status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.patch("/api/member")
async def update_member_name(request: Request, payload: NameUpdateRequest):
    if "SIGNED_IN" not in request.session or not request.session["SIGNED_IN"]:
        return JSONResponse(content={"error": True}, status_code=401)
    
    user_id = request.session.get("USER_ID")
    new_name = payload.new_name
    
    if not new_name:
        return JSONResponse(content={"error": True}, status_code=400)

    try:
        conn = mysql.connector.connect(
            user="root",
            password="12345678",
            host="localhost",
            database="website"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE member SET name = %s WHERE id = %s", (new_name, user_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            request.session["NAME"] = new_name
            return JSONResponse(content={"ok": True}, status_code=200)
        else:
            return JSONResponse(content={"error": True}, status_code=400)
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")
        return JSONResponse(content={"error": True}, status_code=500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()