from flask import Flask, request, jsonify
import datetime
from utils import *

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    try:
        print(request.json)
        request_data = request.json
        con, cur = db_con()
        query = "select * from users where email=%s and password=%s"
        cur.execute(query, (request_data['email'], request_data['password']))
        data = cur.fetchone()
        if (data):
            print(data, flush=True)
            return jsonify({
                "hello": "hello"
            })
        return jsonify({
            "message": "unaauthorised"
        }), 401
    except TypeError as e:
        return jsonify({
            'message': str(e)
        }), 500
    except Exception as e:
        return jsonify({
            'message': str(e)
        }), 500


@app.route("/product")
def products():
    try:
        con, cur = db_con()
        cur.execute("select id,product_name,price,image from product")
        data = cur.fetchall()
        return jsonify({
            'Product': data
        })
    except TypeError as e:
        return jsonify({
            'message': str(e)
        }), 500
    except Exception as e:
        return jsonify({
            'message': str(e)
        }), 500
    finally:
        if (con):
            con.close()


if __name__ == "__main__":
    app.run(debug=True, port=80)
