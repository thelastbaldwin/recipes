from model.user import User
from data import user
from errors import Missing, Duplicate
import pytest

@pytest.fixture
def seed():
    sample = User(
        email="test@test.com",
        username="test_user",
        password_hash="123456"
    )
    resp = user.create(sample)
    yield resp

    user.delete(resp.user_id)

def test_get_all_empty():
    resp = user.get_all()
    assert len(resp) == 0

def test_get_all(seed):
    resp = user.get_all()

    assert len(resp) == 1
    assert resp[0] == seed

def test_get_one_exists(seed):
    resp = user.get_one(seed.user_id)
    assert resp == seed

def test_get_one_missing():
    with pytest.raises(Missing):
        user.get_one(1)

def test_create_duplicate(seed):
    with pytest.raises(Duplicate):
        sample = User(
            email="test2@test.com",
            username=seed.username,
            password_hash=seed.password_hash
        )
        user.create(sample)
    with pytest.raises(Duplicate):
        sample = User(
            email=seed.email,
            username="test_user2",
            password_hash=seed.password_hash
        )
        user.create(sample)

def test_modify(seed):
    copy = seed.model_copy(deep=True)
    copy.password_hash = "234567"
    copy.username = "not_in_use"

    resp = user.modify(seed.user_id, copy)
    assert resp == copy
    
def test_modify_duplicate(seed):
    copy = seed.model_copy(deep=True)
    copy.username = "test_user2"
    copy.email = "test2@test.com"

    remove_me = user.create(copy)

    bad = seed.model_copy(deep=True)
    bad.username = "test_user2"
    with pytest.raises(Duplicate):
        user.modify(seed.user_id, bad)
    
    #cleanup
    user.delete(remove_me.user_id)
    

def test_delete_missing():
    with pytest.raises(Missing):
        user.delete(2)

def test_get_missing():
    with pytest.raises(Missing):
        user.get_one(2)
