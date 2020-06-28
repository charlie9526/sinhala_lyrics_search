set ES_HOST=localhost:9200
REM set JSON_FILE = "bulk_sin_lyrics.json"
REM set INDEX_NAME = "test_lyrics"

cd /d E:\projects\7.ES\charlie_sinhala_lyrics\json_converter
REM curl -H "Content-Type: application/json" -XPOST "%ES_HOST%/%INDEX_NAME%/_bulk?pretty&refresh" --data-binary "@%JSON_FILE%"
curl -H "Content-Type: application/json" -XPOST "%ES_HOST%/test_lyrics/_bulk?pretty&refresh" --data-binary "@bulk_sin_lyrics.json"
curl "localhost:9200/_cat/indices?v"

cd /d E:\projects\7.ES\charlie_sinhala_lyrics\es_batch