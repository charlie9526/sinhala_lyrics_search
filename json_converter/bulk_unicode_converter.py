import json
in_filename = 'lyrics.json'
out_file_name = 'bulk_sin_lyrics.json'

out = open('./'+out_file_name, 'w',encoding='utf-8')

with open('./../scraper/sinhala_songs_lyrics_scraper/'+in_filename,encoding='utf-8') as json_in:
    docs = json.loads(json_in.read())
    for doc in docs:
        out.write('%s\n' % json.dumps({'index': {}}))
        out.write('%s\n' % json.dumps(doc, indent=0,ensure_ascii=False).replace('\n', ''))
