from flask import Flask, jsonify, Response
import os
import rmrl
import json

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
  m = {}
  for doc in docs:
    try:
      with open("./data/{}.metadata".format(doc), "r") as f:
        m[doc] = json.loads(f.read())
    except:
      pass
  return jsonify(m)

@app.route("/render/<key>")
def on_render(key):
  docs = list_docs()
  if not key in docs:
    return Response("not found\n", status=404)
  return Response(rmrl.render("./data/{}.zip".format(key)), mimetype="application/pdf")
