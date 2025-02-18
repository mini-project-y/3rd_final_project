-- 필요시 데이터베이스 삭제
DROP DATABASE final_project;

-- 데이터베이스 생성
create database final_project;

-- 필요시 계정 삭제
drop user 3rdProject;

-- 계정 생성 및 권한 부여
CREATE USER '3rdProject'@'%' IDENTIFIED BY 'passwd1';

GRANT ALL PRIVILEGES ON final_project.* TO '3rdProject'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

REVOKE ALL PRIVILEGES, GRANT OPTION FROM '3rdProject'@'%';

SHOW GRANTS FOR '3rdProject'@'%';
-- USAGE 권한 지정자는 권한 없음을 나타냅니다.
-- 권한은 없지만 MySQL에 계정이 있음을 알려주는 방식으로 사용

