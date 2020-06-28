
movie_list = ['චිත්‍රපට','සිනමා']
beat_list = ['4/4','3/4','2/4','6/8','2/2','1/2']
music_list = [ 'සංගීතමය', 'සංගීතවත්','අධ්‍යක්ෂණය', 'සංගීත']
key_list = ['G major','F major','E minor','C major','A minor','major','minor']
genre_list = ['පැරණි', 'පොප්ස්','පොප්','පරණ','ක්ලැසික්','ක්ලැසි','ඉල්ලීම','චිත්‍රපට','නව']
artist_list = ['කීව', 'කී', 'ගායනා කරන', 'ගයන', 'ගායනා','‌ගේ', 'හඩින්', 'කියනා', 'කිව්ව', 'කිව්', 'කිව', 'ගායනය', 'ගායනා කළා', 'ගායනා කල', 'ගැයූ']
creater_list = ['ලියා', 'ලියූ', 'ලිව්ව', 'ලිව්', 'රචනා',  'ලියා ඇති', 'රචිත', 'ලියන ලද','ලියන', 'හදපු', 'පද', 'රචනය', 'හැදූ', 'හැදුව', 'ලියන', 'ලියන්න','ලීව', 'ලියපු', 'ලියා ඇත', 'ලිඛිත']

def classify_query(token_list,default_amount,raw_string):

    result = {
        'movie':False,
        'artists':False,
        'genre':False,
        'beat':False,
        'key':False,
        'music':False,
        'lyricsCreater':False,
        'total':default_amount
    }

    ### First lets check user searchs for songs for a aspecific beat
    for beat in beat_list:
        if beat in raw_string:
            result['beat'] = True
            break

    for token in token_list:
        if token in key_list:
            result['key'] = True
        elif token in genre_list:
            result['genre'] = True
        elif token in music_list:
            result['music'] = True
        elif token in artist_list:
            result['artists'] = True
        elif token in creater_list:
            result['lyricsCreater'] = True
        elif token in movie_list:
            result['movie'] = True


    if (result['beat']==True):
        result['total'] = default_amount
        return result

    result_amount = 0
    for token in token_list:
        if (token.isnumeric()):
            if (int(token)<default_amount):
                result['total'] = int(token)
            else:
                result['total'] = default_amount
        break
    
    return result
    
        