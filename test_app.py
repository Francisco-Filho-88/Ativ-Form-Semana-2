from app import saudacao


def test_saudacao():
    assert saudacao("João") == "Olá, João!"
