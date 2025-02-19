# Database 연동
import pymysql

# 회원 가입
def insert_member(memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj",
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into member (memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods)
             values(%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, [memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods])

    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()

    # 5. 연결 닫기
    cursor.close()
    conn.close()

def insert_taste_meat(memberid, favorite_tastes, disliked_tastes, excluded_meats):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj",
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

        # 3. 명령 실행, auth_view.py와 연동
    
    if favorite_tastes:
        for taste in favorite_tastes:
            sql = """insert into favorite_taste (memberid, taste_id) values(%s, (select taste_id from taste where taste_name = %s)) """
            cursor.execute(sql, (memberid, taste))

        # sql = """insert into favorite_taste (memberid, taste_id)"""
        # cursor.execute(sql, [(memberid, taste) for taste in favorite_tastes])

        #     select %s, taste_id from taste where taste_name = %s """
        

    if disliked_tastes:
        for taste in disliked_tastes:
            sql = """insert into disliked_taste (memberid, taste_id) values(%s, (select taste_id from taste where taste_name = %s)) """
            cursor.execute(sql, (memberid, taste))
        # sql = """
        #     insert into disliked_taste (memberid, taste_id)
        #     select %s, taste_id from taste where taste_name = %s """
        # cursor.execute(sql, [(memberid, taste) for taste in favorite_tastes])

    if excluded_meats:
        for meat in excluded_meats:
            sql = """insert into excluded_meat (memberid, meat_id) values(%s, (select meat_id from meat where meat_name = %s)) """
            cursor.execute(sql, (memberid, meat))
        # sql = """
        #     insert into excluded meat (memberid, meat_id)
        #     select %s, meat_id from meat where meat_name = %s """
        # cursor.execute(sql, [(memberid, meat) for meat in excluded_meats])

    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()

    # 5. 연결 닫기
    cursor.close()
    conn.close()


def select_member_by_id(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select memberid, passwd, email, gender, nationality, vegetarian_type, allergic_foods
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