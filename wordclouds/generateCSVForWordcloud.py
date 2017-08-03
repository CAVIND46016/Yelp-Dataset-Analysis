# Tokenizes review texts based on 'Adjective' POS only to provide as an input to wordcloud generator.
import json
import csv
import re
from nltk import word_tokenize, pos_tag

""" The input .json file for review texts """
SOURCE = "D:\\yelp_academic_dataset_review_restaurants.json"

""" The output wordcloud csv file for yelp star ratings = 1 """
OUTPUT = "D:\\Yelp_1star_wc_sample_adj.csv"

def normalize_text(text):
    # Remove non-ASCII chars.
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def generateCSV(count = None):
    """
    count ==> Number of rows needed to be created, ignore if entire .json file needs to be read.
    """
    if(count != None):
        c = 0;
    
    part_of_speech = ['JJ'] # Part of Speech = Adjective
    
    with open(OUTPUT, 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file)
        w.writerow(["text"])
        with open(SOURCE, encoding='utf-8') as f:
            for line in f:
                data = json.loads(line) 
                """ star filter for restaurant """
                if(data['stars'] == 1):
                    data['text'] = ''.join([normalize_text(text) for text in data['text']])  
                    word_list = word_tokenize(data['text'])
                    pos_tag_list = [x[0] for x in pos_tag(word_list) if x[1] in part_of_speech]
                    w.writerow([' '.join(pos_tag_list)])
                    if(count != None):
                        c = c + 1;
                        if(c == count):
                            break;
                    
    print("{} generated successfully.".format(OUTPUT))
    
def main():
    generateCSV()
    
if(__name__ == "__main__"):
    main();
    

