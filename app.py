from flask import Flask, request, jsonify
import json
from gnewsclient import gnewsclient 

app = Flask(__name__)
@app.route('/searchPOST/', methods=['POST'])
def post_data():
    topic = request.args.get('topic')
    language =  request.args.get('language')
    location =  request.args.get('location')
    max_results = request.args.get('max_results')
    client = gnewsclient.NewsClient(language=language, location=location, topic=topic, use_opengraph=True, max_results= max_results)
    data = client.get_news()
    print(data)
    return jsonify(
        {"results" : data}
    )

@app.route('/searchGET/', methods=['GET'])
def get_data():
    topic = request.args.get('topic','str')
    language =  request.args.get('language','str')
    location =  request.args.get('location','str')
    max_results = request.args.get('max_results','str')
    max_results = int(max_results)
    client = gnewsclient.NewsClient(language=language, location=location, topic=topic, use_opengraph=True, max_results= max_results)
    data = client.get_news()
    print(data)
    return jsonify(
        {"results" : data}
    )

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    app.run(threaded=True, port=5000)