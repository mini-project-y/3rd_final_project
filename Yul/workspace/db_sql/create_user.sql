-- 사용자 계정 생성 및 권한 부여

create database final_project;

drop user 3rdProject;

CREATE USER '3rdProject'@'%' IDENTIFIED BY 'passwd1';

GRANT ALL PRIVILEGES ON final_project.* TO '3rdProject'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

REVOKE ALL PRIVILEGES, GRANT OPTION FROM '3rdProject'@'%';

SHOW GRANTS FOR '3rdProject'@'%';