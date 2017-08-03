from string import punctuation
from collections import Counter
from itertools import chain
import csv

filename = "D:\\YELP Dataset\\wordcloud datasets\\yelp_restaurants_reviews_nouns_2011.csv";

def countInFile(_filename):
    with open(_filename, 'r') as f:
        linewords = (line.translate(punctuation).lower().split() for line in f)
        ctr = Counter(chain.from_iterable(linewords)).most_common()
        return ctr;

def generateCSV():
    with open('D:\\YELP Dataset\\dates\\New folder\\yelp_restaurants_arndchristmas2011_nouns_fc.csv', 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file, lineterminator = '\n')
        w.writerow(["word", "freq"])
        
        for wrd, freq in countInFile(filename):
            w.writerow([wrd, freq])
            
    print("Completed.")
    
def main():
    generateCSV()
    
if(__name__ == "__main__"):
    main()