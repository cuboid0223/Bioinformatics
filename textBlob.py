#https://textblob.readthedocs.io/en/dev/quickstart.html#quickstart

from textblob.wordnet import VERB
from textblob import Word
from textblob import TextBlob
text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.

Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text) # blob >> 斑點

# Part-of-speech Tagging¶
print("文章中單字的詞性代號: ", blob.tags)  # 印出所有單字的 tag ，詞性標記
# [('The', 'DT'), ('titular', 'JJ'),
#  ('threat', 'NN'), ('of', 'IN'), ...]


# Noun Phrase Extraction
print("文章中的名詞單字: ", blob.noun_phrases)   # 印出所有 名詞單字
# WordList(['titular threat', 'blob', 'ultimate movie monster','amoeba-like mass', ...])


# Sentiment Analysis¶(情緒分析)
for sentence in blob.sentences:  
    # 句子的極性，範圍 -1 ~ 1
	print("極性程度: ", sentence.sentiment.polarity)

for sentence in blob.sentences:
	# 句子的客觀(0)、主觀(1)程度，範圍 0~1
	print("主觀、客觀程度: ", sentence.sentiment.subjectivity)
	

# Tokenization (將字串中的單字或句子，分出來)
zen = TextBlob("Beautiful is better than ugly. "
              "Explicit is better than implicit. "
               "Simple is better than complex.")
print("單字: ", zen.words)
print("句子: ", zen.sentences)


# Words Inflection(單複數變化) and Lemmatization(詞形化)
sentence = TextBlob('Use 4 spaces per indentation level.')
print(sentence.words)
#WordList(['Use', '4', 'spaces', 'per', 'indentation', 'level'])
sentence.words[2].singularize()
#'space' 單數
sentence.words[-1].pluralize()
#'levels' 複數

# from textblob import Word
w = Word("octopi")
w.lemmatize()
#'octopus'
w = Word("went") #過去式轉現在式
w.lemmatize("v")  # Pass in WordNet part of speech (verb)
# 'go'


# WordNet Integration¶ 整合 WordNet(一種工程師用英文字典)
#  from textblob.wordnet import VERB
word = Word("octopus")
word.synsets  # 找出 octopus 的同義詞(synset)
Word("hack").get_synsets(pos=VERB)  # 找出 hack 的同義動詞(synset)， hack , chop 都有劈的意思
#[Synset('chop.v.05'), Synset('hack.v.02'), Synset('hack.v.03'), Synset('hack.v.04'), Synset('hack.v.05'), Synset('hack.v.06'), Synset('hack.v.07'), Synset('hack.v.08')]
Word("octopus").definitions # 找出 octopus 的定義
#['tentacles of octopus prepared as food', 'bottom-living cephalopod having a soft oval body with eight long tentacles']
#from textblob.wordnet import Synset 可自行定義單字
octopus = Synset('octopus.n.02')
shrimp = Synset('shrimp.n.03')
octopus.path_similarity(shrimp)
#0.1111111111111111 的相似度


#Spelling Correction¶ 單字拼對？
b = TextBlob("I havv goood speling!")
print(b.correct())
#I have good spelling!
w = Word('falibility')
w.spellcheck()
#[('fallibility', 1.0)] <<< 1.0 指的是 自信程度


# Get Word and Noun Phrase Frequencies¶ 單字使用頻率
monty = TextBlob("We are no longer the Knights who say Ni. "
                 "We are now the Knights who say Ekki ekki ekki PTANG.")
monty.word_counts['ekki']
# 3
monty.words.count('ekki') # 第二種用法
# 3
monty.words.count('ekki', case_sensitive=True) # 是否在意大寫？ 預設為 false
# 2
