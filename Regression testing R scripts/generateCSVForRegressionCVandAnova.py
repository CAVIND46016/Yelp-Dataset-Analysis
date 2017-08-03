import csv
import re
import json
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

SOURCE = 'D:\\YELP Dataset\\yelp_academic_dataset_review.json';
CSV_FILE = 'D:\\YELP Dataset\\yelp_regression.csv'
    
"""Remove non-ASCII chars."""
def normalize_text(text):
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def generateCSV(count = None):
    tokenizer = RegexpTokenizer(r'\w+')
    stemmer = PorterStemmer()
    
    with open("positive-words.txt") as f:
        pos_words = f.read().split()[213:]
    
    with open("negative-words.txt") as f:
        neg_words = f.read().split()[213:]

    with open("D:\\YELP Dataset\\tobesubmitted\\restaurantID.txt", 'r') as busIds:
        id_list = busIds.read();
            
    if(count != None):
        c = 0    
    with open(CSV_FILE, 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file, lineterminator='\n')
        w.writerow(["review_length", "pos_words", "neg_words", "stars"])
  
        with open(SOURCE, encoding = 'utf-8', errors = 'replace') as f:
            for line in f:
                data = json.loads(line) 
                if(data['business_id'] in id_list):    
                    data['text'] = ''.join([normalize_text(text) for text in data['text']]) 
                    word_list = tokenizer.tokenize(data['text'])
                    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
                    stemmed_words = []
                    for i in filtered_words:
                        stemmed_words.append(stemmer.stem(i))

                    num_positive = sum([r in pos_words for r in stemmed_words])
                    num_negative = sum([r in neg_words for r in stemmed_words])
                    w.writerow([str(len(data['text'])), str(num_positive), str(num_negative), data['stars']])  
                    if(count != None):
                        c = c + 1
                        if(c == count):
                            break;
                    
    print("{} generated successfully.".format(CSV_FILE))
    
def main():
    generateCSV()
    
if(__name__ == "__main__"):
    main();