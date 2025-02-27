# 導入對應資料庫
from fastapi import FastAPI,Request,Form, Depends #從 FastAPI框架中導入 FastAPI模組 和 Request模組
from fastapi.responses import HTMLResponse #從 FastAPI 框架中導入 HTMLResponse模組， 可進行連結HTML網頁
from fastapi.staticfiles import StaticFiles #從 FastAPI 框架中導入 StaticFiles模組，提供靜態文件使用
from fastapi.templating import Jinja2Templates #從 FastAPI 框架中導入 Jinja2Templates模組，用於處理 Jinja2 網頁模板
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

#建立 FastAPI 應用物件
app = FastAPI()

# 使用 SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="secret_key")

#創建一個static資料夾
app.mount("/static", StaticFiles(directory="static"),name="static")

#創建一個templates資料夾,處理特定網頁模板
templates = Jinja2Templates(directory="templates")

#建立網站首頁
@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 定義登入頁面
@app.post("/signin")
async def signin(request: Request,username: str = Form(None), password: str = Form(None)):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號、密碼", status_code=303)
    elif username != "test" or password != "test":
        return RedirectResponse(url="/error?message=帳號、密碼輸入錯誤", status_code=303)
    else:
        request.session["SIGNED_IN"] = True
        return RedirectResponse(url="/member", status_code=303)

# 定義會員頁面
@app.get("/member")
async def get_member_page(request: Request):
    if "SIGNED_IN" not in request.session or not request.session["SIGNED_IN"]:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("member.html", {"request": request})

# 定義錯誤頁面
@app.get("/error", response_class=HTMLResponse)
async def get_error_page(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

# 定義登出頁面
@app.get("/signout")
async def signout(request: Request):
    request.session.pop("SIGNED_IN", None)
    return RedirectResponse(url="/", status_code=303)
# uvicorn main:app --reload ,讓uvicorn 跑起來