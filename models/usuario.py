from app import database
from sqlalchemy import asc, desc
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


class Usuario(UserMixin,database.Model):

    __tablename__ = 'usuarios'

    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(50), nullable=False)
    correo = database.Column(database.String(50), unique=True, nullable=False)
    password = database.Column(database.String(20), nullable=False)
    activo = database.Column(database.Integer, nullable=False)
    perfil = database.Column(database.Integer, nullable=False)

#este es el toString personalizado
    def __str__(self):
        return f"<Usuario {self.id} {self.nombre} {self.correo} {self.password} {self.activo} {self.perfil} >"

    def __init__(self):
        self.activo = 1
        self.perfil = 1


    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def count_records():
        return Usuario.query.count()              

    @staticmethod
    def get_all_activo():
        return Usuario.query.filter_by(activo=1).order_by(asc(Usuario.id))   

    def get_by_id(id):
        return Usuario.query.filter_by(id=id).first()
    
    def save(self):
        if not self.id:
            usuario_existente = Usuario.query.filter_by(correo=self.correo).first()
            #print(usuario_existente.nombre)
            if usuario_existente is not None:
                print("Usuario ya existe en la base de datos")
                return False
            else:
                print("Usuario nuevo")
                
                database.session.add(self)
                database.session.commit()
                return True


    def update(self):
        usuarioActualiza = Usuario.query.filter_by(id=self.id).first()
        usuarioActualiza.nombre = self.nombre
        usuarioActualiza.apellidos = self.apellidos
        usuarioActualiza.correo = self.correo
        usuarioActualiza.nombre_usuario = self.nombre_usuario
        usuarioActualiza.password = self.password
        usuarioActualiza.rol = self.rol
        database.session.commit()
        return usuarioActualiza

    def delete(id):
        #print(self.id)
        usuarioActualiza = Usuario.query.filter_by(id=id).first()
        usuarioActualiza.activo = 0
        database.session.commit()
        return 1    

    @staticmethod
    def usuarioEditor(id):
        usuarioActualiza = Usuario.query.filter_by(id=id).first()
        usuarioActualiza.perfil = 2
        database.session.commit()
        return usuarioActualiza 
        
    # @staticmethod
    # def activar(id):
    #     usuarioActualiza = Usuario.query.filter_by(id=id).first()
    #     usuarioActualiza.is_active = True
    #     database.session.commit()


    # @staticmethod
    # def activa_user(idbuscar):
    #     user = Usuario.query.filter_by(id=idbuscar).first()
    #     user.activo= 1
    #     database.session.commit()

    @staticmethod
    def validarUsuario(correo_enviado):
        return True
        usuario_existente = Usuario.query.filter_by(correo=correo_enviado).first()
        # print(correo_enviado)
        if usuario_existente is not None:
            print("Usuario ya existe en la base de datos")
            return False
        else:
            return True
