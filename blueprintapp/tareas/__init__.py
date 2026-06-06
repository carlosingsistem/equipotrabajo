from flask import Blueprint

bp_tarea = Blueprint('bp_tarea',__name__,template_folder='templates', url_prefix="/tareas")

from blueprintapp.tareas import routes