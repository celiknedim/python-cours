# print('ok')
# import demo
# demo.test()

from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/login")
def read_test(request:Request, x:str = None):
    return templates.TemplateResponse(
        request=request, name="login.html", context={"name": 'Nedim'}
    )

@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    users=[{'user': 'admin'}, {'pwd':"1234"} ]
    return {"username": username}