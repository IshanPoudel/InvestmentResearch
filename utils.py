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

from transformers import  AutoTokenizer , AutoModelForSequenceClassification

from transformers import AutoTokenizer, AutoModelForSequenceClassification


import torch



__model = None
__tokenizer = None


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

def use_finbert_model(message):

    inputs = __tokenizer(message , padding=True , truncation = True , return_tensors = 'pt')

    outputs = __model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits , dim = -1)

    positive = predictions[:, 0].tolist()
    negative = predictions[:, 1].tolist()
    neutral = predictions[:, 2].tolist()

    print(positive , negative , neutral)

    # Find the max of three value.

    if (positive[0]>negative[0] and positive[0]>neutral[0]):
        return  "Positive"
    if (negative[0]>positive[0] and negative[0] > neutral[0]):
        return "Negative"
    if (neutral[0] > positive[0] and neutral[0] >negative[0]):
        return "Neutral"





#






def load_artifacts():

    ''' Loads our ML model'''
    global __model
    global __tokenizer

    __model = load_model('Mymodel.h5')

    __tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")

    __model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

    print('Artifacts loaded')



if __name__ == '__main__':
    load_artifacts()