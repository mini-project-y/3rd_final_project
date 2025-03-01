from flask import Blueprint, render_template, redirect
from flask import request, url_for, session

from ..db_utils import board_util
from ..forms import board_form

board_bp = Blueprint("board", __name__, url_prefix="/board")

@board_bp.route("/list/")
def list():
    boards = board_util.select_board_list(result_type='dict')
    return render_template('board/list.html', boards=boards)

# Form을 사용하는 write 처리
@board_bp.route("/write/", methods=['POST', 'GET'])
def write():
    if not session.get('loginuser'):
        return redirect(url_for('auth.login'))
    
    form = board_form.BoardForm()
    
    if request.method.lower() == 'post' and form.validate_on_submit():
        board_util.insert_board(form.title.data, form.writer.data, form.content.data)
        return redirect(url_for('board.list'))
    else:
        return render_template('board/write.html', form=form)
    
@board_bp.route("/detail/", methods=['GET'])
def detail():
    if not session.get('loginuser'):
        return redirect(url_for('auth.login'))

    boardno = request.args.get('boardno')
    if not boardno:
        return redirect(url_for('board.list'))
    
    board = board_util.select_board_by_boardno(boardno, result_type='dict')
    
    return render_template('board/detail.html', board=board)

@board_bp.route('/delete/', methods=['GET'])
def delete():
    boardno = request.args.get("boardno")
    if boardno:
        # print('------------------------------------->', boardno)
        # 데이터베이스에서 boardno로 데이터 삭제 ( db_utils 모듈 사용 )
        board_util.delete_board(boardno)
    
    # 목록으로 이동
    return redirect(url_for('board.list'))

@board_bp.route('/update/', methods=['GET', 'POST'])
def update():
    if request.method.lower() == 'get': # get 요청 처리 영역
        boardno = request.args.get('boardno')
        if not boardno:
            return redirect(url_for('board.list'))
        
        # boardno에 해당하는 게시글 조회 (db_utils 사용)
        board = board_util.select_board_by_boardno(boardno, result_type='dict')
        if not board:
            return redirect(url_for('board.list'))
        else:
            return render_template('board/update.html', board=board)
    else:   # post 요청 처리 영역
        # 요청 데이터 읽기
        boardno = request.form.get('boardno')
        title = request.form.get('title')
        content = request.form.get('content')
        # 데이터베이스의 데이터 수정 (board_util 모듈 사용)
        board_util.update_board(boardno, title, content)

        return redirect(url_for('board.detail', boardno=boardno))
