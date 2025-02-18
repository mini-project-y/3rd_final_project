# Database 연동
import pymysql

# 회원 가입 - member table
def insert_member(memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods, favorite_food, disliked_food, preferred_food, non_preferred_food):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project",
                           user="3rdProject", passwd="passwd1")
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member (memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods, favorite_food, disliked_food, preferred_food, non_preferred_food)
             values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, [memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods, favorite_food, disliked_food, preferred_food, non_preferred_food])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

# 회원 가입 - favorite_taste table
def insert_member_favorite_taste(memberid, favorite_taste):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project",
                           user="3rdProject", passwd="passwd1")
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member_favorite_taste (m_id, favorite_taste)
             values(%s, %s)"""
    cursor.execute(sql, [memberid, favorite_taste])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

# 회원 가입 - disliked_taste table
def insert_member_disliked_taste(memberid, disliked_taste):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project",
                           user="3rdProject", passwd="passwd1")
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member_disliked_taste (m_id, disliked_taste)
             values(%s, %s)"""
    cursor.execute(sql, [memberid, disliked_taste])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

# 회원 가입 - preferred_taste table
def insert_member_preferred_taste(memberid, preferred_taste):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project",
                           user="3rdProject", passwd="passwd1")
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member_preferred_taste (m_id, preferred_taste)
             values(%s, %s)"""
    cursor.execute(sql, [memberid, preferred_taste])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

# 회원 가입 - non_preferred_taste table
def insert_member_non_preferred_taste(memberid, non_preferred_taste):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project",
                           user="3rdProject", passwd="passwd1")
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member_non_preferred_taste (m_id, non_preferred_taste)
             values(%s, %s)"""
    cursor.execute(sql, [memberid, non_preferred_taste])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

# 회원 가입 - excluded_meat table
def insert_member_excluded_meat(memberid, excluded_meat):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project",
                           user="3rdProject", passwd="passwd1")
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member_excluded_meat (m_id, excluded_meat)
             values(%s, %s)"""
    cursor.execute(sql, [memberid, excluded_meat])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

def select_member_by_id(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="localhost", port=3306, db="final_project", 
                           user="3rdProject", passwd="passwd1")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select memberid, passwd
             from member
             where memberid = %s"""
    cursor.execute(sql, [memberid])

    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    # conn.commit()   # select 하는 것이므로 수정사항이 없어 커밋 할 필요 없다.

    row = cursor.fetchone() # id는 primary_key라서 2개가 나올 수 없으므로 fetchone한다.

    # 5. 연결 닫기
    cursor.close()
    conn.close()

    return row