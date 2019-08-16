from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
  return jsonify({ "message": "Pong!" })

@app.route('/products')
def productList():
  return jsonify({ "message": "Products List", "products": products})

@app.route('/products/<int:id>')
def productGet(id):
  foundList = [product for product in products if product['id'] == id]
  if (len(foundList) > 0):
    return jsonify({"products": foundList[0]})
  return jsonify({ "message": "product not found"})

@app.route('/products', methods=['POST'])
def productCreate():
  newProduct = { 
	"id": len(request.json['name']), 
	"name": request.json['name'], 
	"price": request.json['price'], 
	"quantity": request.json['quantity']
  }
  products.append(newProduct)
  return jsonify({ "message": "product created", "products": products })

@app.route('/products/<int:id>', methods=['PUT'])
def productEdit(id):
  foundList = [product for product in products if product['id'] == id]
  if (len(foundList) > 0):
    foundList[0]['id'] = request.json['id']
    foundList[0]['name'] = request.json['name']
    foundList[0]['quantity'] = request.json['quantity']
    foundList[0]['price'] = request.json['price']
    return jsonify({"message": "product updated", "product": products})

  return jsonify({ "message": "product not found"})

@app.route('/products/<int:id>', methods=['DELETE'])
def productDelete(id):
  foundList = [product for product in products if product['id'] == id]
  if (len(foundList) > 0):
    products.remove(foundList[0])
    return jsonify({"message": "product deleted", "products": products})
  return jsonify({ "message": "product not found"})


if __name__ == "__main__":
  app.run(debug=True, port=3002)