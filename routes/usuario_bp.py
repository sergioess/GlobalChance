from flask import Blueprint

from controllers.UsuarioController import index, store, show, update, destroy, activar,  activar_user, usuarioEditor

usuario_bp = Blueprint('usuario_bp', __name__, template_folder='templates/usuario')
usuario_bp.route('/', methods=['GET'])(index)
usuario_bp.route('/store', methods=['POST'])(store)
usuario_bp.route('/<int:usuario_id_usuario>', methods=['GET'])(show)
usuario_bp.route('/update', methods=['POST'])(update)
usuario_bp.route('/destroy/<int:usuario_id_usuario>', methods=['GET', 'POST', 'DELETE'])(destroy)
usuario_bp.route('/editor/<int:usuario_id_usuario>', methods=['GET', 'POST'])(usuarioEditor)
# usuario_bp.route('/activar/<int:usuario_id_usuario>', methods=['GET', 'POST', 'DELETE'])(activar)
# usuario_bp.route('/inactivo', methods=['GET'])(inactivo)
# usuario_bp.route('/activar_user/<int:usuario_id_usuario>', methods=['GET', 'POST', 'DELETE'])(activar_user)