from elasticsearch import Elasticsearch 

def connect_elasticsearch(host,port):
    _es = None
    _es = Elasticsearch([{'host': host, 'port': port}])
    if _es.ping():
        print('Python is connected successfully to %s : %d !'%(host,port))
    else:
        print('Connection failed!')
    return _es
