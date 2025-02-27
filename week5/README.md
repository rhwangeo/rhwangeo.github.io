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
    SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
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

# Task 4: SQL Aggregation Functions
### Task4-1: SELECT how many rows from the member table.
    SELECT COUNT(*) FROM member;
![task4-1](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/1e76d373-9038-4fa6-85b2-841b2c61e682)
### Task4-2: SELECT the sum of follower_count of all the rows from the member table.
    SELECT SUM(follower_count) FROM member;
![task4-2](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/ce550569-359b-435c-bd77-0d530c824261)
### Task4-3: SELECT the average of follower_count of all the rows from the member table.
    SELECT AVG(follower_count) FROM member;
![task4-3](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/f097d128-f6df-4259-8c86-7caebfc7792d)

### Task4-4: SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
    SELECT AVG(follower_count) AS average_count
    FROM (
    SELECT follower_count
    FROM member
    ORDER BY follower_count DESC
    LIMIT 2) AS subquery;
![task4-4](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/0a1a7832-087c-4bc5-833e-c17ce683cdfa)
# Task 5: SQL JOIN
### Task5-1: Create a new table named message, in the website database.
    CREATE TABLE message(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(member_id) REFERENCES member(id));

    INSERT INTO message(member_id, content,like_count) VALUES (1, 'hello,大家好我是test',6);
    INSERT INTO message(member_id, content,like_count) VALUES (2, '我是成員二號',1);
    INSERT INTO message(member_id, content,like_count) VALUES (3, '我是成員三號,我愛吃西瓜',3);
    INSERT INTO message(member_id, content,like_count) VALUES (4, '我是成員四號,我住南投',2);
    SELECT * from message;
 ![task5-1-r1](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/70cffe4e-699c-4048-a63a-7f328367c30b)

### Task5-2: SELECT all messages, including sender names. We have to JOIN the member table to get that.
	SELECT * from message INNER JOIN  member ON message.member_id=member.id ;
 ![task5-2-r3](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/19d73c73-4db2-4cda-abec-2a8135cacc19)
### Task5-3: SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
	SELECT * from message INNER JOIN member ON message.member_id=member.id where member.username='test' ;
![task5-3-r3](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/f1038c6f-fb03-497e-8dd8-7a6250fbd410)
### Task5-4: Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
	SELECT AVG(message.like_count) AS average_like_count
	FROM message JOIN member ON message.member_id = member.id WHERE member.username = 'test';#new code
 ![task5-4-r3](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/06b51cd9-c88b-44d5-8c23-c9ba9ce84c8d)

### Task5-5: Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
	SELECT member.username, AVG(message.like_count) AS average_like_count
	FROM message JOIN member ON message.member_id = member.id GROUP BY member.username; #new code
![task5-5-r3](https://github.com/rhwangeo/rhwangeo.github.io/assets/161855974/3fadadc6-0a96-481f-9245-67133d3a5825)

