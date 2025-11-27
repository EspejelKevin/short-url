from domain import DBRepository, ShorterDTO


class DBService(DBRepository):
    def __init__(self, repository: DBRepository) -> None:
        self.repository = repository

    def get_url_by_id(self, id: str) -> ShorterDTO:
        return self.repository.get_url_by_id(id)
    
    def get_url_by_code(self, code: str) -> ShorterDTO:
        return self.repository.get_url_by_code(code)
    
    def get_shorter_by_url(self, url: str) -> ShorterDTO:
        return self.repository.get_shorter_by_url(url)
    
    def create_shorter(self, shorter: ShorterDTO) -> bool:
        return self.repository.create_shorter(shorter)
    
    def update_shorter(self, code: str, shorter: ShorterDTO) -> bool:
        return self.repository.update_shorter(code, shorter)
    
    def delete_shorter(self, code: str) -> bool:
        return self.repository.delete_shorter(code)
