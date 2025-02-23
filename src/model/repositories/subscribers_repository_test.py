from .subscribers_repository import SubscribersRepository
import pytest # type: ignore

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "Teste",
        "email": "test@gmail.com",
        "evento_id": 3,
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

@pytest.mark.skip("Select in DB")
def test_ranking():
    subs_repo = SubscribersRepository()

    event_id = 3
    resp = subs_repo.get_ranking(event_id)

    for elem in resp:
        print(f'Link: {elem.link}, Total de inscritos: {elem.total}')