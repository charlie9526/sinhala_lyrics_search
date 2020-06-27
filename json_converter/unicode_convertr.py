import json
in_filename = 'lyrics.json'
out_file_name = 'sin_lyrics.json'

with open('./'+in_filename) as fp:
    data = json.load(fp)

with open('./'+out_file_name, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)


