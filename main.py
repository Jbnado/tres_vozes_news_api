import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from db import config_db
from user.user_controller import user_blueprint
from topic.topic_controller import topic_blueprint
from news.news_controller import news_blueprint
from liked.liked_controller import liked_blueprint

load_dotenv()

app = Flask(__name__)
CORS(app)
config_db(app)

app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(topic_blueprint, url_prefix="/topic")
app.register_blueprint(news_blueprint, url_prefix="/news")
app.register_blueprint(liked_blueprint, url_prefix="/liked")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
