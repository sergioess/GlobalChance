from flask import Blueprint

from controllers.InicioController import index, home, logout, login, about, home2, frmlogin2, frmRegistrar2, consultar
# from controllers.InicioController import index, home, frmlogin, logout, login, frmRegistrar

inicio_bp = Blueprint('inicio_bp', __name__, template_folder='templates/')
inicio_bp.route('/', methods=['GET'])(index)
# TODO
inicio_bp.route('/home', methods=['GET'])(home)
inicio_bp.route('/login', methods=['POST'])(login)
inicio_bp.route('/logout', methods=['GET'])(logout)
inicio_bp.route('/consultar', methods=['GET'])(consultar)
inicio_bp.route('/frmlogin', methods=[ "POST"])(frmlogin2)
inicio_bp.route('/frmregistro', methods=["GET", "POST"])(frmRegistrar2)
# inicio_bp.route('/mailtoadmin', methods=["GET", "POST"])(mailtoadmin)
inicio_bp.route('/about', methods=['GET'])(about)
inicio_bp.route('/home2', methods=['GET'])(home2)


