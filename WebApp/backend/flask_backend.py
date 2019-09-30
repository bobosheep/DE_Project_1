import re
import json
import pickle
import time

from flask import Flask, jsonify, request
app = Flask(__name__)
sentences = {}

@app.route('/')
def home():
    return 'Hello world!'

search_term = ''
result_list = []

@app.route('/search', methods = ['GET'])
def search():
    term = request.args.get('term')
    result_page = request.args.get('page', 1)
    result_page = int(result_page)

    global search_term
    global result_list

    if search_term == term :
        return_json = {"page": result_page, "sentences":result_list[(result_page - 1) * 10 : result_page * 10], "search_time": 0.1, "total_results":len(result_list)}
        return jsonify(return_json)

    else :
        search_term = term
        result_list = []


    if term == None:
        return jsonify({"page":0, "senetences":[], "search_time":0, "total_result": 0})

    print(term)
    count = 0


    start = time.clock()
    for s in sentences:
        find_idx = s[0].find(term)
        if find_idx >= 0:
            before = s[0][:find_idx]
            after = s[0][find_idx+len(term):]
            find_term = s[0][find_idx: find_idx+len(term)]
            sen = before + '<mark>' + find_term + '</mark>' + after
            result_list.append({"name":sen, "count":s[1]})
    end = time.clock()
    search_time = end - start


    return_json = {"page": result_page, "sentences":result_list[(result_page - 1) * 10 : result_page * 10], "search_time": search_time, "total_results":len(result_list)}
    

    return jsonify(return_json)

if __name__ == '__main__':
    with open('../../news_data/sentences.bdata', 'rb') as fp:
        sentences = pickle.load(fp)

    app.run(debug=True)

