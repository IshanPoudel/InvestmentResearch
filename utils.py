import pickle
import json
import numpy as np

import  pandas as pd
import numpy as np
from tqdm import tqdm
from keras.preprocessing.text import Tokenizer
tqdm.pandas(desc="progress-bar")
from gensim.models import Doc2Vec
from sklearn import utils
from sklearn.model_selection import train_test_split
from keras_preprocessing.sequence import pad_sequences

import gensim
from sklearn.linear_model import LogisticRegression
from gensim.models.doc2vec import TaggedDocument
import re
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model



__model = None


def get_negative_neutral_positive(message):
    global __model


    # message = ['The local electronics industry is expected to remain stable amid layoff concerns surrounding Japanese electronics giants operating in the country, an official says.']

    tokenizer = Tokenizer(num_words=50000 , split=' ' , filters= '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' , lower=True)
    seq = tokenizer.texts_to_sequences(message)

    padded = pad_sequences(seq , maxlen=50 , dtype='int32' , value=0)

    pred = __model.predict(padded)

    labels = ['Negative' , 'Neutral' , 'Positive']

    # print(pred , labels[np.argmax(pred)])
    return (labels[np.argmax(pred) ])

def load_artifacts():

    ''' Loads our ML model'''
    global __model

    __model = load_model('Mymodel.h5')

    print('Artifacts loaded')



if __name__ == '__main__':
    load_artifacts()