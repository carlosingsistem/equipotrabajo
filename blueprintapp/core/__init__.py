from flask import Blueprint

bp_core = Blueprint('bp_core',__name__, template_folder='templates')

from blueprintapp.core import routes