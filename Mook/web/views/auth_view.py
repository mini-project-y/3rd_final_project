from flask import Blueprint, request, url_for, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from ..db_utils import auth_util
from ..forms import auth_form
# request : 요청 관련 정보를 저장하는 객체
# render_template : forward 방식 이동
# redirect : redirect 방식 이동
# from werkzeug.security import generate_password_hash : 복원 불가능 암호화 도구
# from werkzeug.security import check_password_hash : 암호화 데이터 비교
# from ..db_utils import auth_util : db 연동 도구 (from ..db_utils : 상대경로)
# from ..forms import auth_form : 인증 관련 Form
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# form을 사용하는 회원가입 처리 구현 (view -> Form)
@auth_bp.route("/register/", methods=['GET', 'POST'])
def register():
    
    form = auth_form.RegisterForm()
    if request.method.lower() == 'post' and form.validate_on_submit(): # validate_on_submit: 지정된 유효성 검사 규칙에 적합한지 확인하는 도구
        # print(','.join(form.preferred_taste.data))
        # 유효성 검사 결과 적합하다면 아래를 실행
        passwd_hash = generate_password_hash(form.passwd.data)

        favorite_tastes = request.form.getlist('favorite_taste')
        disliked_tastes = request.form.getlist('disliked_taste')
        excluded_meats = request.form.getlist('excluded_meats')

        auth_util.insert_member(form.memberid.data, passwd_hash, form.email.data, form.gender.data, form.nationality.data, form.vegetarian_type.data, form.allergic_foods.data)
        auth_util.insert_taste_meat(form.memberid.data, favorite_tastes, disliked_tastes, excluded_meats)
        # return "test"
        return redirect( url_for('auth.login'))
    else:
        # 유효성 검사 결과 부적합하다면 아래를 실행

        import pandas as pd
        from pathlib import Path
        import oauthlib
        import os

        rpath = auth_bp.root_path # Blueprint가 존재하는 경로
        root_path = Path(rpath).parent # rpath의 부모 경로
        country_name_path = 'data_files/국가명.csv'

        country_name_df = pd.read_csv(os.path.join(root_path, country_name_path))
        countries = country_name_df['영어_국명'].tolist()

        return render_template("auth/auth-register.html", form=form, countries=countries)
    
# Form을 사용하는 로그인 처리 구현
@auth_bp.route("/login/", methods=['GET', 'POST'])
def login():
    form = auth_form.LoginForm()
    if request.method.lower() == 'post' and form.validate_on_submit():
        # 1. member_id로 데이터베이스에서 데이터 조회
        member = auth_util.select_member_by_id(form.memberid.data)
        # 2. 조회된 데이터가 없으면 로그인 실패
        if not member:
            return render_template('auth/auth-login.html', 
                                   form=form,
                                   error = 'ID not found. Please check and try again.')
        # 3. 조회된 데이터가 있으면 패스워드 비교
        if not check_password_hash(member[1], form.passwd.data): # 4. 패스워드가 다르면 로그인 실패
            return render_template('auth/auth-login.html', 
                                   form=form,
                                   error = "Invalid password. Please check and try again.")
        else:   # 5. 패스워드가 같으면 로그인 처리
            session['loginuser'] = \
                { k: v for k, v in zip(['memberid', 'passwd', 'email'], member) if k != 'passwd' }
            
            session['memberid'] = member[0]
            
            return redirect(url_for("main.index"))
    else:
        return render_template("auth/auth-login.html", form=form)
    
@auth_bp.route('/logout', methods=['GET'])
def logout():
    session.clear() # 세션의 모든 요소를 제거
    return redirect(url_for('main.index'))

@auth_bp.route("/forgot_pw/")
def forgot_pw():
    return render_template("auth/auth-forgot-password.html")