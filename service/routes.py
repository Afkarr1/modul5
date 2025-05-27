from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Dummy data simulasi
PRODUCTS = [
    {"id": 1, "name": "Printer", "category": "Office", "price": 1200000, "available": True},
    {"id": 2, "name": "Scanner", "category": "Office", "price": 900000, "available": True}
]

# READ - GET /products/<id>
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        abort(404)

# UPDATE - PUT /products/<id>
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        abort(404)
    data = request.get_json()
    product.update({
        "name": data.get("name", product["name"]),
        "category": data.get("category", product["category"]),
        "price": data.get("price", product["price"]),
        "available": data.get("available", product["available"])
    })
    return jsonify(product), 200

# DELETE - DELETE /products/<id>
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global PRODUCTS
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        abort(404)
    PRODUCTS = [p for p in PRODUCTS if p["id"] != product_id]
    return '', 204

