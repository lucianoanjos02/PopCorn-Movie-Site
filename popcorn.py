import config
from model import Movie, Series, User
from dao import MovieDAO, SeriesDAO, UserDAO
import db_connection
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'jooj'

# ---------- Objetos de conexão com o banco ----------
movie_dao = MovieDAO(db_connection.session)
series_dao = SeriesDAO(db_connection.session)
user_dao = UserDAO(db_connection.session)

@app.route('/')
def home():
    if 'user_logged' in session:    
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html')


@app.route('/signin')
def signin():
    next = request.args.get('next')
    return render_template('signin.html')


@app.route('/register', methods=['POST'])
def register():
    login = request.form['login']
    password = request.form['password']
    user_name = request.form['user-name']
    email = request.form['email']
    birth_date = request.form['birth-date']
    if user_dao.get_user(request.form['login']) == None:
        new_user = User(login=login, 
                        password=password, 
                        user_name=user_name, 
                        email=email, 
                        birth_date=birth_date)
        user_dao.register_user(new_user)
        session['user_logged'] = request.form['login']
        return redirect(url_for('home'))
    else:
        print("Usuário já cadastrado")
        return redirect(url_for('signin'))


@app.route('/authentication', methods=['POST'])
def authentication():
    user = user_dao.get_user(request.form['login'])
    if user != None and request.form['login'] == user.login:
        if user.password == request.form['password']:
            session['user_logged'] = user.login
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host=config.SITE_HOST, port=config.SITE_PORT, debug=config.SITE_DEBUG)