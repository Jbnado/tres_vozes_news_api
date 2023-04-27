from flask import Flask
from flask_cors import CORS
from db import config_db
from user.user_controller import user_blueprint

app = Flask(__name__)
CORS(app)
config_db(app)

app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
