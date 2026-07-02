from flask import Blueprint, jsonify
from calculator import Calculator

api = Blueprint("api", __name__)

calc = Calculator()


@api.route("/")
def home():
    return jsonify(
        {
            "application": "Flask DevOps API",
            "version": "1.0.0",
            "status": "Running"
        }
    )


@api.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify(
        {
            "operation": "addition",
            "result": calc.add(a, b)
        }
    )


@api.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return jsonify(
        {
            "operation": "subtraction",
            "result": calc.subtract(a, b)
        }
    )


@api.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return jsonify(
        {
            "operation": "multiplication",
            "result": calc.multiply(a, b)
        }
    )


@api.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    return jsonify(
        {
            "operation": "division",
            "result": calc.divide(a, b)
        }
    )