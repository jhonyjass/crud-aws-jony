from conexion import db

class Tarea(db.Model):
    __tablename__ = 'tareas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    completada = db.Column(db.Boolean, default=False, nullable=False)
    prioridad = db.Column(db.String(10), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def __init__(self, descripcion, prioridad, completada=False):
        self.descripcion = descripcion
        self.completada = completada
        self.prioridad = prioridad
