There are four main steps in the project <br>
    1. Scraping - Scrapy <br>
    2. Json converting - Python <br>
    3. Indexing - Elasticsearch and Kibana <br> 
    4. Searching - Flask <br>

Key Requirements <br>
    1. Elastic search <br>
    2. Kibana <br>
    3. Python v3 <br>
    4. Scrapy - python <br> 
    5. Flask - python <br>
    6. Elasticsearch client - python <br>
    7. Singling - python <br>
    8. Mtranslate - python <br>

1) Scraping
    The scraper is the directory of the scraping of the project. Song lyrics are scraped from "https://sinhalasongbook.com". Default 10 pages are scraped and the range can be changed by MIN_RANGE and MAX_RANGE variables of the  "scraper\sinhala_songs_lyrics_scraper\sinhala_songs_lyrics_scraper\spiders\sinhala_songs_lyrics_spider.py".
    run following command from "scraper\sinhala_songs_lyrics_scraper" 
    
    scrapy crawl sinhala_songs_lyrics_spider  -o lyrics.json
    
    The output of the scrper is the "lyrics.json" file of the "scraper\sinhala_songs_lyrics_scraper". Default the lyrics.json is consisted of 1005 songs.

2) JSON converter
    Scraped result is with unicode and it is not capable of using for the BULK API of the Elasticsearch. Therefore according the reqired format of the BULK API the lyrics document file is genrated by running "bulk_unicode_converter.py" of the json_converter directory.

3) Indexing
    The most important part of the project. The index creating mapping and settings are in the "settings.json" file in the web-app directory. Use kibana to create index by copying and pasting the command of the "web-app/settings.json". You can simply add all song documents by running "create_index.bat" batch file of es_batch directory or run the folowing curl command within the json_converter directory.

    curl -H "Content-Type: application/json" -XPOST "localhost:9200/test_lyrics/_bulk?pretty&refresh" --data-binary "@bulk_sin_lyrics.json"

4) Searching
    Before run the flask app the singling library should be instantated in the computer. For that download the library fot the followin URL and add the path of the root directory of the library to the PYTHONPATH as mentioned in the repo readme. For run the library there are few dependencies ahould be installed ; "emoji","nltb" python libraries.
    
    https://github.com/ysenarath/sinling

    Now run the "web-app/app.py".

    Search and enjoy Sinhala lyrics from "http://localhost:5000/".
