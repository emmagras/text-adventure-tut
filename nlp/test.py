import nltk

raw = "all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy. \
    all work and no play makes jack a dull boy."

tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.collocations()
