# Task2
### Task2-1: Create a new database named website.
    show databases;
![task2-1](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/93a58094-dc12-45ac-ab63-752c5db45038)
### Task2-2: Create a new table named member, in the website database.
    SHOW TABLES;
![task2-2](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/3c72ddf6-a2d8-4f5f-ba10-fe10e42d546c)

# Task 3: SQL CRUD
### Task3-1: INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
### Task3-2: SELECT all rows from the member table.
    INSERT INTO member(name, username, password,follower_count) VALUES ('test', 'test', 'test',5);
    INSERT INTO member(name, username, password,follower_count) VALUES ('Andy', 'aaa', '123',1);
    INSERT INTO member(name, username, password,follower_count) VALUES ('Bill', 'bbb', '456',4);
    INSERT INTO member(name, username, password,follower_count) VALUES ('Charle', 'ccc', '789',2);
    SELECT * from member;
![task3-1_2](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/40af82d9-49a3-4daf-9057-849c66757273)
### Task3-3: SELECT all rows from the member table, in descending order of time.

### Task3-4: SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.

### Task3-5: SELECT rows where username equals to test.
### Task3-6: SELECT rows where name includes the es keyword.
### Task3-7: SELECT rows where both username and password equal to test.
### Task3-8: UPDATE data in name column to test2 where username equals to test.
