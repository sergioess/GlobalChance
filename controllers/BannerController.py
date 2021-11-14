from flask import Flask,session
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import sys
import os
from flask_session import Session

from models.banner import Banner


app = Flask(__name__)
app.config.from_object('config')


# con este se listan los benners
# @login_required
def index():
    bannersLista = Banner.get_Active()
    print(bannersLista)
    # return render_template('/banner/index.html', banner=bannersLista)
    return render_template('/banner/index.html', bannersLista = bannersLista)    



# @login_required
def store():
    _archivo = request.files.get('txtFoto')
    _titulo = request.form.get('txtTitulo')
    _descripcion = request.form.get('txtDescripcion')
	
    now=datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if(_archivo.filename != ''):
        print('El Archivo es: ' , _archivo)
        nuevoNombreFoto = tiempo + _archivo.filename
        _archivo.save("banner/" + nuevoNombreFoto)

   
    banner = Banner(nuevoNombreFoto, _titulo, _descripcion, True)
    print(banner)
    if banner.save():
        return redirect('/producto')
    else:
        session.pop('_flashes', None)
        flash(f'Error al guardar el Banner, intentelo nuevamente', 'danger')
        return redirect('/banner')  

# con este método se elimina un registro
def destroy(banner_id):
    Banner.delete(banner_id)
    return redirect('/banner')

def inactivaBanner(banner_id):
    Banner.inactivaBanner(banner_id)
    return redirect('/banner')