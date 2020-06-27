from elasticsearch import Elasticsearch 
from start_es import connect_elasticsearch

es = connect_elasticsearch('localhost',9200)
create_index(es,'ww')
# print(put_settings(es,'ww'))