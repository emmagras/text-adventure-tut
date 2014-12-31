import numpy as np
from nltk.probability import FreqDist
from nltk.classify import SklearnClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nltk.corpus import movie_reviews
"""
class RDDMaker(object):
    ''' 
        Class designed to keep track of variables and make code more readable
    '''
    def __init__(
            self, filep=os.path.abspath(\
            '/home/emma/Dropbox/Statistics/Spark/ols_dummy_data.csv'),
            headers=True,
            app_name="rpyg",
            master="local"):

        self.conf = SparkConf().setAppName(app_name).setMaster(master)
        self.sc = SparkContext(conf=self.conf)
        self.filep = filep
        self.rdd = self.sc.textFile(abspath)
        if headers == True:
            self.rdd, self.headers = self.remove_headers(some_header_string)

"""

pipeline = Pipeline([('tfidf', TfidfTransformer()),
                     ('chi2', SelectKBest(chi2, k=1000)),
                     ('nb', MultinomialNB())])
classif = SklearnClassifier(pipeline)

sentences = open('sentences.txt').read().split('\n') 
ratings = [[ str(tags) for tags in tag_list\
                            .replace(" ","")\
                            .split(',')] 
                                for tag_list in 
                                    open('ratings.txt')\
                                    .read()\
                                    .split('\n')]        

possible_ratings = []
for ratinglist in ratings:
    for ratingword in ratinglist:
        if ratingword not in possible_ratings:
            possible_ratings.append(ratingword)
#raw_input(possible_ratings)
vocab = FreqDist(sentences)
for thing in vocab:
    raw_input(thing)
'''frequencies = []
for rating_word in possible_ratings:
    frequencies.append([FreqDist(movie_reviews.words(i)) for i in (rating_word)])'''
pos1 = []
for i in movie_reviews.fileids('pos'):
    pos1.append(FreqDist(movie_reviews.words(i)))
[FreqDist(movie_reviews.words(i)) for i in movie_reviews.fileids('pos')]
pos = [FreqDist(movie_reviews.words(i)) for i in movie_reviews.fileids('pos')]
neg = [FreqDist(movie_reviews.words(i)) for i in movie_reviews.fileids('neg')]

raw_input(pos[:10])
for thing in pos:
    print(type(thing))
    for k,v in thing:
        print(type(k))
        print(type(v))
        raw_input("wait")

add_label = lambda lst, lab: [(x, lab) for x in lst]
classif.train(add_label(pos[:100], 'pos') + add_label(neg[:100], 'neg'))

l_pos = np.array(classif.classify_many(pos[100:]))
l_neg = np.array(classif.classify_many(neg[100:]))
print "Confusion matrix:\n%d\t%d\n%d\t%d" % (
          (l_pos == 'pos').sum(), (l_pos == 'neg').sum(),
          (l_neg == 'pos').sum(), (l_neg == 'neg').sum())