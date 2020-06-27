
def connect_elasticsearch(host,port,es_object):
    _es = es_object
    if _es.ping():
        print('Python is connected successfully to %s : %d !'%(host,port))
    else:
        print('Connection failed!')
    return _es
