# Librerias a usar en el modulo
from flask import request,render_template,redirect,url_for,Blueprint

# Referencia a la base de datos
from blueprintapp.app import db
# Modelos con los que interactura el modulo
from blueprintapp.miembros.models import Miembro

bp_miembro = Blueprint('bp_miembro',__name__,template_folder='templates')

@bp_miembro.route("/")
def index():
    miembros = Miembro.query.all()
    return render_template('miembro/index.html',miembros=miembros)

@bp_miembro.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('miembro/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        # Crear un objeto miembro
        miembro = Miembro(nombre=nombre,email=email)
        # Insertar en la bd a traves del ORM
        db.session.add(miembro)
        db.session.commit()
        # Redireccion al listado de miembros
        return redirect(url_for('bp_miembro.index'))
        
# Para editar un miembro    
@bp_miembro.route("/edit/<int:id_miembro>", methods=['GET', 'POST'])
def edit_miembro(id_miembro):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        # Buscamos el miembro en la BD
        miembro = Miembro.query.get(id_miembro)
        # Actualizamos sus datos
        miembro.nombre = nombre
        miembro.email = email
        db.session.commit()
        # Redireccion al listado de miembros
        return redirect(url_for('bp_miembro.index'))
    
    # Si es GET, mostramos el formulario con datos actuales
    miembro = Miembro.query.get(id_miembro)
    
    return render_template("miembro/edit.html", miembro=miembro)


