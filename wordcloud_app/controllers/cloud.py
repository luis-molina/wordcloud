import numpy as np
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def generate_cloud_from_frequencies(frequencies,bg_color="white",custom_width=400,custom_height=200):
    # Create and generate a word cloud image
    # Grab background color, width and height from paremeters
    # Stropwords are set to empty and collocations disabled since this function will take in count input text that should be already cleaned for this
    wordcloud = WordCloud(background_color=bg_color,width=custom_width,height=custom_height,stopwords=set(),collocations=False).generate_from_frequencies(frequencies)

    #output the image file
    wordcloud.to_file("media/img/output.png")
