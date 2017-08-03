# dsouza{c, d, m}@indiana.edu
import json
import csv
import re

"""Remove non-ASCII chars."""
def normalize_text(text):
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def json_to_csv(json_file, csv_file, count = None):
    """
    json_file ==> .json file to be converted
    csv_file ==> output csv file
    fileType ==> 'business' or 'reviews'
    count ==> Enter number of records to be created, ignore if all records are needed.
    """
    
    with open("D:\\YELP Dataset\\tobesubmitted\\restaurantID.txt", 'r') as busIds:
        id_list = busIds.read();
        
    if(count != None):
        c = 0    
    with open(csv_file, 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file, lineterminator='\n')
        w.writerow(["text", "stars"])       
        with open(json_file, encoding = 'utf-8', errors = 'replace') as f:
            for line in f:
                data = json.loads(line) 
                if(data['business_id'] in id_list):    
                    w.writerow([data['text'], data['stars']])
                    if(count != None):
                        c = c + 1
                        if(c == count):
                            break;
                    
    print("File {} created successfully.".format(csv_file))

def main():
    json_file = "D:\\YELP Dataset\\yelp_academic_dataset_review.json"
    csv_file =  "D:\\YELP Dataset\\tobesubmitted\\yelp_academic_dataset_review.csv"
    
    json_to_csv(json_file, csv_file)
    
if(__name__ == "__main__"):
    main();