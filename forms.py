from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastraUsuarioForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    senha = PasswordField('Digite a Senha',validators=[DataRequired()])
    repita_senha = PasswordField('Digite a Senha novamente',validators=[DataRequired(), EqualTo(senha)])
    botao = SubmitField('Cadastrar')




















"""
from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    PasswordField, 
    SubmitField, 
    BooleanField
)
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CadastroUsuarioForm(FlaskForm):
   username = StringField(
       'Usuário', 
       validators=[DataRequired(), Length(min=2, max=80)]
        )
   email = StringField('Email', validators=[DataRequired(), Email()]) 
   password = PasswordField('Senha', validators=[DataRequired()])
   confirm_password = PasswordField('Repita a Senha', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Cadastrar')




"""








"""
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Regitrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Lembre-me')
    submit = SubmitField('Entrar')

    """