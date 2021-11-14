from flask import Flask, session
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.usuario import Usuario
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from app import Bcrypt ,bcrypt
from flask_session import Session

@login_required
def index():
    
    user = Usuario.query.filter_by(id=current_user.id).first()
    if(user.perfil!=3):
        session.pop('_flashes', None)
        flash(f'Acceso no autorizado', 'danger')
        return redirect('/home')   

    usuariosLista = Usuario.get_all_activo()

    return render_template('/usuario/index.html', usuarios=usuariosLista)

@login_required
def store():
    _id_usuario = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _correo = request.form.get('txtCorreo')
    _pass = request.form.get('txtPassword')
    _confirmpass = request.form.get('txtConfirmarPassword')
    _perfil = request.form.get('txtperfil')
    if _pass == _confirmpass:
        _password = bcrypt.generate_password_hash(_pass).decode('utf-8')
        usuario = Usuario(_id_usuario,_nombre, _correo, _password, _perfil)
        usuario.activo = 1
        if usuario.save():
            return redirect('/usuario')
        else:
            session.pop('_flashes', None)
            flash(f'El usuario ya existe en la base de datos, por favor digite otro nombre', 'danger')
            return redirect('/usuario')
    
def show():
    pass

@login_required
def update():
    _id_usuario = request.form.get('txtId')
    _nombre = request.form.get('txtNombre')
    _correo = request.form.get('txtCorreo')
    _password = bcrypt.generate_password_hash(request.form.get('txtPassword')).decode('utf-8')
    _perfil = request.form.get('txtperfil')
    usuario = Usuario(_id_usuario, _nombre, _correo, _password, _perfil)
    print(usuario)
    usuario.update()
    return redirect('/usuario')

@login_required
def destroy(usuario_id_usuario):
    usuario = Usuario(usuario_id_usuario, "User", "User", "User", 1)
    Usuario.delete(usuario)
    return redirect('/usuario')

@login_required
def activar(usuario_id_usuario):
    Usuario.activar(usuario_id_usuario)

    usuariosInactivos = 0
    if Usuario.count_records_inacticos() > 0:
        usuariosInactivos = Usuario.count_records_inacticos()
    
    session['inactivos'] = usuariosInactivos    
    return redirect('/usuario')    
    

# @login_required
# def inactivo():
#     #print("Ingresamos a Inactivo")
#     lista_usuarios_inac=Usuario.get_all_inactivo()
#     return render_template('/usuario/inactivos.html', usuarios=lista_usuarios_inac)

@login_required
def activar_user(usuario_id_usuario):
    Usuario.activa_user(usuario_id_usuario)
    lista_usuarios_inac=Usuario.get_all_inactivo()
    return render_template('/usuario/inactivos.html', usuarios=lista_usuarios_inac)

