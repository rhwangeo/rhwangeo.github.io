#抓取PTT電影版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    #url="https://www.ptt.cc/bbs/Lottery/index.html"
    #建立一個Request物件,附加Request Headers的資訊
    request=req.Request(url,headers={
    "Cookie":"over18=1",#18禁頁面通過辦法
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    #print(data) #HTTP Error- 由於被辨識出非正常使用者所以無法使用,需變更開發人員工具>Network>User_Agent
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼,取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")#讓BeautifulSoup協助解析HTML格式文件
    titles=root.find_all("div",class_="title")#尋找class="title"的div標籤
    pushes=root.find_all("div",class_="nrec")
    #print(titles,pushes)
    with open("article.csv","a",encoding="utf-8-sig") as file:
        for title,push in zip (titles, pushes):
            if title.a !=None: #如果標題包含a標籤(沒有被刪除),印出來
                #print(title.a.string,push.string)
                #取得標題的網頁連結
                article_url="https://www.ptt.cc"+title.a["href"]
                #print(article_url)
                #重新通過標題網頁爬蟲
                request_article=req.Request(article_url,headers={
                "Cookie":"over18=1",#18禁頁面通過辦法
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
                })
                with req.urlopen(request_article) as response:
                    article=response.read().decode("utf-8")
                #print(article)
                #用BeautifulSoup解析標題HTML格式文件
                root_article=bs4.BeautifulSoup(article,"html.parser")
                #先找出與時間有關的Span
                article_time=root_article.find("span",class_="article-meta-tag",string="時間")
                #插入None判斷如果有時間標題,則印出
                if article_time is not None:
                    #找出與時間有關的span後,找出下一行的時間資料
                    article_time_value=article_time.find_next_sibling("span",class_="article-meta-value")
                    if article_time_value is not None: #如果標題沒有時間,印出來
                        push_text=push.string if push.string else "0"
                        #print(title.a.string,push_text,article_time_value.string)
                        file.write(title.a.string+","+push_text+","+article_time_value.string+"\n")
    #抓取上一頁連結
    nextLink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"]
#抓取頁面的標題
pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:#!!!!!!!!!!!!!!!數字1記得改回3
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
#print(pageURL)