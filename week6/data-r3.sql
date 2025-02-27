show databases;
CREATE database website;
USE website;
SHOW TABLES;
CREATE TABLE member(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,  #bigint 表示數字範圍-2^63 to 2^63,比INT能儲存更大的數字
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

#Task3
INSERT INTO member(name, username, password,follower_count) VALUES ('test', 'test', 'test',5);
INSERT INTO member(name, username, password,follower_count) VALUES ('Andy', 'aaa', '123',1);
INSERT INTO member(name, username, password,follower_count) VALUES ('Bill', 'bbb', '456',4);
INSERT INTO member(name, username, password,follower_count) VALUES ('Charle', 'ccc', '789',2);

SELECT * from member;
SELECT * FROM member ORDER BY time DESC;
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1; #包前不包後
SELECT * FROM member WHERE username = 'test';
SELECT * FROM member WHERE name LIKE '%es%';
SELECT * FROM member WHERE username = 'test' AND password = 'test';
SET SQL_SAFE_UPDATES=0; #關閉安全設定(索引KEY部分)
UPDATE member SET name = 'test2' WHERE username = 'test';

#Task4
SELECT COUNT(*) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;
SELECT AVG(follower_count) AS average_count
FROM (
    SELECT follower_count
    FROM member
    ORDER BY follower_count DESC
    LIMIT 2
) AS subquery; #FROM的括弧內容是要取得前2兩名的follower_count數作為查詢列表

#Task5
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(member_id) REFERENCES member(id) #外鍵設定
);

INSERT INTO message(member_id, content,like_count) VALUES (1, 'hello,大家好我是test',6);
INSERT INTO message(member_id, content,like_count) VALUES (2, '我是成員二號',1);
INSERT INTO message(member_id, content,like_count) VALUES (3, '我是成員三號,我愛吃西瓜',3);
INSERT INTO message(member_id, content,like_count) VALUES (4, '我是成員四號,我住南投',2);

SELECT * from message;
SELECT * from message INNER JOIN  member ON message.member_id=member.id ; #new code
SELECT * from message INNER JOIN member ON message.member_id=member.id where member.username='test' ; #new code
SELECT AVG(message.like_count) AS average_like_count
FROM message JOIN member ON message.member_id = member.id #new code
WHERE member.username = 'test';
SELECT member.username, AVG(message.like_count) AS average_like_count
FROM message JOIN member ON message.member_id = member.id GROUP BY member.username; #new code

#foreignkey 檢查code
#方法一
DELETE FROM member WHERE id=4;
#方法二
SELECT
kcu.TABLE_NAME,
kcu.COLUMN_NAME,
kcu.CONSTRAINT_NAME,
kcu.REFERENCED_TABLE_NAME,
kcu.REFERENCED_COLUMN_NAME

FROM
INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu

WHERE
kcu.TABLE_SCHEMA = 'website' AND
kcu.REFERENCED_TABLE_NAME IS NOT NULL AND
(kcu.TABLE_NAME = 'member' OR kcu.TABLE_NAME = 'message');

drop table message;
drop table member;