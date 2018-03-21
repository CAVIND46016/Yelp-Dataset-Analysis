"""
https://github.com/amueller/word_cloud/blob/master/examples/simple.py
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wc(text):
    """
    text - string to be considered for generating wordcloud
    ***************************************************************************************
    *    Title: word_cloud
    *    Author: Andreas Mueller
    *    Availability: https://github.com/amueller/word_cloud/blob/master/examples/simple.py"
    ***************************************************************************************
    """
    w_cloud = WordCloud(max_font_size=40).generate(text)
    plt.imshow(w_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def main():
    """
    Entry-point for the function
    """
    data_set = open("yelp_1star_wc_sample_adj.csv", 'r').read()
    generate_wc(data_set)
    data_set.close()
    
if __name__ == "__main__":
    main()
