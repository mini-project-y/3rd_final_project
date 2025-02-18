-- 사용할 database 선택
use final_project;

-- 필요한 경우 테이블 삭제
-- drop table member;

-- member 테이블 생성
CREATE TABLE member (
    memberid VARCHAR(30) PRIMARY KEY
    , passwd VARCHAR(300) NOT NULL
    , email VARCHAR(300) NOT NULL
    , gender VARCHAR(50) NOT NULL
    , nationality VARCHAR(100) NOT NULL
    , vegetarian_type VARCHAR(50) NOT NULL
    , allergic_foods VARCHAR(300) DEFAULT 'None'    
    , favorite_food VARCHAR(300) NOT NULL
    , disliked_food VARCHAR(300) NOT NULL
    , preferred_food VARCHAR(300) NOT NULL
    , non_preferred_food VARCHAR(300) NOT NULL
);
select * from member;

-- favorite_taste 코드 테이블 생성
create table favorite_taste(
	favorite_taste VARCHAR(20) PRIMARY KEY
);
-- favorite_taste 테이블 값 입력
INSERT INTO favorite_taste(favorite_taste) VALUES ('sweet');
INSERT INTO favorite_taste(favorite_taste) VALUES ('sour');
INSERT INTO favorite_taste(favorite_taste) VALUES ('spicy');
INSERT INTO favorite_taste(favorite_taste) VALUES ('salty');
INSERT INTO favorite_taste(favorite_taste) VALUES ('bitter');
INSERT INTO favorite_taste(favorite_taste) VALUES ('greasy');
select * from favorite_taste;

-- disliked_taste 코드 테이블 생성
create table disliked_taste(
	disliked_taste VARCHAR(20) PRIMARY KEY
);
-- disliked_taste 테이블 값 입력
INSERT INTO disliked_taste(disliked_taste) VALUES ('sweet');
INSERT INTO disliked_taste(disliked_taste) VALUES ('sour');
INSERT INTO disliked_taste(disliked_taste) VALUES ('spicy');
INSERT INTO disliked_taste(disliked_taste) VALUES ('salty');
INSERT INTO disliked_taste(disliked_taste) VALUES ('bitter');
INSERT INTO disliked_taste(disliked_taste) VALUES ('greasy');
select * from disliked_taste;

-- preferred_taste 코드 테이블 생성
create table preferred_taste(
	preferred_taste VARCHAR(20) PRIMARY KEY
);
-- preferred_taste 테이블 값 입력
INSERT INTO preferred_taste(preferred_taste) VALUES ('sweet');
INSERT INTO preferred_taste(preferred_taste) VALUES ('sour');
INSERT INTO preferred_taste(preferred_taste) VALUES ('spicy');
INSERT INTO preferred_taste(preferred_taste) VALUES ('salty');
INSERT INTO preferred_taste(preferred_taste) VALUES ('bitter');
INSERT INTO preferred_taste(preferred_taste) VALUES ('greasy');
select * from preferred_taste;

-- non_preferred_taste 코드 테이블 생성
create table non_preferred_taste(
	non_preferred_taste VARCHAR(20) PRIMARY KEY
);
-- non_preferred_taste 테이블 값 입력
INSERT INTO non_preferred_taste(non_preferred_taste) VALUES ('sweet');
INSERT INTO non_preferred_taste(non_preferred_taste) VALUES ('sour');
INSERT INTO non_preferred_taste(non_preferred_taste) VALUES ('spicy');
INSERT INTO non_preferred_taste(non_preferred_taste) VALUES ('salty');
INSERT INTO non_preferred_taste(non_preferred_taste) VALUES ('bitter');
INSERT INTO non_preferred_taste(non_preferred_taste) VALUES ('greasy');
select * from non_preferred_taste;

-- excluded_meat 코드 테이블 생성
create table excluded_meat(
	excluded_meat VARCHAR(20) PRIMARY KEY
);
-- excluded_meat 테이블 값 입력
INSERT INTO excluded_meat(excluded_meat) VALUES ('beef');
INSERT INTO excluded_meat(excluded_meat) VALUES ('pork');
INSERT INTO excluded_meat(excluded_meat) VALUES ('chicken');
INSERT INTO excluded_meat(excluded_meat) VALUES ('none');
select * from excluded_meat;

-- member_favorite_taste 테이블 생성
create table member_favorite_taste(
	id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , favorite_taste VARCHAR(20)
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (favorite_taste) REFERENCES favorite_taste(favorite_taste)
);
select * from member_favorite_taste;

-- member_disliked_taste 테이블 생성
create table member_disliked_taste(
	id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , disliked_taste VARCHAR(20)
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (disliked_taste) REFERENCES disliked_taste(disliked_taste)
);
select * from member_disliked_taste;

-- member_preferred_taste 테이블 생성
create table member_preferred_taste(
    id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , preferred_taste VARCHAR(20)
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (preferred_taste) REFERENCES preferred_taste(preferred_taste)
);
select * from member_preferred_taste;

-- member_non_preferred_taste 테이블 생성
create table member_non_preferred_taste(
    id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , non_preferred_taste VARCHAR(20)
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (non_preferred_taste) REFERENCES non_preferred_taste(non_preferred_taste)
);
select * from member_non_preferred_taste;

-- member_excluded_meat 테이블 생성
create table member_excluded_meat(
    id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , excluded_meat VARCHAR(20)
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (excluded_meat) REFERENCES excluded_meat(excluded_meat)
);
select * from member_excluded_meat;

-- join해서 조회하기
SELECT m.*, ft.favorite_taste, dt.disliked_taste, pt.preferred_taste, nt.non_preferred_taste, em.excluded_meat
FROM member AS m
INNER JOIN member_favorite_taste AS ft
ON m.memberid = ft.m_id
INNER JOIN member_disliked_taste AS dt
ON m.memberid = dt.m_id
INNER JOIN member_preferred_taste AS pt
ON m.memberid = pt.m_id
INNER JOIN member_non_preferred_taste AS nt
ON m.memberid = nt.m_id
INNER JOIN member_excluded_meat AS em
ON m.memberid = em.m_id;

select * from member;

DROP TABLE board;
CREATE TABLE board
(
    boardno INT PRIMARY KEY AUTO_INCREMENT	/*pk 자동 증가 번호*/
    , title VARCHAR(100) NOT NULL			/*제목*/
    , writer VARCHAR (20) NOT NULL			/*작성자*/
    , content VARCHAR (4000) NOT NULL		/*내용*/
    , writedate DATE DEFAULT (NOW())		/*작성한 날*/
    , modifydate DATE DEFAULT (NOW())		/*수정한 날*/
    , readcount INT DEFAULT (0)				/*조회 회수*/
    , deleted BOOLEAN DEFAULT (FALSE)		/*삭제 여부 - 삭제하면 글을 조회하지 못하게 하고, 데이터 자체를 삭제하지 않아, 왜냐면 글의 댓글들도 지워야하는데, 그러면 그 댓글 단 사람의 데이터는? 곤란해짐*/

    , CONSTRAINT fk_board_to_member FOREIGN KEY (writer) REFERENCES member (memberid) /*작성자는 member와 참조*/
);

select * from board;
