
# Project 2 feature branch

from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="inventory",
        user="inventory",
        password="inventorypass"
    )


@app.route("/")
def home():
    return "Inventory API is running!"


@app.route("/products")
def products():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price, quantity FROM products")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    products_list = []

    for row in rows:
        products_list.append({
            "id": row[0],
            "name": row[1],
            "price": float(row[2]),
            "quantity": row[3]
        })

    return jsonify(products_list)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, price, quantity FROM products WHERE id = %s",
        (product_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "id": row[0],
        "name": row[1],
        "price": float(row[2]),
        "quantity": row[3]

    })




@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE products
        SET name = %s, price = %s, quantity = %s
        WHERE id = %s
        RETURNING id
        """,
        (
            data["name"],
            data["price"],
            data["quantity"],
            product_id
        )
    )

    row = cur.fetchone()

    if row is None:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"error": "Product not found"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "message": "Product updated",
        "id": row[0]
    })


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM products WHERE id = %s RETURNING id",
        (product_id,)
    )

    row = cur.fetchone()

    if row is None:
        conn.rollback()
        cur.close()
        conn.close()
        return jsonify({"error": "Product not found"}), 404

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "message": "Product deleted",
        "id": row[0]
    })



@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO products (name, price, quantity)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (data["name"], data["price"], data["quantity"])
    )

    product_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "message": "Product created",
        "id": product_id
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
