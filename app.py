from flask import Flask
from routes.ops_user import ops_user_routes
from routes.client_user import client_user_routes
from database.db import init_db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'storage'
app.secret_key = 'your_secret_key_here'

# Register routes
app.register_blueprint(ops_user_routes)
app.register_blueprint(client_user_routes)

# Initialize database
init_db()

if __name__ == '__main__':
    app.run(debug=True)
