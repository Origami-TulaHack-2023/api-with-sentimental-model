import json
from flask import Flask, request
from classifier import get_prediction

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Moe Flask п�~@иложение в кон�~Bейне�~@е Docker.'

@app.route('/predict', methods=['POST'])
def predict():
    feedbacks = json.loads(request.json)
    predictions = get_prediction([feedback["text"] for feedback in feedbacks])

    for i in range(len(feedbacks)):
        feedbacks[i]["label"] = predictions[i]

    return feedbacks

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')