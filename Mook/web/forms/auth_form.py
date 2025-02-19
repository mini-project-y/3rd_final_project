# pip install flask-wtf # flask Form을 사용하기 위해 설치
# pip install email-validator

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Optional  # DataRequired: 데이터 반드시 있어야해, 빈 칸 안됀다는 뜻

class LoginForm(FlaskForm):    # FlaskForm 상속받아 내가 필요한걸 추가해서 쓰겠다.
    memberid = StringField("User ID", validators=[DataRequired("ID not found. Please check and try again.")])  # 화면에 출력할때 보여주는 이름 lable, 유효성 검사도구: validators
    passwd = PasswordField("Password", validators=[DataRequired("Invalid password. Please check and try again.")])

class RegisterForm(LoginForm):
    memberid = StringField("User ID", validators=[DataRequired("Invalid username. Please try again with a different one.")])
    passwd = PasswordField("Password", validators=[DataRequired("Password is too weak. Please create a stronger one.")])
    email = EmailField("Email", validators=[Email("Invalid email format. Please check and try again")])
    gender = StringField("Gender", validators=[DataRequired("You haven't selected a gender. Please make a selection.")])
    nationality = StringField("Nationality", validators=[DataRequired("You haven't selected a Nationality. Please make a selection.")])
    vegetarian_type = StringField("Vegetarian Type", validators=[DataRequired("You haven't selected a Vegetarian Type. Please make a selection.")])
    excluded_meats = SelectMultipleField("Excluded Meats", 
                                          choices=[
                                              ('beef', ''),
                                              ('pork', ''),
                                              ('chicken', ''),
                                              ('none', '')
                                          ], validators=[DataRequired("You haven't selected a Excluded Meats. Please make a selection.")])
    allergic_foods = StringField("Allergic Food", validators=[Optional()])
    
    favorite_taste = SelectMultipleField("Favorite Taste", 
                                          choices=[
                                              ('sweet', ''),
                                              ('sour', ''),
                                              ('spicy', ''),
                                              ('salty', ''),
                                              ('bitter', ''),
                                              ('greasy', '')
                                          ], validators=[DataRequired("You haven't selected a Favorite Taste. Please make a selection.")])
    disliked_taste = SelectMultipleField("Disliked Taste", 
                                          choices=[
                                              ('sweet', ''),
                                              ('sour', ''),
                                              ('spicy', ''),
                                              ('salty', ''),
                                              ('bitter', ''),
                                              ('greasy', '')
                                          ], validators=[DataRequired("You haven't selected a Disliked Taste. Please make a selection.")])
