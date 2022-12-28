import json
import tensorflow as tf
from tensorflow import keras
import keras_nlp
import numpy as np
from data_package.data_generator.text_generation.config.core import TEXT_CORPUS_FILE
from loguru import logger

def clean_text_corpus(text_corpus):
    text_corpus = text_corpus.replace('\n', ' ').split(' ')
    text_list = list(filter(None, text_corpus))
    return text_list

def retrieve_texts(text_urls):
    """
    Returns a corpus of concatenated  text docs
    input dictionary:
        key:string of text
        value: url of text doc
    output string corpus
    """
    texts = ''
    for name in text_urls.keys():
        filepath = keras.utils.get_file(f'{name}.txt', origin=text_urls[name])
        text = ''
        with open(filepath, encoding='utf-8') as f:
            text = f.read()
            # First 50 lines are the Gutenberg intro and preface
            # Skipping first 10k characters for each book should be approximately
            # removing the intros and prefaces.
            texts += text[10000:]
    return clean_text_corpus(text)

def create_unique_list(text_list):
    """
    creates a set for first iteration of text
    """
    text_list = list(set(text_list))
    return text_list


def save_list(text_list):
    """
    save list as json
    """
    logger.info(f"Saving files in {DATASET_DIR.stem}")
    with open(TEXT_CORPUS_FILE, "w") as fp:
        json.dump(text_list, fp)



