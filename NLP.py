import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from  nltk.tokenize import word_tokenize as wt
# from  nltk.tokenize import sent_tokenize as st
from  nltk.corpus  import stopwords as sw
file = open('sentence.txt')
# sentence = "Ali is a boy. He is 7 years old"
# wordTokens = wt(sentence)
# sentenceTokens = st(sentence)
# print(wordTokens)
# print(sentenceTokens)
# print(sw.fileids())
englishCollection = set(sw.words('english'))
# words = ['ali', 'is','a', 'boy']
words = wt(file.read())
result = [words for words in words if words not in englishCollection]
print(result)