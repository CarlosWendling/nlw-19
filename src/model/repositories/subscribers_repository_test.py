from .subscribers_repository import SubscribersRepository
import pytest # type: ignore

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "Matheus",
        "email": "matheus@gmail.com",
        "evento_id": 1,
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select():
    email = "carlos@gmail.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    resp = subs_repo.select(email, evento_id)
    print(resp.nome)