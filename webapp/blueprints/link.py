from flask import Blueprint, render_template

bp = Blueprint("link", __name__)


@bp.route("/link")
def link():
    place_holder = {"title": "リンクページ"}
    return render_template("link/index.html", **place_holder)
