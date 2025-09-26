import os
import pytest
from model.explorer import Explorer
from errors import Missing, Duplicate

# set this before data imports below for data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Carl Weathers",
        country="USA", 
        description="To catch a predator",
    )

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("Arnold Schwarzenegger")

def test_modify(sample):
    clone = sample.model_copy(deep=True)
    clone.country = "MX"
    
    resp = explorer.modify(sample.name, clone)
    assert resp == clone

def test_modify_missing():
    thing: Explorer = Explorer(name="Arnold Schwarzenegger", country="RU", description="I'm here, kill me.",)
    with pytest.raises(Missing):
        _ = explorer.modify(thing.name, thing)

def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)