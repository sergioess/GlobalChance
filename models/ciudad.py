from app import database
from sqlalchemy import asc, desc


class Ciudad(database.Model):

    __tablename__ = 'ciudades'

    id = database.Column(database.Integer, primary_key=True)
    nombre_ciudad = database.Column(database.String(50), nullable=False)
    id_departamento = database.Column(database.Integer, nullable=False)
    area = database.Column(database.Float, nullable=False)
    poblacion = database.Column(database.Float, nullable=False)


#este es el toString personalizado
    def __str__(self):
        return f"<Ciudad {self.id} {self.nombre_ciudad} {self.id_departamento} {self.area} {self.poblacion} >"

    def __init__(self):
        pass


    @staticmethod
    def get_all():
        return Ciudad.query.all()


    def get_by_id(id):
        return Ciudad.query.filter_by(id=id).first()

    def get_ciudad_by_iddpto(id):
        return Ciudad.query.filter_by(id_departamento=id).all()