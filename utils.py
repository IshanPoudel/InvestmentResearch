import pickle
import json
import numpy as np


__model = None


def get_positive_or_negative(sentence):
    #load the model.
    return (__model.predict(sentence))


def load_artifacts():

    ''' Loads our ML model'''
    global __model

    with open("Scratch/positive_or_negative.pickle" , 'rb') as f:
        __model = pickle.load(f)

    print('Artifacts loaded')