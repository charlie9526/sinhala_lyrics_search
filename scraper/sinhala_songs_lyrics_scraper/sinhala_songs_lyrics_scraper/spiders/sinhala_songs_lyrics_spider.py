import re
import pickle
import scrapy
from mtranslate import translate
from sinhala_songs_lyrics_scraper.items import SinhalaSongsLyricsScraperItem

MIN_RANGE = 1
MAX_RANGE = 10

class SinhlaSongsLyricsSpider(scrapy.Spider):
    name = "sinhala_songs_lyrics_spider"

    start_urls = ["https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page=" + str(x) for x in range(MIN_RANGE,MAX_RANGE)]    

    def parse(self, response):
        global translation_helper
        try:
            translation_helper = pickle.load(open('../'+file_name, 'rb'))
        except (OSError, IOError):
            pickle.dump(translation_helper, open('../'+file_name, 'wb'))

        for href in response.xpath("//main[contains(@id, 'genesis-content')]//div[contains(@class, 'entry-content')]//div[contains(@class, 'pt-cv-wrapper')]//h4[contains(@class, 'pt-cv-title')]/a/@href"):
            href =  href.extract()
            yield scrapy.Request(href, callback=self.parse_lyrics_from_href)

    def parse_lyrics_from_href(self,response):
        
        item = SinhalaSongsLyricsScraperItem()
        
        item['url'] = response.url
        
        item['songName'] = re.split('\||–|-',response.xpath("//div[contains(@class, 'site-inner')]//header[contains(@class, 'entry-header')]/h1/text()").extract()[0])[1].strip()
        
        item['songNameSinglish'] = re.split('\||–|-',response.xpath("//div[contains(@class, 'site-inner')]//header[contains(@class, 'entry-header')]/h1/text()").extract()[0])[0].strip()

        artists = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-3-6')]//span[contains(@class, 'entry-categories')]/a/text()").extract()
        if len(artists)==0:
            item['artists'] = []
        else:
            item['artists'] = english_array_to_sinhala(artists)
            # item['artists'] = artists
        
        genre = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-3-6')]//span[contains(@class, 'entry-tags')]/a/text()").extract()
        if len(genre) == 0:
            item['genre'] = []
        else:
            item['genre'] = english_array_to_sinhala(genre)
            # item['genre'] = genre          
        
        lyricsCreater = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-2-6')]//span[contains(@class, 'lyrics')]/a/text()").extract()
        if len(lyricsCreater) == 0:
            item['lyricsCreater'] = []
        else:
            item['lyricsCreater'] = english_array_to_sinhala(lyricsCreater)
            # item['lyricsCreater'] = lyricsCreater

        music = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-2-6')]//span[contains(@class, 'music')]/a/text()").extract()
        if len(music) == 0:
            item['music'] = []
        else:
            item['music'] = english_array_to_sinhala(music)
            # item['music'] = music
        
        movie = response.xpath("//div[contains(@class, 'entry-content')]//div[contains(@class, 'su-column su-column-size-2-6')]//span[contains(@class, 'movies')]/a/text()").extract()
        if len(movie) == 0:
            item['movie'] = []
        else:
            item['movie'] = english_array_to_sinhala(movie)
        
        key_n_beat = re.split('\|',  response.xpath("//div[contains(@class, 'entry-content')]/h3/text()").extract()[0])
        try:
            item['key'] = re.split(':', key_n_beat[0])[1].strip()
        except IndexError:
            item['key'] = key_n_beat[0].strip()
            item['beat'] = ''
        try:
            item['beat'] = re.split(':', key_n_beat[1])[1].strip()
        except:
            item['beat'] = ''
        
        temp_content = response.xpath("//div[contains(@class, 'entry-content')]//pre/text()").extract()
        tempory_lyric = ''
        new_line_1 = True
        new_line_2 = False
        for line in temp_content:
            line_content = (re.sub("[\da-zA-Z\-—\[\]\t\@\_\!\#\+\$\%\^\&\*\(\)\<\>\?\|\}\{\~\:\∆\/]", "", line)).split('\n')
            for line1 in line_content:
                # temp_lyric += line1.strip()
                if line1 == '' or line1.isspace():
                    if not new_line_2:
                        new_line_2 = True
                        tempory_lyric += '\n'
                else:
                    new_line_1 = False
                    new_line_2 = False
                    tempory_lyric += line1.strip()
            if not new_line_1:
                new_line_1 = True
                tempory_lyric += '\n'
        item['lyrics'] = tempory_lyric

        try:
            item['views'] = int(re.sub('[^0-9,]', "", response.xpath("//div[contains(@class, 'entry-content')]/div[contains(@class, 'tptn_counter')]/text()").extract()[0]).replace(',', ''))
        except:
            item['views'] = None

        global translation_helper
        pickle.dump(translation_helper, open('../'+file_name, 'wb'))

        yield item


exception_words = {
    'Wayo': "වායෝ",
    'Daddy': "ඩැඩී"
}      
file_name = 'translation_helper.pickle'
translation_helper = {}

def english_array_to_sinhala(stringList):
    temp = []
    for string in stringList:
        temp.append(english_word_to_sinhala(string))
    return temp

def english_word_to_sinhala(word):
    if word in exception_words:
        return exception_words[word]
    elif word in translation_helper:
        return translation_helper[word]
    elif word.lower() == "unknown":
        return ''
    else:
        translation = translate(word, 'si', 'en')
        translation_helper[word] = translation
        return translation