# coding=UTF-8
#
# Calculates the N most user words from a given text, using stopwords removal and NLTK

import sys
import codecs
import nltk
from .cloud import generate_cloud_from_frequencies
import re

def calculateAndGenerateCloud(input_text,max_words,language,custom_stopwords_text):

    try:
        total_words_wanted = int(max_words)

        cloud_width = 800
        cloud_height = 600

        # Obtaining default stopwords according to language
        default_language_stopwords = set(nltk.corpus.stopwords.words(language.lower()))

        # Obtaining custom stopwords from custom stopwords text
        # The stopwords should be one per line
        custom_stopwords = set(custom_stopwords_text.splitlines())

        # Merge the language stopwords with the custom stopwords
        all_stopwords = default_language_stopwords | custom_stopwords

        # first, remove all punctuation using regex
        input_text = re.sub(r'[^\w\s]',' ',input_text)

        words = nltk.word_tokenize(input_text)

        # second check for punctuation, remove single character words, which are mostly punctuation
        words = [word for word in words if len(word) > 1]

        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Set all words to lowercase all words (the default language stopwords are lowercase and the custom stopwords should be too)
        words = [word.lower() for word in words]

        # Remove the stopwords
        words = [word for word in words if word not in all_stopwords]

        # Calculate frequency distribution
        frequency_distribution = nltk.FreqDist(words)

        # init frequencies dict
        frequencies = dict()

        for word, frequency in frequency_distribution.most_common(total_words_wanted):
            # in case of using generate_cloud_from_frequency
            frequencies[word] = frequency

        # generate cloud output image
        generate_cloud_from_frequencies(frequencies,"white",cloud_width,cloud_height)

        return 'success'
    except ValueError:
        return 'no-words-for-cloud'
    except:
        return 'unexpected-fail'