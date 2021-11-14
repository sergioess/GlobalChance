from flask import Flask,session
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import sys
import os
from flask_session import Session

from models.temperatura import Temperatura


app = Flask(__name__)
app.config.from_object('config')



# con este se listan los benners
# @login_required
def index():
    temperaturaLista = Temperatura.get_all()
    print(temperaturaLista)
    # return render_template('/temperatura/index.html', banner=temperaturaLista)
    return render_template('/temperatura/index.html')    



# @login_required
def store():
    _ciudad = request.form.get('txtCiudad')
    _temperatura = request.form.get('txtTemperatura')
    _usuario = request.form.get('txtUsuario')
		  
    temperatura = Temperatura(_ciudad, _temperatura, _usuario)
    print(temperatura)
    if temperatura.save():
        return redirect('/temperatura')
    else:
        session.pop('_flashes', None)
        flash(f'Error al guardar el registro', 'danger')
        return redirect('/temperatura')  

# con este método se elimina un registro
def destroy(temperatura_id):
    Temperatura.delete(temperatura_id)
    return redirect('/temperatura')