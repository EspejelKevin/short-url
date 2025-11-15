from fastapi import FastAPI
import uvicorn

from infrastructure import router


app = FastAPI(title='URL Shorter')
app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=False, port=8000)
