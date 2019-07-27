import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# instanciamos la app
app = Flask(__name__) 
# creamos la variable de la ruta hacia el archivo sqlite
basedir = os.path.abspath(os.path.dirname(__file__)) 
# configuramos la base de datos sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializamos la base de datos
db = SQLAlchemy(app) 
# Inicializamos Marshmallow
ma = Marshmallow(app) 

# modelo del producto (que describe como debe ser el objeto)
class Smartlog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.column(db.DateTime)
  name = db.column(db.String(50))
  depth = db.column(db.Integer)
  leave_surface = db.column(db.DateTime)
  leave_bottom = db.column(db.DateTime)
  bottom_time = db.column(db.Integer)

  def __init__(self, date, name, depth, leave_surface, leave_bottom, bottom_time):
    self.date = date
    self.name = name
    self.depth = depth
    self.leave_surface = leave_surface
    self.leave_bottom = leave_bottom
    self.bottom_time = bottom_time
# se crea el schema (esquema) de el Smartlog
class SmartlogSchema(ma.Schema):
  class Meta:
    fields = ('id', 'date', 'name', 'depth', 'leave_surface', 'leave_bottom', 'bottom_time')

# inicializamos el esquema
smartlog_schema = SmartlogSchema()
smartlogs_schema = SmartlogSchema(many=True)

# crear Smartlog
@app.route('/smartlogs', methods=['POST'])
def add_smartlog():
  date = request.json['date']
  name = request.json['name']
  depth = request.json['depth']
  leave_surface = request.json['leave_surface']
  leave_bottom = request.json['leave_bottom']
  bottom_time = request.json['bottom_time']

  new_smartlog = Smartlog(date, name, depth, leave_surface, leave_bottom, bottom_time)
  db.session.add(new_smartlog)
  db.session.commit()
  return smartlog_schema.jsonify(new_smartlog)

# listar todos los smartlogs
@app.route('/smartlogs', methods=['GET'])
def get_smartlogs():
  all_smartlogs = Smartlog.query.all()
  result = smartlogs_schema.dump(all_smartlogs)
  print(result)
  return jsonify(result.data)

# corremos el servidor
if __name__ == '__main__':
  app.run(debug=True)