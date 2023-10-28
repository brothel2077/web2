import os

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://std_1909_exam:Denis2017@std-mysql.ist.mospolytech.ru/std_1909_exam'
SECRET_KEY = 'qwerty1234'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
ADMIN_ROLE_ID = 1
MODER_ROLE_ID = 2

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')