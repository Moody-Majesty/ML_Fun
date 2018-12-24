import collections

import string
import nltk
from nltk.corpus import stopwords
import pickle

# PreProcessing
from nltk.util import bigrams # For bigrams
from nltk.lm.preprocessing import pad_both_ends # For padding at starting and ending
from nltk.util import everygrams  # For unigrams
from nltk.util import ngrams # For ngrams
from nltk.lm import NgramCounter
from nltk.lm.preprocessing import flatten
from nltk.lm.preprocessing import padded_everygram_pipeline

# Training
from nltk.lm import MLE

with open('data/next_word_data.txt') as f:
    data = f.readlines()


# # Preparing Data
# Before we train our **ngram** models it is necessary to make sure the data we put in them is in the right format.
def clean(doc):
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation) 
    stop_free = " ".join([i for i in doc.lower().split('[^A-Za-z]+') if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    return punc_free

text = [clean(doc).split() for doc in data]
#print(doc_clean)


# Creating bigrams
text = list(bigrams(pad_both_ends(text, n=2)))

# Creating unigrams as well as bigrams
#padded_bigrams = list(pad_both_ends(text, n=2))
#text = list(everygrams(padded_bigrams, max_len=2))
#print(text)


# During training and evaluation our model will rely on a vocabulary that defines which words are “known” to the model. To create this vocabulary we need to pad our sentences (just like for counting ngrams) and then combine the sentences into one flat stream of words.
text = list(flatten(pad_both_ends(sent, n=2) for sent in text))

# # Training a Model
train, vocab = padded_everygram_pipeline(2, text)

# let us train a **Maximum Likelihood Estimator (MLE)**. We only need to specify the highest ngram order to instantiate it.
lm = MLE(10)

lm.fit(train, vocab)

# The vocabulary helps us handle words that have not occurred during training.
# Looking for known words
#print(lm.vocab.lookup(text[11]))

# Looking for unknown (UNK) words
#lm.vocab.lookup(["aliens", "from", "Mars"])

# # Using a Trained Model
# When it comes to ngram models the training boils down to counting up the ngrams from the training corpus.
#print(lm.counts)

# However, the real purpose of training a language model is to have it score how probable words are in certain contexts. This being MLE, the model returns the item’s relative frequency as its score.
#lm.score("variation")

# Here’s how you get the score for a word given some preceding context. For example we want to know what is the chance that “b” is preceded by “a”.
#lm.score("b", ["a"])

# Building on this method, we can also evaluate our model’s cross-entropy and perplexity with respect to sequences of ngrams.
#test = [('power', 'variation'), ('over', 'temperature')]
#lm.entropy(test)
#lm.perplexity(test)

with open('model/MLE.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(lm, f)





