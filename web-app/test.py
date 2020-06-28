from sinling import word_splitter,SinhalaTokenizer

jk = SinhalaTokenizer()
sentence = "2/4"
l = word_splitter.split(sentence)
# l = jk.tokenize(sentence)
print(l['affix'])