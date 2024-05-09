from lib.user import User


def test_create():
    account = User(1, "my username", "my email")
    assert account.id == 1
    assert account.username == "my username"
    assert account.email == "my email"