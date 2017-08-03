import pandas as pd
import nltk
import csv
import json
import re
import datetime

SOURCE = 'D:\\yelp_academic_dataset_review_restaurants.json';

def normalize_text(text):
    # Remove non-ASCII chars.
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def str2Date(dt):
    return datetime.datetime.strptime(dt, "%Y-%m-%d").date()

def generateCSV(year, count = None):
    
    DESTINATION = "D:\\wordcloud datasets\\yelp_restaurants_reviews_nouns_{}.csv".format(year);
    
    bus_rest = pd.read_csv("D:\\YELP Dataset\\tobesubmitted\\yelp_academic_dataset_business_restaurants.csv", low_memory=False);
    
    required_pos = ['NNP', 'NN'] # Common and proper nouns (probable topics during christmas season)
    date_range = ['{}-12-01'.format(year), '{}-12-31'.format(year)]
    
    if(count != None):
        c = 0
        
    with open(DESTINATION, 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file, lineterminator = '\n')
        w.writerow(["name", "city", "text"])
        with open(SOURCE, encoding='utf-8') as f:
            for line in f:
                data = json.loads(line) 
                if((str2Date(data['date']) > str2Date(date_range[0])) & (str2Date(data['date']) < str2Date(date_range[1]))):
                      data['text'] = ''.join([normalize_text(text) for text in data['text'].lower()]) 

                      if(('christmas' not in data['text']) & ('Christmas' not in data['text'])):
                          continue;

                      df = bus_rest[(bus_rest['business_id'] == data['business_id'])]; 
                      word_list = nltk.word_tokenize(data['text'])
                      pos_tag_list = [x[0] for x in nltk.pos_tag(word_list) if x[1] in required_pos]
                      w.writerow([df['name'].values[0], df['city'].values[0], ' '.join(pos_tag_list)])
                      if(count != None):
                          c = c + 1;
                          if(c == count):
                              break;
                            
    print("{} created successfully.".format(DESTINATION))
    
def main():
    year = 2011;
    generateCSV(year)
    
if(__name__ == "__main__"):
    main();
    
