from datetime import datetime
from flask import Blueprint, render_template

bp = Blueprint("miniblog", __name__)


class PostData:
    def get_data(self) -> list[dict]:
        return [
            {
                "post_header": "雑記",
                "post_title": "おためしポスト2",
                "post_body": "本文はhtmlなり、markdownなりしたいところ",
                "post_datetime": datetime.now().strftime("%Y年%m月%d日 %H:%M:%S") 
            },
            {
                "post_header": "雑記",
                "post_title": "おためしポスト1",
                "post_body": "べた書きでJinja2のレンダリングが効くかを確認してます。日付は datetime.now() で取得中。",
                "post_datetime": datetime.now().strftime("%Y年%m月%d日 %H:%M:%S") 
            },
        ]


@bp.route("/miniblog")
def miniblog():
    place_holder = {
        "title": "リンクページ",
        "posts": PostData().get_data()
    }
    return render_template("miniblog/index.html", **place_holder)