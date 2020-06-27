from elasticsearch import Elasticsearch 
from es_funcs.start_es import connect_elasticsearch
from es_funcs.search_main import search_main
from flask import Flask, redirect, url_for, request, render_template

ES_HOST = 'localhost'
ES_PORT = 9200
INDEX = "test_lyrics"

app = Flask(__name__)
es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
connect_elasticsearch('localhost',9200,es)

@app.route('/')
def view_app():
    return render_template('index.html')

@app.route('/search',methods = ['POST'])
def search():
    if request.method == 'POST':
      query = request.form['query']
      result = search_main(query,es,INDEX)
      return result

if __name__ == '__main__':
   app.run(debug = True)