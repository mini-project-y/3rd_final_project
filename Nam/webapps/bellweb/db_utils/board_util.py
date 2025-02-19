import pymysql

# 글 쓰기 -> db 저장 작업
def insert_board(title, writer, content):
    # 1. 데이터베이스에 연결
    conn = pymysql.connect(host="192.168.0.2", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")    # user="root", passwd="mysql"
    # 2. 명령도구 준비
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """insert into board (title, writer, content)
             values(%s, %s, %s)"""
    cursor.execute(sql, [title, writer, content])
    # 4. 이전 변경 작업을 모두 원본 테이블에 적용하기
    conn.commit()
    # 5. 연결 닫기
    cursor.close()
    conn.close()

# db에서 글 목록 불러와서 글 번호 순서로 정렬
def select_board_list(result_type='list'):
    conn = pymysql.connect(host="192.168.0.2", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """select boardno, title, writer, readcount, writedate, modifydate, deleted
             from board
             order by boardno desc"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    if result_type == 'list':
        return rows
    else:
        return result_as_dict(rows, ['boardno', 'title', 'writer', 'readcount', 'writedate', 'modifydate', 'deleted'])

# db에서 글 번호를 받아서 상세 보기에 연결할 수 있게 하기
def select_board_by_boardno(boardno, result_type='list'):
    conn = pymysql.connect(host="192.168.0.2", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    cursor = conn.cursor()
    sql = """select boardno, title, writer, content, readcount, writedate, modifydate, deleted
             from board
             where boardno = %s"""
    cursor.execute(sql, [boardno])

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    if result_type == 'list':
        return rows[0]
    else:
        cols = "boardno,title,writer,content,readcount,writedate,modifydate,deleted".split(",")
        results = result_as_dict(rows, cols)
        return results[0]

# 딕셔너리로 줘서 어떤 컬럼에 어떤 값이 들어있는지 확실하게 하기
# row = 값, 컬럼 = key
def result_as_dict(rows, columns):
    dict_list = []
    for row in rows:
        d = { c: v for c, v in zip(columns, row) }
        dict_list.append(d)
    return dict_list

def delete_board(boardno):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="final_pj",
                           user="humanda", passwd="humanda")
    cursor = conn.cursor()

    # sql = """delete board where boardno = %s"""
    sql = """update board set deleted  = TRUE where boardno = %s""" # TRUE로 써도 되고 1로 써도 된다.
    cursor.execute(sql, [boardno])

    conn.commit()

    cursor.close()
    conn.close()

def update_board(boardno, title, content):
    conn = pymysql.connect(host="127.0.0.1", port=3306, db="final_pj",
                           user="humanda", passwd="humanda")
    cursor = conn.cursor()

    sql = """update board set title = %s, content = %s where boardno = %s"""
    cursor.execute(sql, [title, content, boardno])

    conn.commit()

    cursor.close()
    conn.close()