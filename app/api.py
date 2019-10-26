from flask import Flask, request
from app import module

app = Flask(__name__)


@app.route("/", methods=["GET"])
def calculate_insurance():
    return module.calculate_insurance(request.json)
