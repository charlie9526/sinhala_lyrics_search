# Sinhala Lyrics Search

## Design
![Image of Yaktocat](https://github.com/charlie9526/sinhala_lyrics_search/blob/master/images/IR_ARCHITECTURE.jpg)

## Folder structure 

    1. corpus - scraped sinhala lyrics ( 1005 sinhala song lyrics with 9 metadata )
    2. es_batch - Important batch file to input documents from BULK API (create_index.bat)
    3. json_converter - Convert the JSON file in to the specified format of the BULK API
    3. mapping - Mappings and settings of the index
    4. scraper - Scrapy application for song scraping 
    5. web-app - Flask application for query processing and simple UI


## Four main steps in the project
    1. Scraping - Scrapy 
    2. Json converting - Python
    3. Indexing - Elasticsearch and Kibana  
    4. Searching - Flask 

## Major Requirements 
    1. Elastic search 
    2. Kibana 
    3. Python v3 
    4. Scrapy - python  
    5. Flask - python 
    6. Elasticsearch client - python 
    7. Singling - python 
    8. Mtranslate - python 

# Steps
1) Scraping
    The scraper is the directory of the scraping of the project. Song lyrics are scraped from "https://sinhalasongbook.com". Default 10 pages are scraped and the range can           be changed by MIN_RANGE and MAX_RANGE variables of the  "scraper\sinhala_songs_lyrics_scraper\sinhala_songs_lyrics_scraper\spiders\sinhala_songs_lyrics_spider.py". 
    Run following command from "scraper\sinhala_songs_lyrics_scraper" 
        
```
scrapy crawl sinhala_songs_lyrics_spider  -o lyrics.json
```

   The output of the scrper is the "lyrics.json" file of the "scraper\sinhala_songs_lyrics_scraper". Default the lyrics.json is consisted of 1005 songs. The same unicode            converted output of 1005 songs is at corpus directory of the repo. 

2) JSON converter
    Scraped result is with unicode and it is not capable of using for the BULK API of the Elasticsearch. Therefore according to the reqired format of the BULK API the lyrics         document file is genrated by running "bulk_unicode_converter.py" of the json_converter directory.

3) Indexing
    The most important part of the project. The index creating mapping and settings are in the "settings.json" file in the mapping directory. Use kibana to create index by           copying and pasting the command of the "mapping/settings.json". You can simply add all song documents by running "bulk_es.bat" batch file of es_batch directory or           run the folowing curl command within the json_converter directory. The index name is "test_lyrics"

```
curl -H "Content-Type: application/json" -XPOST "localhost:9200/test_lyrics/_bulk?pretty&refresh" --data-binary "@bulk_sin_lyrics.json"
```

4) Searching
    Before run the flask app the "singling" library should be installed in the computer. For that, download the library from the followin URL and add the path of the root           directory of the library to the PYTHONPATH as mentioned in the library's repo readme. For run the library there are few dependencies ahould be installed ; "emoji","nltb"         python libraries.

    https://github.com/ysenarath/sinling

    Now run the "web-app/app.py".

    Search and enjoy Sinhala lyrics from "http://localhost:5000/".
# Important
If your elastic search port is not 9200 and host is not the localhost ,you should change following steps:
3 rd step  
    change "bulk_es.bat" file's "ES_HOST_POST" variable or change curl command's "localhost:9200" 
4th step 
    "app.py" file's "ES_HOST", "ES_PORT" variables.
    
Default is "localhost:9200"

# Examples
## 1. අමරදේව ගැයූ ක්ලැසික් සුපිරි 10
![Image of Yaktocat](https://github.com/charlie9526/sinhala_lyrics_search/blob/master/images/sample%202.jpg)

## 2. දුලීකා සිනමා ගී
![Image of Yaktocat](https://github.com/charlie9526/sinhala_lyrics_search/blob/master/images/sample%203.jpg)

## 3. සනත් නන්දසිරිගේ දුලීකා සිනමා ගී
![Image of Yaktocat](https://github.com/charlie9526/sinhala_lyrics_search/blob/master/images/sample%204.jpg)

## 4. Doc count and Views relationship can be observed by aggregations
    
    "aggregations": {
    "name": {
      "buckets": [
        {
          "doc_count": 12,         ==========================> Document amount of the search query's result which views are exists between 0-1000
          "from": 0.0, 
          "key": "0.0-1000.0", 
          "to": 1000.0
        }, 
        {
          "doc_count": 24,         ==========================> Document amount of the search query's result which views are exists between 1000-2000
          "from": 1000.0, 
          "key": "1000.0-2000.0", 
          "to": 2000.0
        }, 
        {
          "doc_count": 10,         ==========================> Document amount of the search query's result which views are exists between 2000-3000 
          "from": 2000.0, 
          "key": "2000.0-3000.0", 
          "to": 3000.0
        }, 
        {
          "doc_count": 8,         ==========================> Document amount of the search query's result which views are exists between 3000-4000
          "from": 3000.0, 
          "key": "3000.0-4000.0", 
          "to": 4000.0
        }, 
        {
          "doc_count": 4,         ==========================> Document amount of the search query's result which views are exists between 4000-5000
          "from": 4000.0, 
          "key": "4000.0-5000.0", 
          "to": 5000.0
        }, 
        {
          "doc_count": 0, 
          "from": 5000.0, 
          "key": "5000.0-6000.0", 
          "to": 6000.0
        }, 
        {
          "doc_count": 0, 
          "from": 6000.0, 
          "key": "6000.0-7000.0", 
          "to": 7000.0
        }, 
        {
          "doc_count": 0, 
          "from": 7000.0, 
          "key": "7000.0-8000.0", 
          "to": 8000.0
        }, 
        {
          "doc_count": 0, 
          "from": 8000.0, 
          "key": "8000.0-9000.0", 
          "to": 9000.0
        }, 
        {
          "doc_count": 0, 
          "from": 9000.0, 
          "key": "9000.0-10000.0", 
          "to": 10000.0
        }
      ]
    }
   
