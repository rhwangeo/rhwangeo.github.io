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
![task3-1_2](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/830a488b-6228-40f0-810b-be6905a803d5)
### Task3-3: SELECT all rows from the member table, in descending order of time.
    SELECT * FROM member ORDER BY time DESC;
![task3-3](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/992a29f3-3ad0-43a5-835a-6ed39c38a610)
### Task3-4: SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
    SELECT * FROM member ORDER BY time DESC LIMIT 4 OFFSET 1;
![task3-4](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/0177d600-effc-45ce-bc1a-e30d7b8a982a)
### Task3-5: SELECT rows where username equals to test.
    SELECT * FROM member WHERE username = 'test';
![task3-5](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/71806f32-b2eb-4615-9a55-55c4e346cb3f)
### Task3-6: SELECT rows where name includes the es keyword.
    SELECT * FROM member WHERE name LIKE '%es%';
![task3-6](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/db778a33-3b04-48c8-a321-52edadaade88)
### Task3-7: SELECT rows where both username and password equal to test.
    SELECT * FROM member WHERE username = 'test' AND password = 'test';
![task3-7](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/b61d4040-0fe7-4610-88a5-31e9e64122ee)
### Task3-8: UPDATE data in name column to test2 where username equals to test.
    SET SQL_SAFE_UPDATES=0; #關閉安全設定(索引KEY部分)
    UPDATE member SET name = 'test2' WHERE username = 'test';
![task3-8](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/b59bacd2-d10c-4363-8210-9d12e31dbfca)
