# app/home/views.py

from flask import render_template, url_for, redirect, request, session

from . import home
from forms import QueryForm
from .. import db
from ..models import Word

@home.route('/', methods=['GET','POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    form = QueryForm()
    if form.validate_on_submit():
        return redirect(url_for('home.show_results'), code=307)

    return render_template('home/index.html', form=form, title="Psiholeks")

@home.route('/pretraga', methods=['POST'])
def show_results():
    """
    Show query results
    """
    words = Word.query.filter_by(rijec=request.form.get('rijec')).all();
    return render_template('home/results.html', words=words, title="Rijeci")
