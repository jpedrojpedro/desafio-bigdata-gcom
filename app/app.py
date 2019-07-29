from flask import Flask
app = Flask(__name__)


# TODO: deve ser POST
@app.route("/<path:url>/view", methods=['GET'])
@app.route("/<path:url>/view/", methods=['GET'])
def view(url):
    return "View: {}".format(url)


@app.route("/<path:url>/similar", methods=['GET'])
@app.route("/<path:url>/similar/", methods=['GET'])
def similar(url):
    return "Similar: {}".format(url)


# TODO: deve ser DELETE
@app.route("/", methods=['GET'])
def delete():
    return "Delete!"
