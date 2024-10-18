# app.py
from flask import Flask
from extensions import db, migrate, cors

# Initialize the app and configure it
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cocktails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up the database and migrations
db.init_app(app)
migrate.init_app(app, db)
cors.init_app(app)

# Import the routes after the app and db initialization
from routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
