from fastapi import FastAPI
import uvicorn

from infrastructure import router
import container


def on_start_up():
    container.SingletonContainer.init()

app = FastAPI(title='URL Shorter', on_startup=[on_start_up])
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=False, port=8000)
