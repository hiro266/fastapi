import asyncio
from typing import Union
from fastapi import FastAPI, Header, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # または ["*"] で全て許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# GET

items = ["item1", "item2", "item3", "item4", "item5"]
# appオブジェクトに対して、デコレーターを使ってルーティングを設定
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/")
# skipとlimitはクエリパラメータ → skip=どこまでスキップするか, limit=いくつ取得するか
def read_items(skip: int = 0, limit: int = 10):
    return {"items": items[skip : skip + limit]}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id, "item_name": "サッカーボール"}

# -------------------------------------------------------------
# Post

# BaseModelを継承すると、インスタンス変数を定義できて型チェックができる
class Item(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None

@app.post("/items/")
def create_item(item: Item):
    # 下記出力はAPI側で確認するためのもの
    print(f"実務ではデータベースに保存処理を書く: {item.name}, {item.price}, {item.description}")
    return item

# -------------------------------------------------------------
# Header

@app.get("/sample/")
def read_sample(
    response: Response,
    authorization: Union[str, None] = Header(default=None)):
    print(authorization)
    response.headers["custom-header"] = "12345"
    return {"message": "ヘッダー情報を取得しました"}