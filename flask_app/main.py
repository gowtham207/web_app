import os
import jwt
from flask import Flask, request, jsonify, send_from_directory, abort
import datetime
import bcrypt
from werkzeug.security import safe_join
from utils import db_con, logger, SECRET_SALT, SECRET_KEY, EFS_ROOT

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({
        "version": "1.2"
    })

@app.route('/images/<path:filename>', methods=['GET'])
def serve_image(filename):
    file_path = safe_join(EFS_ROOT, filename)
    if os.path.isfile(file_path):
        return send_from_directory(EFS_ROOT, filename)
    else:
        abort(404, description="Resource not found")

@app.before_request
def before_request():
    print(request.endpoint)
    if request.endpoint in ['root', 'login', 'register']:
        return

    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(" ")[1]
    
    if not token:
        logger.warning('Token is missing in the request.')
        return jsonify({'message': 'Token is missing!'}), 403
    
    try:
        con, cur = db_con()
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        request.user_id = data['user_id']
        request.user_email = data['user_email']
        print(request.user_email)

        query = "SELECT 1 FROM users WHERE email=%s AND deleted_at IS NULL"
        cur.execute(query, (request.user_email,))
        if not cur.fetchone():
            logger.warning('User not found for the provided email.')
            return jsonify({'message': 'User not found!'}), 403
    except jwt.ExpiredSignatureError:
        logger.warning('Token has expired.')
        return jsonify({'message': 'Token has expired!'}), 403
    except jwt.InvalidTokenError:
        logger.warning('Invalid token.')
        return jsonify({'message': 'Invalid token!'}), 403
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({'message': 'An unexpected error occurred!'}), 500
    finally:
        if con:
            con.close()

@app.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.json
        con, cur = db_con()
        email = request_data['email']
        password = request_data['password']

        query = "SELECT id, fname, lname, email, password FROM users WHERE email=%s AND deleted_at IS NULL"
        cur.execute(query, (email,))
        user = cur.fetchone()

        if user:
            stored_hashed_password = user['password']
            password_with_salt = (password + SECRET_SALT).encode('utf-8')

            if bcrypt.checkpw(password_with_salt, stored_hashed_password.encode('utf-8')):
                token = jwt.encode({
                    'user_id': user['id'],
                    'user_email': user['email'],
                    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
                }, SECRET_KEY, algorithm='HS256')

                logger.info(f"User {user['email']} logged in successfully.")
                return jsonify({
                    "message": "Login successful",
                    "user": {
                        "id": user['id'],
                        "fname": user['fname'],
                        "lname": user['lname'],
                        "email": user['email']
                    },
                    "token": token
                })
        
        logger.warning(f"Unauthorized login attempt for email: {email}.")
        return jsonify({
            "message": "Unauthorized"
        }), 401
    except TypeError as e:
        logger.error(f"TypeError during login: {e}")
        return jsonify({
            'message': str(e)
        }), 500
    except Exception as e:
        logger.error(f"Exception during login: {e}")
        return jsonify({
            'message': str(e)
        }), 500

@app.route('/register', methods=['POST'])
def register():
    con = None
    try:
        request_data = request.json
        fname = request_data['fname']
        lname = request_data['lname']
        email = request_data['email']
        password = request_data['password']

        con, cur = db_con()

        query = "SELECT 1 FROM users WHERE email=%s AND deleted_at IS NULL"
        cur.execute(query, (email,))
        if cur.fetchone():
            logger.warning(f"Registration attempt failed: Email {email} already exists.")
            return jsonify({
                "message": "Email already exists"
            }), 400

        password_with_salt = (password + SECRET_SALT).encode('utf-8')
        hashed_password = bcrypt.hashpw(password_with_salt, bcrypt.gensalt())
        logger.info(f"User {email} registered successfully.")

        query = "INSERT INTO users (fname, lname, email, password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (fname, lname, email, hashed_password.decode('utf-8'), datetime.datetime.now(), datetime.datetime.now()))
        con.commit()

        return jsonify({
            "message": "User registered successfully"
        }), 200
    except Exception as e:
        logger.error(f"Exception during registration: {e}")
        return jsonify({
            'message': str(e)
        }), 500
    finally:
        if con:
            con.close()

@app.route("/getProducts", methods=['POST'])
def get_products():
    try:
        con, cur = db_con()
        cur.execute("SELECT id, product_name, price, image_url FROM product")
        data = cur.fetchall()
        for item in data:
            item['image_url'] = f'/images/{item["image_url"]}'
        logger.info("Products fetched successfully.")
        return jsonify({
            'products': data
        })
    except TypeError as e:
        logger.error(f"TypeError during fetching products: {e}")
        return jsonify({
            'message': str(e)
        }), 500
    except Exception as e:
        logger.error(f"Exception during fetching products: {e}")
        return jsonify({
            'message': str(e)
        }), 500
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
