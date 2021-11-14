from flask import Blueprint

from controllers.BannerController import index, store, destroy

banner_bp = Blueprint('banner_bp', __name__, template_folder='templates/banner')
banner_bp.route('/', methods=['GET'])(index)
banner_bp.route('/store', methods=['POST'])(store)
banner_bp.route('/destroy/<int:banner_id>', methods=['GET', 'POST', 'DELETE'])(destroy)