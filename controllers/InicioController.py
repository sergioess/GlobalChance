from flask import Flask, session
from app import Bcrypt ,bcrypt, mail
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import LoginForm, RegistroForm
from flask_mail import  Message
from flask_session import Session

from models.usuario import Usuario
from models.banner import Banner

 
  
@login_required
def home():
    # print("Actual logueado", current_user)
    # user = Usuario.query.filter_by(id=current_user.id).first()
    bannersLista = Banner.get_Active()

    return render_template('/home.html', bannersLista = bannersLista) 

def index():
    
    return render_template('/index.html')



def frmRegistrar2():
    _nombre = request.form.get('txtNombre')   
    _correo = request.form.get('txtCorreo2')   
    _password = request.form.get('txtPassword2')  
    

    print("Nombre Ingresado", _nombre)

    print("El correo es: ", _correo)
    if Usuario.validarUsuario(_correo):
        
        _password = bcrypt.generate_password_hash(_password).decode('utf-8')

        usuario = Usuario()
        usuario.nombre = _nombre
        usuario.correo = _correo
        usuario.password = _password
        usuario.activo = 1
        print(usuario)
        usuario.save()

        # mailtoUser(_nombre, _correo, )

    else:
        session.pop('_flashes', None)
        flash(f'El usuario ya existe en la base de datos, por favor digite otro nombre', 'danger')
        return redirect('/index.html')
    return render_template("index.html")



def frmlogin2():
    
    _nombre = request.form.get('txtCorreo')   
    _password = request.form.get('txtPassword')  

    passIngresado=bcrypt.generate_password_hash('_password').decode('utf-8')
    # print("Ingresado", _nombre, _password,passIngresado)
    # print("Ingresado", passIngresado)
    user = Usuario.query.filter_by(correo=_nombre).first()
    
    # print(user)
    if not user:
        session.pop('_flashes', None)
        flash(f'Usuario no encontrado en la Base de Datos!', 'danger')
        return render_template("index.html")
    else:
        passUsuario = user.password
        print("Encontrado")

    
        # print("Usuario",user.nombre,  passUsuario)
        # print(bcrypt.check_password_hash(user.password, _password))
        if user and bcrypt.check_password_hash(user.password, _password):
            


            n = login(_nombre)

            next = request.args.get('next', None)
            if next:
                return redirect(next)     
            return n       
        else:
            session.pop('_flashes', None)
            flash(f'Inicio de Sesion incorrecto, verifique el Usuario y Contraseña!', 'danger')

            return render_template("index.html")

    # return render_template('/login.html', form = login_form )    


@login_required
def logout():
    logout_user()
    return render_template('index.html') 
    #return 'You are now logged out!'    


def login(nombre):
 
    # print(bcrypt.generate_password_hash('_password'))
    # print(nombre)
    user = Usuario.query.filter_by(correo=nombre).first()
    #print(user)

    login_user(user)

    if(user.perfil==3):
        return redirect('/usuario')    

    bannersLista = Banner.get_Active()
    return render_template('home.html', bannersLista=bannersLista)
    #return 'You are now logged in!'       

# def mailtoadmin():
#     msg = Message('Hello from the other side!', sender = 'peter@mailtrap.io', recipients = ['sergioess@hotmail.com'])
#     msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#     mail.send(msg)
#     return "Message sent!"


def mailtoUser(nombre,  correo):
    msg = Message('Usuario Registrado', sender = 'TecnoAmbiental', recipients = [correo])
    msg.body = "Estimado " + str(nombre) + " su cuenta  ha sido creada."
    mail.send(msg)

def about():
    return render_template('about.html')

def home2():
    return render_template('home2.html')
