import numpy as np
#from nltk.book import *
import nltk.book
from collections import defaultdict


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
print(text1.concordance("hello"))