from fastapi.routing import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import uuid

from domain import ShorterInput
import container


router = APIRouter(prefix='/api/v1')

@router.get('/shorter/{code}')
def get_url_and_redirect(code: str):
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.get_url()
        response = use_case.execute(code)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)

@router.post('/shorter')
def create_shorter(shorter: ShorterInput):
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.create_shorter()
        response = use_case.execute(shorter)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)

@router.put('/shorter/{code}')
def update_shorter(code: str, shorter: ShorterInput):
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.update_url()
        response = use_case.execute(code, shorter)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)

@router.delete('/shorter/{code}')
def delete_shorter(code: str):
    with container.SingletonContainer.scope() as app:
        use_case = app.use_cases.delete_shorter()
        response = use_case.execute(code)
        return JSONResponse(jsonable_encoder(response, exclude={'status_code'}),
                            status_code=response.status_code)
