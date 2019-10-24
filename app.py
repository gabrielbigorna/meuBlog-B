from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CadastraUsuarioForm

#from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meublog.db'
app.config['SECRET_KEY'] = 'cb7684e2dbe580b4e4e311dfcebe1b55'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String( ), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():

    form = CadastraUsuarioForm()
    if form.validate_on_submit():
    
        print(form.senha.data)
        print(form.email.data)
    

    return render_template('register.html', formulario=form)



@app.route('/login')
def login():
    return render_template('login.html')











"""


"""


if __name__ == '__main__':
    app.run(debug=True)