from abc import abstractmethod, ABCMeta
from ..dto.shorter import ShorterDTO


class DBRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_url_by_id(self, id: str) -> ShorterDTO:
        raise NotImplementedError
    
    @abstractmethod
    def get_url_by_code(self, code: str) -> ShorterDTO:
        raise NotImplementedError
    
    @abstractmethod
    def create_shorter(self, shorter: ShorterDTO) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def update_shorter(self, shorter: ShorterDTO) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def delete_shorter(self, id: str) -> bool:
        raise NotImplementedError
