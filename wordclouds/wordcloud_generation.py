#!/usr/bin/env python
"""https://github.com/amueller/word_cloud/blob/master/examples/simple.py"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generateWordCloud(text):
    """
    text ==> string to be considered for generating wordcloud
    #***************************************************************************************
    #*    Title: word_cloud
    #*    Author: Andreas Mueller
    #*    Availability: https://github.com/amueller/word_cloud/blob/master/examples/simple.py"
    #***************************************************************************************
    """
    wc = WordCloud(max_font_size = 40).generate(text)
    plt.imshow(wc, interpolation = "bilinear")
    plt.axis("off")
    plt.show()

def main():
    dataset = open("D:\\YELP Dataset\\tobesubmitted\\wordcloud datasets\\Yelp_1star_wc_sample_adj.csv", 'r').read();
    generateWordCloud(dataset);
    
if(__name__ == "__main__"):
    main();