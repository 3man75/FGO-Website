import shutil
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import requests
import json
import urllib
import os




app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def create_app():

     #Starter page where users come in

     return render_template('index.html')


#Shows one particular servant who is my favorite
@app.route('/favorite servant')
def favServant():

     return render_template('servant.html')


#Below is to show ALL NA Servants in the game
@app.route('/all')
def naServants():
     
     return render_template('json.html')

if __name__ == '__main__':

    

    #create_app()

    PORT = os.getenv('PORT', 2000)

    app.run(host="0.0.0.0", debug=True, port = PORT)  #port=PORT

    #checking for push
