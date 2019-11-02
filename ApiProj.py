import numpy as np
import re
import flask
import json
from flask import Flask, request
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)

@app.route('/home')
def test_api():
    return 'my Flash API works!!!'

@app.route('/topwords', methods=['POST'])
def top_words():

    data = json.loads(request.data.decode())
    text, num_of_words = data["text"], data["num"]
    tokens = re.split(' ', text)
    token_len = [len(word) for word in tokens]
    ordered_token_len = np.argsort(token_len)
    words = []
    for idx in ordered_token_len[-num_of_words:]:
        words.append(tokens[idx])
    return str(words)

@app.route('/lastwords', methods=['POST'])
def last_words():

    data = json.loads(request.data.decode())
    text, num_of_words = data["text"], data["num"]
    tokens = re.split(' ', text)
    token_len = [len(word) for word in tokens]
    ordered_token_len = np.argsort(token_len)
    words = []
    for idx in ordered_token_len[:num_of_words]:
        words.append(tokens[idx])
    return str(words)

@app.route('/removestopwords', methods=['POST'])
def remove_stop_words():

    data = json.loads(request.data.decode())
    text = data["text"]
    tokens = re.split(' ', text)
    stop_words = stopwords.words('english')
    tokens = [t for t in tokens if t not in stop_words]  # remove stopwords and punctuation
    return str(tokens)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)