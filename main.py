from flask import Flask, request, g
import logging as log

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handleGet():
    return

@app.route('/', methods=['POST'])
def handlePost():
    return

if __name__ == '__main__':
    log.info("Starting flask server")
    app.run(port=5000, debug=True)  # Run the Flask app