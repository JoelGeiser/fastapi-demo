from fastapi import Cookie, Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

from fastapi.templating import Jinja2Templates
from model import ShopItem

app = FastAPI()
templates = Jinja2Templates(directory="templates")
counter = 1


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


def get_cookie(username: str | None = Cookie(None)):
    if username is None:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN,
                            detail="Cookie not found")
    return username


@app.get("/cookie")
def read_cookie(username: str | None = Depends(get_cookie)) -> JSONResponse:
    return {"user": username}


@app.post("/cookie")
def create_cookie() -> JSONResponse:
    content = {"message": "Join us @Noser, we have cookies =)"}
    response = JSONResponse(content=content)
    response.set_cookie(key="username", value='joel_geiser')
    return response


@app.post("/items")
def create_item(item: ShopItem):
    return item


@app.get("/count")
def count(request: Request):
    global counter
    counter += 1
    context = {"request": request,
               "welcome": "Das ist mein Test",
               "counter": counter}
    return templates.TemplateResponse("count.html", context)
