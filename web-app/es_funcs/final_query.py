
def get_final_query(classifiere_result,processed_raw_query):
    field_list = []

    for key in classifiere_result:
        if (key=='total'):
            continue
        if (classifiere_result[key]):
            field_list.append(key+'^3')
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
        'size':classifiere_result['total']['total']
    }
    if (classifiere_result['total']['rating']):
        query['sort'] = [{'views':'desc'}]
    print(query)
    return query
        