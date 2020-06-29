from elasticsearch import Elasticsearch 

from es_funcs.es_init import connect_elasticsearch
from es_funcs.main_search import search_main
from es_funcs.final_query import get_final_query

from word_process.splitter import process_word
from word_process.classifiere import classify_query

from flask import Flask, redirect, url_for, request, render_template

ES_HOST = 'localhost'
ES_PORT = 9200
INDEX = "test_lyrics"
DEFAULT_RESULTS = 15

app = Flask(__name__)
es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
connect_elasticsearch('localhost',9200,es)

@app.route('/')
def view_app():
    return render_template('index.html')

@app.route('/search',methods = ['POST'])
def search():
    if request.method == 'POST':
        search_string = request.form['search_string']
        word_list = process_word(search_string)
        classifiere_result,processed_raw_query = classify_query(word_list,DEFAULT_RESULTS,search_string)
        final_query = get_final_query(classifiere_result,processed_raw_query)
        result = search_main(final_query,es,INDEX)
        return result

if __name__ == '__main__':
   app.run(debug = True)