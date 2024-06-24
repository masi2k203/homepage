import sys
from datetime import datetime

from flask import Blueprint, render_template

bp = Blueprint("home", __name__, static_folder="./webapp/templates/home/img")


@bp.route("/")
def home():
    place_holder = {
        "title": "工事中",
        "now_date": str(datetime.now()),
        "working": "Backend Info: " + str(sys.version_info),
    }
    return render_template("home/index.html", **place_holder)
