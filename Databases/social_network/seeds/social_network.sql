DROP TABLE IF EXISTS Users;
DROP SEQUENCE IF EXISTS Users_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

INSERT INTO users(username, email) VALUES ('default_user', '123@mail.com');
INSERT INTO users(username, email) VALUES ('second_user', '456@mail.com');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int
    
);

INSERT INTO posts (title, content, views, user_id) VALUES ('my first title', 'content of the post', 100, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('my second title', 'content of the second post', 10, 2);