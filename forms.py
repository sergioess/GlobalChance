from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('nombre_usuario', validators=[DataRequired()], render_kw={"placeholder": "Nombre de Usuario",'class': 'form-control'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": "Contraseña", 'class': 'form-control'})
    submit = SubmitField('Iniciar Sesion', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6'})

class RegistroForm(FlaskForm):
    nombre  = StringField('Nombres ', validators=[DataRequired('Ingrese Nombres')])
    correo  = StringField('Correo Electrónico', validators=[DataRequired('Ingrese su correo electrónico'),Email('Ingrese un Correo Válido') ])
    password = PasswordField('Contraseña', validators=[DataRequired('Ingrese su contraseña')])
    confirmarPassword = PasswordField('Confirmar Contraseña', validators=[DataRequired('Confirme su contraseña')])
    submit = SubmitField('Registrar Usuario', render_kw={ 'class': 'btn btn-primary col-sm-12 col-md-6', "onclick": "return Validate()"
})