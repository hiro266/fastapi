from fastapi import FastAPI

app = FastAPI()

# ↑appオブジェクトに対して、デコレーターを使ってルーティングを設定
@app.get("/")
def read_root():
    return {"message": "Hello World"}