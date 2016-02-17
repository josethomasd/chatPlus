from flask import render_template
from flask import request
from flask import flash
from flask import redirect

from flask.ext.wtf import Form
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

from chatPlusPlacesApp import chatPlusPlacesApp

from chatPlusPlacesApp.lib.classes import chatPlusConstants
from chatPlusPlacesApp.lib.classes import chatPlusPlacesJson

#from .forms import searchForm
# index view function suppressed for brevity

class searchForm(Form):
    searchString = StringField('searchString', validators=[DataRequired()])
#class searchOption(Form):
#    option = request.form['options']

constantsObject = chatPlusConstants.chatPlusConstants

@chatPlusPlacesApp.route('/',methods=['GET', 'POST'])
@chatPlusPlacesApp.route('/index', methods=['GET', 'POST'])
@chatPlusPlacesApp.route('/indexnew', methods=['GET', 'POST'])
def index():
    form = searchForm()
    if form.validate_on_submit():
       	searchString = form.searchString.data
        print('working')
        placesObject = chatPlusPlacesJson.chatPlusPlacesJson()
        placeSearch = placesObject.getJSON(searchString)
        return render_template('indexnew.html',title='Home',form=form,placeSearch=placeSearch)
    #if form.validate_on_submit():
    #    form = searchOption(request.form)
    #    searchOption=form.searchOption.data
    #    placesJson = placesObject.getJSONFinal(searchOption)
    #    return render_template('index.html',title='Home',form=form,placeJson=placeJson)
    return render_template('index.html',title='Home',form=form,placesJson=None)

def indexnew():
    if form.validate_on_submit():
        form = searchOption(request.form)
        print('working1')
        earchOption=form.searchOption.data
        placesJson = placesObject.getJSONFinal(searchOption)
        return render_template('indexnew.html',title='Home',form=form,placeJson=placeJson)
    return render_template('index.html',title='Home',form=form,placesJson=None)
