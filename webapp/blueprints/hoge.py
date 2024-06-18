from flask import Blueprint

bp = Blueprint("hoge", __name__, url_prefix="/hoge")


@bp.route("sample")
def sample():
    return """
<h1>ほげ</h1>
"""
