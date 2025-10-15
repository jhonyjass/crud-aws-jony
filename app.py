import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from conexion import db


app = Flask(__name__)
app.secret_key = "clave-secreta"

# Configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'postgresql://postgres:postgres@db:5432/proyecto_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la conexión
db.init_app(app)
migrate = Migrate(app, db)

from models.tareas import Tarea




# -------------------------
# Rutas principales
# -------------------------
@app.route("/")
def index():
    tareas = Tarea.query.order_by(Tarea.fecha_creacion.desc()).all()
    return render_template("tareas.html", tareas=tareas)


# -------------------------
# Agregar tarea (solo POST)
# -------------------------
@app.route("/agregar", methods=["POST"])
def agregar():
    descripcion = request.form.get("descripcion")
    prioridad = request.form.get("prioridad")

    if not descripcion or not prioridad:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("index"))

    try:
        nueva = Tarea(descripcion=descripcion, prioridad=prioridad)
        db.session.add(nueva)
        db.session.commit()
        flash("Tarea agregada correctamente.", "success")
    except Exception:
        db.session.rollback()
        flash("Error al agregar tarea.", "danger")

    return redirect(url_for("index"))


# -------------------------
# Editar tarea (solo POST)
# -------------------------
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    tarea = Tarea.query.get_or_404(id)
    descripcion = request.form.get("descripcion")
    prioridad = request.form.get("prioridad")
    if not descripcion or not prioridad:
        flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for("index"))
    try:
        tarea.descripcion = descripcion
        tarea.prioridad = prioridad
        db.session.commit()
        flash("Tarea actualizada correctamente.", "success")
    except Exception:
        db.session.rollback()
        flash("Error al actualizar tarea.", "danger")
    return redirect(url_for("index"))


@app.route("/editar_estado/<int:id>", methods=["POST"])
def editar_estado(id):
    tarea = Tarea.query.get_or_404(id)
    try:
        tarea.completada = not tarea.completada
        db.session.commit()
        estado = "completada" if tarea.completada else "pendiente"
        flash(f"Tarea marcada como {estado}.", "success")
    except Exception:
        db.session.rollback()
        flash("Error al cambiar el estado de la tarea.", "danger")

    return redirect(url_for("index"))


@app.route("/eliminar/<int:id>", methods=["GET"])
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    try:
        db.session.delete(tarea)
        db.session.commit()
        flash("Tarea eliminada correctamente.", "success")
    except Exception:
        db.session.rollback()
        flash("Error al eliminar tarea.", "danger")

    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
