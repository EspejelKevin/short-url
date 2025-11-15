from fastapi.exceptions import HTTPException

import uuid
from datetime import datetime

from domain import DBRepository, Response


class GetURL:
    def __init__(self, db_service: DBRepository) -> None:
        self.db_service = db_service
        self.meta = {'transaction_id': str(uuid.uuid4()),
                     'timestamp': datetime.now()}

    def execute(self, code: uuid.UUID) -> Response:
        shorter = self.db_service.get_url_by_code(code)

        if not shorter:
            raise HTTPException(404, detail=f'shorter not found: {code}')
        
        data = {'url': shorter.url}

        return Response(data=data, meta=self.meta, status_code=200)
