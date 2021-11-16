from flask import Blueprint

from controllers.TemperaturaController import index, store, destroy, datos

temperatura_bp = Blueprint('temperatura_bp', __name__, template_folder='templates/temperatura')
temperatura_bp.route('/', methods=['GET'])(index)
temperatura_bp.route('/store', methods=['POST'])(store)
temperatura_bp.route('/datos', methods=['POST'])(datos)
temperatura_bp.route('/destroy/<int:temperatura_id>', methods=['GET', 'POST', 'DELETE'])(destroy)