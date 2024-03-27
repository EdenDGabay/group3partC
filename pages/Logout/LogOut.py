from flask import Blueprint, render_template, session
from flask import request, redirect, url_for
from utilities.db.mongo_util import mongo_db_instance

LogOut = Blueprint('LogOut',
                   __name__)

@LogOut.route('/')
def logout():
    session.clear()
    return redirect(url_for('HomePage.index'))
