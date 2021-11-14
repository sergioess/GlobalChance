from app import database
from sqlalchemy import asc, desc
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

from models.ciudad import Ciudad

class Banner(database.Model):

    __tablename__ = 'banners'

    id = database.Column(database.Integer, primary_key=True)
    archivo = database.Column(database.String(50), nullable=False)
    titulo = database.Column(database.String(50), nullable=False)
    descripcion = database.Column(database.String(50), nullable=False)
    activo = database.Column(database.Boolean, nullable=False)

#este es el toString personalizado
    def __str__(self):
        return f"<Banner {self.id} {self.fecha_registro} {self.id_ciudad} {self.Banner_aire} {self.id_usuario} >"

    def __init__(self, archivo, titulo, descipcion, activo):
        self.archivo = archivo
        self.titulo = titulo
        self.descipcion = descipcion
        self.activo = activo
        


    @staticmethod
    def get_all():
        return Banner.query.all()


    def get_by_id(id):
        return Banner.query.filter_by(id=id).first()


    def save(self):

        print (self)
        database.session.add(self)
        database.session.commit()

    def delete(id):
        bannerElimina = Banner.query.filter_by(id=self.id).first()
        database.session.delete(bannerElimina)
        database.session.commit()

    def inactiva(self):
        bannerModifica = Banner.query.filter_by(id=self.id).first()
        bannerModifica.activo = False

        database.session.commit()