from flask import Flask, session
from app import Bcrypt ,bcrypt, mail

from flask import config, render_template, redirect, url_for, request, abort, flash, jsonify
from sqlalchemy import desc
from models.usuario import Usuario



# @login_required
def home():
    # print("Actual logueado", current_user)
    # user = Usuario.query.filter_by(id=current_user.id).first()


    return render_template('/home.html') 

def index():
    
    return render_template('/index.html')