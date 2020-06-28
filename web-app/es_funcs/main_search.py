
def search_main(query,es_object,index):
    result = es_object.search(index=index, body=query)
    return result