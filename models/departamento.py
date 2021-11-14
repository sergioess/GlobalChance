from app import database
from sqlalchemy import asc, desc


class Departamento(database.Model):

    __tablename__ = 'departamentos'

    id = database.Column(database.Integer, primary_key=True)
    nombre_departamento = database.Column(database.String(50), nullable=False)


#este es el toString personalizado
    def __str__(self):
        return f"<Departamento {self.id} {self.nombre} >"

    def __init__(self):
        pass


    @staticmethod
    def get_all():
        return Departamento.query.all()


    def get_by_id(id):
        return Departamento.query.filter_by(id=id).first()