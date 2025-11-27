from fastapi.exceptions import HTTPException

import uuid
from datetime import datetime

from domain import (DBRepository, ShorterInput,
                    Response, ShorterDTO)


class CreateShorter:
    def __init__(self, db_service: DBRepository) -> None:
        self.db_service = db_service
        self.meta = {'transaction_id': str(uuid.uuid4()),
                     'timestamp': datetime.now()}
        
    def execute(self, shorter: ShorterInput) -> Response:
        url = shorter.url.encoded_string()
        shorter_db = self.db_service.get_shorter_by_url(url)

        if shorter_db:
            raise HTTPException(409, detail='shorter already exists, try again')
        
        _id = str(uuid.uuid4())
        code = str(uuid.uuid4().int)

        shorter_dto = ShorterDTO(id=_id, url=url, code=code)

        if not self.db_service.create_shorter(shorter_dto):
            raise HTTPException(500, detail='error while creating shorter, try again')
        
        data = {'id': _id, 'code': code}

        return Response(data=data, meta=self.meta, status_code=201)
