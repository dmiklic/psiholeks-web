# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
#from wtforms_components import NumberRangeField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Word

class QueryForm(FlaskForm):
    """
    Form for users to query the dictionary
    """
    rijec = StringField(u'Riječ', validators=[])
    konkretnost = StringField('Konkretnost',render_kw={'disabled':'disabled'})
    predocivost = StringField(u'Predočivost',render_kw={'disabled':'disabled'})
    dob_usvajanja = StringField(u'Dob usvajanja',render_kw={'disabled':'disabled'})
    subj_frekvencija = StringField(u'Subjektivna frekvencija',render_kw={'disabled':'disabled'})
    submit = SubmitField(u'Pretraži')
