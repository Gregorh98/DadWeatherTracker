from http import HTTPMethod

from flask import Blueprint, redirect, url_for, render_template, request

routes = Blueprint("routes", __name__)


@routes.route("/")
def index():
    return redirect(url_for("routes.home"))


@routes.route("/home", methods=[HTTPMethod.GET, HTTPMethod.POST])
def home():
    if request.method == HTTPMethod.POST:
        weather = request.form.get("weather")
        wind = request.form.get("wind")
        temperature = request.form.get("temperature")
        return (f"{weather}, {wind}, {temperature}")

    return render_template("home.html")
