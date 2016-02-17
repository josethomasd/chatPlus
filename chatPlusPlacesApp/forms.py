from flask.ext.wtf import Form
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired
from flask import request, redirect

class searchForm(Form):
    searchString = StringField('searchString', validators=[DataRequired()])
class searchOption(Form):
    request.form.get('option')
