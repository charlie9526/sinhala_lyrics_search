
def search_main(query,es_object,index):
    query_body = {
        "query":{
            "match":{
                "lyrics":query
            }
        },
        "size":20
    }
    return es_object.search(index=index, body=query_body)