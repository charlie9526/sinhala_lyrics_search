set ES_HOST=localhost:9200

cd ..\json_converter
curl -H "Content-Type: application/json" -XPOST "%ES_HOST%/test_lyrics/_bulk?pretty&refresh" --data-binary "@bulk_sin_lyrics.json"
curl "localhost:9200/_cat/indices?v"

cd /d E:\projects\7.ES\charlie_sinhala_lyrics\es_batch