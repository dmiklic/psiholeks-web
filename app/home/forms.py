# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
#from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Word

class QueryForm(FlaskForm):
    """
    Form for users to query the dictionary
    """
    rijec = StringField(u'Riječ', validators=[])
    submit = SubmitField(u'Pretraži')
