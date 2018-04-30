# app/home/views.py

from flask import render_template, url_for, redirect

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
        return redirect(url_for('home.show_results'))

    return render_template('home/index.html', form=form, title="Psiholeks")

@home.route('/results')
def show_results():
    """
    Show query results
    """
    words = Word.query.all();
    return render_template('home/results.html', words=words, title="Rijeci")
