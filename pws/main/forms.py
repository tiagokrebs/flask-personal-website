from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('Qual o seu nome?', validators=[Required()])
    submit = SubmitField('Entrar')
