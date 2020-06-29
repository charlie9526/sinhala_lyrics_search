
def get_final_query(classifiere_result,processed_raw_query):
    field_list = []

    for key in classifiere_result:
        if (key=='total'):
            continue
        if (classifiere_result[key]):
            field_list.append(key+'^7')
        # else:
        #     field_list.append(key)
    processed_raw_query = processed_raw_query.strip()
    query = {
        'query':{
            'multi_match':{
                'type':  'most_fields',
                'query':processed_raw_query,
                'fields':field_list
            }
        },
        'size':classifiere_result['total']['total'],
        'aggs':get_agg_json()
    }
    if (processed_raw_query.strip()==""):
        query = {
            "query": {
                "match_all": {}
            }
        }
    if (classifiere_result['total']['rating']):
        query['sort'] = [{'views':'desc'}]
    print(query)
    return query

def get_agg_json():
    
    k = {
    "name": {
      "range": {
        "field": "views",
        "ranges":[
          {
            "from": 0,
            "to": 1000
          },
          {
            "from": 1000,
            "to": 2000
          },
          {
            "from": 2000,
            "to": 3000
          },
          {
            "from": 3000,
            "to": 4000
          },
          {
            "from": 4000,
            "to": 5000
          },
          {
            "from": 5000,
            "to": 6000
          },
          {
            "from": 6000,
            "to": 7000
          },
            {
            "from": 7000,
            "to": 8000
          },
            {
            "from": 8000,
            "to": 9000
          },
            {
            "from": 9000,
            "to": 10000
          }
          ]
      }
    }}
  
    return k
