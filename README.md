# fastapi

https://www.youtube.com/watch?v=kZHdC-_yPgI

### 手順

- ローカルの 8000 番ポートで API サーバー起動
  - `uvicorn main:app --reload`
- リクエスト
  - `python client.py`

### api ドキュメント

- web
  - `http://localhost:8000/docs`
- json
  - `http://localhost:8000/openapi.json`

### コマンド履歴

- `pip install fastapi`
- `pip install "uvicorn[standard]"`
