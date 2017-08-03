# dsouza{c, d, m}@indiana.edu
# Tokenizes review texts based on 'Adjective' POS only to provide as an input to wordcloud generator.
import json
import csv
import re
from nltk import word_tokenize, pos_tag

""" The input .json file for review texts """
SOURCE = "D:\\YELP Dataset\\yelp_academic_dataset_review.json"

""" The output wordcloud csv file for yelp star ratings = 1 """
OUTPUT = "D:\\YELP Dataset\\tobesubmitted\\wordcloud datasets\\Yelp_1star_wc_sample_adj.csv"

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
        
    with open("D:\\YELP Dataset\\tobesubmitted\\restaurantID.txt", 'r') as busIds:
        id_list = busIds.read();
    
    part_of_speech = ['JJ'] # Part of Speech = Adjective
    
    with open(OUTPUT, 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file)
        w.writerow(["text"])
        with open(SOURCE, encoding='utf-8') as f:
            for line in f:
                data = json.loads(line) 
                """ star filter for restaurant """
                if(data['stars'] == 1 and (data['business_id'] in id_list)):
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
    

