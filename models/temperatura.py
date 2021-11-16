from app import database
from sqlalchemy import asc, desc
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from flask_login import current_user

from models.ciudad import Ciudad

class Temperatura(database.Model):

    __tablename__ = 'registro_temperatura'

    id = database.Column(database.Integer, primary_key=True)
    fecha_registro = database.Column(database.Date, nullable=False)
    id_ciudad = database.Column(database.Integer, ForeignKey("ciudades.id"))
    temperatura_aire = database.Column(database.Float, nullable=False)
    id_usuario = database.Column(database.Integer, nullable=False)

    temp_ciudad = database.relationship("Ciudad", backref='ciudades.id', lazy='joined')

#este es el toString personalizado
    def __str__(self):
        return f"<Temperatura {self.id} {self.fecha_registro} {self.id_ciudad} {self.temperatura_aire} {self.id_usuario} >"

    def __init__(self, id_ciudad, temperatura_aire, id_usuario,fecha_registro ):
        self.id_ciudad = id_ciudad
        self.temperatura_aire = temperatura_aire
        self.id_usuario = id_usuario
        self.fecha_registro = fecha_registro
        


    @staticmethod
    def get_all():
        temperatura = database.session.query(Temperatura, Ciudad).join(Ciudad).filter(Temperatura.id_usuario==current_user.id).order_by(asc(Temperatura.id)).all()
        # return Temperatura.query.all()
        # print (temperatura)
        return temperatura


    def get_by_id(id):
        return Temperatura.query.filter_by(id=id).first()


    def save(self):

        # print ('Tempearatura desde Modelo', self)
        database.session.add(self)
        database.session.commit()

    def delete(id):
        # print(id)
        temperaturaElimina = Temperatura.query.filter_by(id=id).first()
        # print(temperaturaElimina)

        database.session.delete(temperaturaElimina)
        database.session.commit()

    @staticmethod
    def getDatos(ciudad):
        # print("hey por aca")
        temperatura = database.session.query(Temperatura.temperatura_aire).filter(Temperatura.id_ciudad==ciudad).all()
        # print(temperatura)
        return temperatura