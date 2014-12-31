from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize, wordpunct_tokenize
from nltk.collocations import *

"http://www.nltk.org/book/ch06.html"
"http://www.nltk.org/book/ch03.html"

def get_msg_words(msg, stopwords=[], strip_html=False):
    """ Returns the set of unique words contained in each line
    of the message, omitting any in the optionally provided
    list."""
    
    msg_words = set(wordpunct_tokenize(msg))
    input("msg_words: "+str(msg_words))

def clean_strings(item):
    return item.strip('"').strip('\n').lower()

rpg_sentences = open('sentences.txt').read().split('\n')
(train_size,test_size) = (0.75*len(rpg_sentences), 0.25*len(rpg_sentences))


#for item in rpg_sentences:
#    print(item.strip('"').strip('\n').lower())
#[newlist.append(item.strip('"').strip('\n').lower()) for item in rpg_sentences]

rpg_sentences = map(lambda item:clean_strings(item), rpg_sentences)
print(rpg_sentences)


get_msg_words(rpg_sentences)

#tokens = word_tokenize(rpg_sentences)


#vendor_text = nltk.Text(tokens)
#vendor_text.collocations()

