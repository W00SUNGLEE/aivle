/*
헤어짐의 아쉬움을 달래는 쿼리
*/ 

-- 1) 데이터베이스 만들기

-- 만들기
CREATE DATABASE yourdb;

-- 연결
USE yourdb;

-- 확인
SELECT DATABASE();

-- 2) 테이블 만들기

CREATE TABLE friend (
	friend_no int not null,
    friend_name varchar(20) not null,
    phone varchar(20) null,
    primary key(friend_no)
);

-- 3) 데이터 추가alter
insert into friend VALUES(1, "홍길동", "010-3456-7890");
insert into friend VALUES(2, "일지매", "010-7890-3456");
insert into friend VALUES(3, "이우성", "010-1234-5678");

-- 4) 데이터 조회
select *
	from friend
    where friend_no = 1;