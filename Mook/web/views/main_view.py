from flask import Blueprint, render_template

from ..db_utils import dashboard_util

main_bp = Blueprint("main", __name__, url_prefix="/")

@main_bp.route("/")
def index():

    data_count_list = {table_name : dashboard_util.select_count_by_table(table_name) 
                       for table_name in ['member', 'board', 'food_recipes']}
    
    top_n_board_list = dashboard_util.select_top_n_board_list(10, result_type="dict")

    return render_template('index.html', data_count_list=data_count_list, board_list=top_n_board_list) # templates/index.html을 처리해서 응답