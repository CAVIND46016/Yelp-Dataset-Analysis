"""
Tokenizes review texts based on 'Adjective' POS only to provide as an input to wordcloud generator.
"""
import json
import csv
import re
from nltk import word_tokenize, pos_tag

def normalize_text(text):
    """
    Remove non-ASCII chars.
    """
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def generate_csv(src_file, op_file, count=None):
    """
    count ==> Number of rows needed to be created, ignore if entire .json file needs to be read.
    """
    if count is not None:
        curr = 0
        
    # Part of Speech = Adjective
    part_of_speech = ['JJ']
    
    with open(op_file, 'w', encoding='utf-8', errors='replace') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["text"])
        with open(src_file, encoding='utf-8') as j_file:
            for line in j_file:
                data = json.loads(line) 

                if data['stars'] == 1:
                    data['text'] = ''.join([normalize_text(text) for text in data['text']])  
                    word_list = word_tokenize(data['text'])
                    pos_tag_list = [x[0] for x in pos_tag(word_list) if x[1] in part_of_speech]
                    csv_writer.writerow([' '.join(pos_tag_list)])
                    if count is not None:
                        curr += 1
                        if curr == count:
                            break
                    
    print("{} generated successfully.".format(op_file))
    
def main():
    """
    Entry-point for the function.
    """
    # The input .json file for review texts
    src_file = "yelp_academic_dataset_review_restaurants.json"
    # The output wordcloud csv file for yelp star ratings = 1
    op_file = "yelp_1star_wc_sample_adj.csv"
    
    generate_csv(src_file, op_file)
    
if __name__ == "__main__":
    main()
    
