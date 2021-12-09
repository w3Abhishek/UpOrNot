import check
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/<string:url>')
def hello_world(url):
    return jsonify(check.check_status(url))

if __name__ == '__main__':
    app.run()