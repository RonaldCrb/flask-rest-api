from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__) # <== instanciamos la app

basedir = os.path.abspath(os.path.dirname(__file__)) # <== creamos la variable de la ruta hacia el archivo sqlite
# configuramos la base de datos sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # <== Inicializamos la base de datos

ma = Marshmallow(app) # <== Inicializamos Marshmallow

@app.route('/', methods=['GET']) # <== definimos la ruta

def get(): # <== definimos el metodo que es invocado por la ruta
  return jsonify({ 'msg': 'hola mundo' })



if __name__ == '__main__':
  app.run(debug=True) # <== corremos el servidor
