
def get_final_query(classifiere_result,processed_raw_query):
    field_list = []
    for key in classifiere_result:
        if (key=='total'):
            continue
        if (classifiere_result[key]):
            field_list.append(key+'^2')
        else:
            field_list.append(key)
    query = {
        'query':{
            'multi_match':{
                'query':processed_raw_query,
                'fields':field_list
            }
        },
        'size':classifiere_result['total']
    }
    print(query)
    return query
        