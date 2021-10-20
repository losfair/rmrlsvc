from flask import Flask, jsonify, Response
import os
import rmrl

app = Flask(__name__)

def list_docs():
    suffix = ".metadata"
    docs = map(lambda x: x[:-len(suffix)], filter(lambda x: x.endswith(suffix), os.listdir("./data")))
    docs = list(docs)
    docs.sort()
    return docs

@app.route("/list")
def on_list():
    docs = list_docs()
    return jsonify(docs)

@app.route("/render/<key>")
def on_render(key):
    docs = list_docs()
    if not key in docs:
        return Response("not found\n", status=404)
    return Response(rmrl.render("./data/{}.zip".format(key)), mimetype="application/pdf")
