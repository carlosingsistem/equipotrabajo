# Librerias a usar en el modulo
from flask import request, render_template, redirect, url_for
from flask_login import login_required
# Referencia a la base de datos
from blueprintapp.extensions import db
# Modelos con los que interactura el modulo
from blueprintapp.tareas.models import Tarea
from blueprintapp.tareas import bp_tarea

# Para listar las tareas
@bp_tarea.route("/")
@login_required
def index():
    tareas = Tarea.query.all()
    return render_template('tareas/index.html',tareas=tareas)

# Para crear una nueva tarea
@bp_tarea.route("/create",methods=['GET','POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('tareas/create.html')
    elif request.method == 'POST':
        descripcion = request.form.get('descripcion')
        completado = True if 'completado' in request.form.keys() else False
        # Crear un objeto miembro
        tarea = Tarea(descripcion=descripcion,completado=completado)
        # Insertar en la bd a traves del ORM
        db.session.add(tarea)
        db.session.commit()
        # Redireccion al listado de tareas
        return redirect(url_for('bp_tarea.index'))
        
# Para actualizar una tarea
@bp_tarea.route("/edit/<int:id_tarea>" , methods=["GET", "POST"])
@login_required
def edit_tarea(id_tarea):
    if request.method == "POST":
        descripcion = request.form['descripcion']
        completado = True if 'completado' in request.form.keys() else False
        # Buscamos la tarea en la BD
        tarea = Tarea.query.get(id_tarea)
        # Actualizamos los datos la tarea
        tarea.descripcion = descripcion
        tarea.completado = completado
        db.session.commit()
        # Redirigimos al listado
        return redirect(url_for("bp_tarea.index"))
    
    # Si es GET, mostramos el formulario con datos actuales
    tarea = Tarea.query.get(id_tarea)
    
    return render_template("tareas/edit.html" , tarea=tarea)

# Para eliminar una tarea
@bp_tarea.route("/delete/<int:id_tarea>")
@login_required
def delete_tarea(id_tarea):
    # Buscamos la tarea en la BD por su id
    tarea = Tarea.query.get(id_tarea)
    # Eliminamos el registro
    db.session.delete(tarea)
    db.session.commit()
    # Redirigimos al listado de tareas
    return redirect(url_for("bp_tarea.index"))