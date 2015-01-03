#import numpy as np
#from nltk.book import *
import nltk
from collections import defaultdict


sentences = nltk.Text(
                    nltk.word_tokenize(
                    open("sentences.txt").read()))
sentences.collocations()



made_obsolte_2014_1_1 = '''
tokens = nltk.word_tokenize(sentences)
text = nltk.Text(tokens)
nltk.word_tokenize(sentences)
sentences = open('sentences.txt').read().split('\n') 
ratings = [[ str(tags) for tags in tag_list\
                            .replace(" ","")\
                            .split(',')] 
                                for tag_list in 
                                    open('ratings.txt')\
                                    .read()\
                                    .split('\n')]
nltk.book.texts()
raw_input("waiting for a sec")
print(text1.concordance("hello"))'''