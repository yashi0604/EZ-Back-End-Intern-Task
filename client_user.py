from flask import Blueprint, request, jsonify
from database.db import get_db_connection

import uuid

client_user_routes = Blueprint('client_user_routes', __name__)

@client_user_routes.route('/client/signup', methods=['POST'])
def client_signup():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO client_users (email) VALUES (?)', (email,))
    conn.commit()
    conn.close()

    # Dummy encrypted link
    encrypted = str(uuid.uuid4())
    return jsonify({
        "download-link": f"/client/download-file/{encrypted}",
        "message": "Signup successful"
    }), 201
