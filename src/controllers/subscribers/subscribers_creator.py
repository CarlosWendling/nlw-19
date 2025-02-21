from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
    def __init__(self, subs_repo: SubscribersRepositoryInterface):
        self.__subs_repo = subs_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        subs_email = subscriber_info["email"]
        subs_evento_id = subscriber_info["evento_id"]

        self.__check_sub(subs_email, subs_evento_id)
        self.__insert_sub(subscriber_info)
        return self.__format_response(subscriber_info)

    def __check_sub(self, subs_email: str, subs_evento_id: int) -> None:
        response = self.__subs_repo.select(subs_email, subs_evento_id)
        if response: raise Exception("Subscriber already exists!")
    
    def __insert_sub(self, subs_info: dict) -> None:
        self.__subs_repo.insert(subs_info)
    
    def __format_response(self, subs_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": 1,
                    "attributes": subs_info
                }
            },
            status_code=201
        )