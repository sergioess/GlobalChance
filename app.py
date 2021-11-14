from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_session import Session

from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config.from_object('config')
from flask import send_from_directory


bcrypt = Bcrypt(app)
lasession = Session(app)
lasession.init_app(app)


database = SQLAlchemy(app)
mail = Mail(app)
from models.usuario import Usuario
# #ACA LAS IMPORTACION DE LAS RUTAS
from routes.inicio_bp import inicio_bp


# #ACA REGISTRAMOS LAS RUTAS
app.register_blueprint(inicio_bp, url_prefix='/')


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "inicio_bp.frmlogin"

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))


@app.route('/img/<nombreFoto>')
def img(nombreFoto):
    return send_from_directory(app.config['CARPETA_IMG'], nombreFoto)

@app.route('/uplbanner/<nombreFoto>')
def uplproductos(nombreFoto):
    # print(app.config['CARPETA'])
    return send_from_directory(app.config['CARPETA_PTOS'], nombreFoto)



if __name__ == '__main__':
    app.run(debug=False)

