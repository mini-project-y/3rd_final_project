import pymysql


def select_count_by_table(table_name):
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """select count(*) from {0}""".format(table_name)
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return row[0]

# db에서 글 목록 불러와서 글 번호 순서로 정렬
def select_top_n_board_list(n=5, result_type='list'):
    conn = pymysql.connect(host="192.168.0.9", port=3306, db="final_pj", 
                           user="humanda", passwd="1234")
    cursor = conn.cursor()
    # 3. 명령 실행, auth_view.py와 연동
    sql = """select boardno, title, writer, readcount, writedate, modifydate, deleted
             from board
             order by boardno desc
             limit %s"""
    cursor.execute(sql, [n])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    if result_type == 'list':
        return rows
    else:
        return result_as_dict(rows, ['boardno', 'title', 'writer', 'readcount', 'writedate', 'modifydate', 'deleted'])

def result_as_dict(rows, columns):
    dict_list = []
    for row in rows:
        d = { c: v for c, v in zip(columns, row) }
        dict_list.append(d)
    return dict_list