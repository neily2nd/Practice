from lib.user_repo  import UserRepo
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepo(db_connection)
    result = repo.all()
    assert result == [
        User(1, 'default_user', '123@mail.com'),
        User(2, 'second_user', '456@mail.com')
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepo(db_connection)
    result = repo.find(2)
    assert result == User(2, 'second_user', '456@mail.com')
    
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepo(db_connection)
    user = User(None, "e", "e@e.net")
    repo.create(user)
    assert repo.all() == [
        User(1, 'default_user', '123@mail.com'),
        User(2, 'second_user', '456@mail.com'),
        User(3, "e", "e@e.net")
        
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepo(db_connection)
    repo.delete(2)
    assert repo.all() == [
        User(1, 'default_user', '123@mail.com')
    ]

def test_update(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepo(db_connection)
    repo.update(1, "neil", "neil@home.com")
    assert repo.find(1) == User(1, 'neil', 'neil@home.com')