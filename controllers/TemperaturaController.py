from flask import Flask,session
from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import sys
import os
from flask_session import Session

from models.temperatura import Temperatura
from models.ciudad import Ciudad


app = Flask(__name__)
app.config.from_object('config')



# con este se listan los benners
# @login_required
def index():
    temperaturaLista = Temperatura.get_all()
    # print(temperaturaLista)
    ciudadLista = Ciudad.get_all()
    # print(ciudadLista)

    return render_template('/temperatura/index.html', ciudadLista=ciudadLista, temperaturaLista=temperaturaLista)    



# @login_required
def store():
    _ciudad = request.form.get('txtCiudad')
    _rtemperatura = request.form.get('txtTemperatura')
    _usuario = request.form.get('txtUsuario')

	# print('Ingresado', _ciudad, _rtemperatura, _usuario)
    date = datetime.now()	  
    temperatura = Temperatura(_ciudad, _rtemperatura, _usuario, date)
    # print(temperatura)
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


def datos():
    _ciudad = request.form.get('ciudad')
    print("La ciudad que envia", _ciudad)
    datos = Temperatura.getDatos(_ciudad)
    datos2 = []
    print(datos)
    for x in datos:
        
        for y in x:
            datos2.append(y)
    print(datos2)
    return jsonify(datos2)