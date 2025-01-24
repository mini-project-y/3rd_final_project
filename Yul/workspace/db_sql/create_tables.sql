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

-- favorite_taste 코드 테이블 생성
create table favorite_taste(
	favorite_taste_id INT AUTO_INCREMENT PRIMARY KEY
    , taste VARCHAR(20) NOT NULL
);
-- favorite_taste 테이블 값 입력
INSERT INTO favorite_taste(taste) VALUES ('sweet');
INSERT INTO favorite_taste(taste) VALUES ('sour');
INSERT INTO favorite_taste(taste) VALUES ('spicy');
INSERT INTO favorite_taste(taste) VALUES ('salty');
INSERT INTO favorite_taste(taste) VALUES ('bitter');
INSERT INTO favorite_taste(taste) VALUES ('greasy');
select * from favorite_taste;

-- disliked_taste 코드 테이블 생성
create table disliked_taste(
	disliked_taste_id INT AUTO_INCREMENT PRIMARY KEY
    , taste VARCHAR(20) NOT NULL
);
-- disliked_taste 테이블 값 입력
INSERT INTO disliked_taste(taste) VALUES ('sweet');
INSERT INTO disliked_taste(taste) VALUES ('sour');
INSERT INTO disliked_taste(taste) VALUES ('spicy');
INSERT INTO disliked_taste(taste) VALUES ('salty');
INSERT INTO disliked_taste(taste) VALUES ('bitter');
INSERT INTO disliked_taste(taste) VALUES ('greasy');
select * from disliked_taste;

-- preferred_taste 코드 테이블 생성
create table preferred_taste(
	preferred_taste_id INT AUTO_INCREMENT PRIMARY KEY
    , taste VARCHAR(20) NOT NULL
);
-- preferred_taste 테이블 값 입력
INSERT INTO preferred_taste(taste) VALUES ('sweet');
INSERT INTO preferred_taste(taste) VALUES ('sour');
INSERT INTO preferred_taste(taste) VALUES ('spicy');
INSERT INTO preferred_taste(taste) VALUES ('salty');
INSERT INTO preferred_taste(taste) VALUES ('bitter');
INSERT INTO preferred_taste(taste) VALUES ('greasy');
select * from preferred_taste;

-- non_preferred_taste 코드 테이블 생성
create table non_preferred_taste(
	non_preferred_taste_id INT AUTO_INCREMENT PRIMARY KEY
    , taste VARCHAR(20) NOT NULL
);
-- non_preferred_taste 테이블 값 입력
INSERT INTO non_preferred_taste(taste) VALUES ('sweet');
INSERT INTO non_preferred_taste(taste) VALUES ('sour');
INSERT INTO non_preferred_taste(taste) VALUES ('spicy');
INSERT INTO non_preferred_taste(taste) VALUES ('salty');
INSERT INTO non_preferred_taste(taste) VALUES ('bitter');
INSERT INTO non_preferred_taste(taste) VALUES ('greasy');
select * from non_preferred_taste;

-- excluded_meats 코드 테이블 생성
create table excluded_meats(
	excluded_meats_id INT AUTO_INCREMENT PRIMARY KEY
    , meat VARCHAR(20) NOT NULL
);
-- excluded_meats 테이블 값 입력
INSERT INTO excluded_meats(meat) VALUES ('beef');
INSERT INTO excluded_meats(meat) VALUES ('pork');
INSERT INTO excluded_meats(meat) VALUES ('chicken');
select * from excluded_meats;

-- member_favorite_taste 테이블 생성
create table member_favorite_taste(
	id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , ft_id INT
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (ft_id) REFERENCES favorite_taste(favorite_taste_id)
);

-- member_disliked_taste 테이블 생성
create table member_disliked_taste(
	id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , dt_id INT
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (dt_id) REFERENCES disliked_taste(disliked_taste_id)
);

-- member_preferred_taste 테이블 생성
create table member_preferred_taste(
    id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , pt_id INT
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (pt_id) REFERENCES preferred_taste(preferred_taste_id)
);

-- member_non_preferred_taste 테이블 생성
create table member_non_preferred_taste(
    id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , nt_id INT
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (nt_id) REFERENCES non_preferred_taste(non_preferred_taste_id)
);

-- member_excluded_meats 테이블 생성
create table member_excluded_meats(
    id INT AUTO_INCREMENT PRIMARY KEY
    , m_id VARCHAR(30)
    , em_id INT
    , FOREIGN KEY (m_id) REFERENCES member(memberid)
    , FOREIGN KEY (em_id) REFERENCES excluded_meats(excluded_meats_id)
);