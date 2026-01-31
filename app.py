from flask import Flask, request, jsonify
from google.cloud import storage
import json

app = Flask(__name__)
client = storage.Client()

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    bucket_name = data["bucket"]
    filename = data["name"]

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)
    content = blob.download_as_text()

    result = {
        "filename": filename,
        "size": len(content)
    }

    out_bucket = client.bucket("file-pipeline-output-xyz")
    out_blob = out_bucket.blob(filename + ".json")
    out_blob.upload_from_string(json.dumps(result))

    return jsonify(result)
