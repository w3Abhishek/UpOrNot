import check
from flask import Flask, jsonify
 
app = Flask(__name__)
 

@app.route('/<string:url>')
def hello_world(url):
    return jsonify(check.check_status(url))

if __name__ == '__main__':
    app.run()