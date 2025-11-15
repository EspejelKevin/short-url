from fastapi.routing import APIRouter

import uuid

from domain import ShorterInput


router = APIRouter(prefix='/api/v1')

@router.get('/shorter/{code}')
def get_url_and_redirect(code: uuid.UUID):
    pass

@router.post('/shorter')
def create_shorter(shorter: ShorterInput):
    pass

@router.put('/shorter/{code}')
def update_shorter(code: uuid.UUID, shorter: ShorterInput):
    pass

@router.delete('/shorter/{code}')
def delete_shorter(code: uuid.UUID):
    pass
