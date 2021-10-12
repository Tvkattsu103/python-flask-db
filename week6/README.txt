Administrator@Admin MINGW64 /d/Dev/Python/week6
$ python -m venv myenv

$ source venv/Scripts/activate
(venv) 
$ set FLASK_APP = hello_flask.py
(venv) 
$ flask run

$ pip install python-dotenv

$ pip list

$ python --version

$pip install flask-sqlalchemy flask-migrate

$  deactivate

//Sửa lỗi could not be resolved
b1. Check xem mình đang install ở folder myenv nào = lệnh 'pip uninstall flask_sqlalchemy'
b2. If (folder myenv==sai) { thì 'deactivate' } else { 'mình chịu' }
b3. đến đúng folder rồi dùng lệnh 'source myenv/Scripts/activate'

Insert row vao table
>>> from app.models import User
>>> from app import db
>>> u1 = User(username='Thanh', email='thanh@gmail.com')
>>> u1
Thành Nguyễn Lê Trung14:15
>>> db.session.add(u1)
>>> db.session.commit()
Thành Nguyễn Lê Trung14:17
################
Query table User
>>> User.query.all()