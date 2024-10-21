from fastapi import FastAPI
from uvicorn import run

from api.routes import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    run('main:app', host="0.0.0.0", port=8000, reload=True)
