from flask import render_template
from flask_login import login_required
from blueprintapp.core import bp_core

@bp_core.route("/")
def index():
    return render_template('core/index.html')

@bp_core.route("/dashboard")
@login_required
def dashboard():
    return render_template("core/dashboard.html")