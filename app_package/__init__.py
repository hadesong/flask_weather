from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app_package import view