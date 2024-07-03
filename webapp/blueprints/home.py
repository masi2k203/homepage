import sys
from datetime import datetime

from flask import Blueprint, render_template, request

bp = Blueprint("home", __name__, static_folder="./webapp/templates/home/img")


@bp.route("/")
def home():
    place_holder = {
        "title": "ホーム",
    }
    return render_template("home/index.html", **place_holder)
