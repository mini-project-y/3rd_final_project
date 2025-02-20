import pymysql

def select_member_information(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select gender, nationality, vegetarian_type
             from member
             where memberid = %s"""
    cursor.execute(sql, [memberid])

    row = cursor.fetchall()

    cursor.close()
    conn.close()

    return row

def select_member_allergic(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select allergic_foods 
             from member
             where memberid = %s"""
    cursor.execute(sql, [memberid])

    row = cursor.fetchall()

    cursor.close()
    conn.close()

    return row

def select_favorit_taste(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select taste_name
             from taste
             where taste_id in (select taste_id 
                               from favorite_taste
                               where memberid = %s)"""
    cursor.execute(sql, [memberid])

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [row[0] for row in rows] if rows else []

def select_disliked_taste(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select taste_name
             from taste
             where taste_id in (select taste_id 
                               from disliked_taste
                               where memberid = %s)"""
    cursor.execute(sql, [memberid])

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [row[0] for row in rows] if rows else []

def select_excluded_meat(memberid):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    
    # 2. 명령도구 준비
    cursor = conn.cursor()

    # 3. 명령 실행, auth_view.py와 연동
    sql = """select meat_name
             from meat
             where meat_id in (select meat_id 
                               from excluded_meat
                               where memberid = %s)"""
    cursor.execute(sql, [memberid])

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [row[0] for row in rows] if rows else []