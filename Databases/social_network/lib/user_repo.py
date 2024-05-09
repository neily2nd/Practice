from lib.user import User

class UserRepo:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute("SELECT * from users")
        return [
            User(row["id"], row["username"], row["email"])
            for row in rows
        ]
        
    def find(self, user_id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"])
        
    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s)",
        [user.username, user.email]
        )
        return None
    
    def delete(self, user_id):
        self._connection.execute(
            "DELETE FROM users WHERE id = %s", [user_id]
        )
        
    def update(self, user_id, new_username, new_email):
        self._connection.execute(
            "Update users SET username = %s, email = %s WHERE id = %s",
            [new_username, new_email, user_id]
        )