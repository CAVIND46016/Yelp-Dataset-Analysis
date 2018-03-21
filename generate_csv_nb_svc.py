"""
Creating input file for running NB and SVM classifiers
"""
import json
import csv
import re

def normalize_text(text):
    """
    Remove non-ASCII chars.
    """
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def json_to_csv(json_file, csv_file, count=None):
    """
    json_file ==> .json file to be converted
    csv_file ==> output csv file
    fileType ==> 'business' or 'reviews'
    count ==> Enter number of records to be created, ignore if all records are needed.
    """
    
    with open("restaurantID.txt", 'r') as bus_id:
        id_list = bus_id.read()
        
    if count is not None:
        curr = 0    
    with open(csv_file, 'w', encoding='utf-8', errors='replace') as file:
        csv_writer = csv.writer(file, lineterminator='\n')
        csv_writer.writerow(["text", "stars"])       
        with open(json_file, encoding='utf-8', errors='replace') as j_file:
            for line in j_file:
                data = json.loads(line) 
                if data['business_id'] in id_list:    
                    csv_writer.writerow([data['text'], data['stars']])
                    if count is not None:
                        curr += 1
                        if curr == count:
                            break
                    
    print("File {} created successfully.".format(csv_file))

def main():
    """
    Entry-point for the function.
    """
    json_file = "yelp_academic_dataset_review.json"
    csv_file = "yelp_academic_dataset_review.csv"
    
    json_to_csv(json_file, csv_file)
    
if __name__ == "__main__":
    main()
    
