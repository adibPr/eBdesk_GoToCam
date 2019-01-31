#!/usr/bin/env python3

import os
import sys

import pandas as pd
path_this = os.path.abspath (os.path.dirname (__file__))

def load_data_sentiment ():
    path_data = os.path.join (path_this, 'data', 'sentiment_mini', 'imdb_labelled.txt')
    return pd.read_csv (path_data, sep='\t', names=['comment', 'sentiment'], header=None)

def load_lexicon_sentiment ():
    path_sentiment = os.path.join (path_this, 'data', 'lexicon')
    word = {}
    # assuming there are negative and positive word in inside $path
    for cat in ('negative', 'positive'):
        full_path = os.path.join (path_sentiment, '{}-words.txt'.format (cat))
        with open (full_path, 'r', encoding='ISO-8859-1') as f_buff:
            word[cat] = [l for l in f_buff.read ().splitlines () if l and not l.startswith (';')]
    
    return word

if __name__ == '__main__' :
    data = load_data_sentiment ()
    lexicon = load_lexicon_sentiment ()
    