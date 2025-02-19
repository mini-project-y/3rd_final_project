import pymysql

def select_recipe(predicted_class):
    conn = pymysql.connect(host="192.168.0.2", port=3306, db="final_pj",
                           user="humanda", passwd="1234")
    
    cursor = conn.cursor()

    sql = """select name, ingredients, recipe, food_name_eng
             from food_recipes
             where food_no = %s"""
    
    cursor.execute(sql, [predicted_class])

    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows