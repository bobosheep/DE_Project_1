import re
import json
import pickle

from flask import Flask, jsonify, request
app = Flask(__name__)
sentences = {}

@app.route('/')
def home():
    return 'Hello world!'

@app.route('/search', methods = ['GET'])
def search():
    term = request.args.get('term')
    if term == None:
        return 'Nothing'
    print(term)
    return_list = {}
    for s in sentences.items():
        if s[0].find(term) >= 0:
            return_list[s[0]] = s[1]
    print(return_list)
    return jsonify(return_list)

if __name__ == '__main__':
    with open('../news_data/sentences.bdata', 'rb') as fp:
        sentence = pickle.load(fp)

    app.run()

