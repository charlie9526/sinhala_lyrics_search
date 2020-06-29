
movie_list = ['චිත්‍රපට','සිනමා']
beat_list = ['4/4','3/4','2/4','6/8','2/2','1/2']
music_list = [ 'සංගීතමය', 'සංගීතවත්','අධ්‍යක්ෂණය', 'සංගීත']
key_list = ['G major','F major','E minor','C major','A minor','major','minor']
genre_list = ['පැරණි', 'පොප්ස්','පොප්','පරණ','ක්ලැසික්','ක්ලැසි','ඉල්ලීම','චිත්‍රපට','නව']
artist_list = ['කීව', 'කී', 'ගායනා කරන', 'ගයන', 'ගායනා','‌ගේ', 'හඩින්', 'කියනා', 'කිව්ව', 'කිව්', 'කිව', 'ගායනය', 'ගායනා කළා', 'ගායනා කල', 'ගැයූ']
creater_list = ['ලියා', 'ලියූ', 'ලිව්ව', 'ලිව්', 'රචනා',  'ලියා ඇති', 'රචිත', 'ලියන ලද','ලියන', 'හදපු', 'පද', 'රචනය', 'හැදූ', 'හැදුව', 'ලියන', 'ලියන්න','ලීව', 'ලියපු', 'ලියා ඇත', 'ලිඛිත']
super_list = ['සුපිරි', 'නියම', 'පට්ට','ඉහළම', 'හොඳ', 'හොඳම', 'එලකිරි', 'එළකිරි', 'සුප්පර්', 'සුප්රකට', 'ඉහල',  'වැඩිපුර', 'වැඩිපුරම', 'සුප්‍රකට', 'ජනප්රිය', 'ජනප්රියම', 'ජනප්‍රිය', 'ජනප්‍රියම', 'ප්‍රකට', 'ප්‍රසිද්ධ']



def classify_query(token_list,default_amount,raw_string):
    nothing_special = True
    result = get_base_result()
    result['total'] = {
        'total':default_amount,
        'rating':False
    }
    ### First lets check user searchs for songs for a aspecific beat
    result,nothing_special = check_beat(raw_string,result,nothing_special)

    result,nothing_special = classify_list(token_list,result,nothing_special)

    result = mark_nothing_special(result,nothing_special)

    result = check_rating(result,raw_string)

    if (result['beat']==True):
        result['total']['total'] = default_amount
        return result

    result_amount = 0
    for token in token_list:
        if (token.isnumeric()):
            if (int(token)<default_amount):
                result['total']['total'] = int(token)
            else:
                result['total']['total'] = default_amount
        break
    
    return result
    

def classify_list(token_list,result_obj,nothing_special):
    result = result_obj
    for token in token_list:
        if token in key_list:
            nothing_special = False
            result['key'] = True
        elif token in movie_list:
            nothing_special = False
            result['movie'] = True
            result['genre'] = True
        elif token in genre_list:
            nothing_special = False
            result['genre'] = True
        elif token in music_list:
            nothing_special = False
            result['music'] = True
        elif token in artist_list:
            nothing_special = False
            result['artists'] = True
        elif token in creater_list:
            nothing_special = False
            result['lyricsCreater'] = True
    return result,nothing_special

def check_beat(raw_string,result,nothing_special):
    for beat in beat_list:
        if beat in raw_string:
            nothing_special = False
            result['beat'] = True
            break
    return result,nothing_special

def  mark_nothing_special(result,nothing_special):
    if (nothing_special):
        result['songName'] = True
        result['lyrics'] = True
    return result

def check_rating(result,raw_string):
    for rating_word in super_list:
        if rating_word in raw_string:
            result['total']['rating'] = True
            break
    return result

def get_base_result():
    RESULT = {
        'songName':False,
        'lyrics':False,
        'movie':False,
        'artists':False,
        'genre':False,
        'beat':False,
        'key':False,
        'music':False,
        'lyricsCreater':False,
        'total':0
    }
    return RESULT