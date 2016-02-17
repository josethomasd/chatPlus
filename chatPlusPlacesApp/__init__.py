from flask import Flask

chatPlusPlacesApp = Flask(__name__)
chatPlusPlacesApp.config.from_object('config')

from chatPlusPlacesApp import views
