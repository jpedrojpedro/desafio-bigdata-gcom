from app import app
from models import VideoHistory
from flask import request, abort, jsonify


@app.route("/<path:url>/view/", methods=['POST'])
def view(url):
    user = request.form.get('user')
    __video_history_params(url, user)
    vh = VideoHistory(user=user, url=url)
    vh.clean_url()
    vh.save()
    return jsonify(vh.to_dict())


@app.route("/<path:url>/similar/", methods=['GET'])
def similar(url):
    __url_params(url)
    return jsonify(VideoHistory.similar())


@app.route("/", methods=['DELETE'])
def delete():
    return jsonify(VideoHistory.delete_all())


def __video_history_params(url, user):
    if url is None or user is None:
        abort(404)
    if len(url) == 0 or len(user) < 3:
        abort(404)


def __url_params(url):
    if url is None or len(url) == 0:
        abort(404)
