"""
Converts .json file to .csv file
"""
import json
import csv
import re
from yelp_fieldlists import getHeaders, getData

BUSINESS    = "business"
REVIEW      = "review"
TIP         = "tip"
CHECKIN     = "checkin"
USER        = "user"

typelists   = [BUSINESS, REVIEW, TIP, CHECKIN, USER]

"""Remove non-ASCII chars."""
def normalize_text(text):
    text = re.sub('[^\x00-\x7F]+', ' ', text)
    return text

def json_to_csv(json_file, csv_file, fileType, count = None):
    """
    json_file ==> .json file to be converted
    csv_file ==> output csv file
    fileType ==> 'business' or 'review' or 'tip'
    count ==> Number of records to be created, ignore if entire .json file needs to be scanned
    """
    
    if(fileType not in typelists):
        raise ValueError('Type {} not defined.'.format(fileType));

    if(count != None):
        c = 0    
    with open(csv_file, 'w', encoding = 'utf-8', errors = 'replace') as file:
        w = csv.writer(file, lineterminator='\n')
        w.writerow(getHeaders(fileType));      
        with open(json_file, encoding = 'utf-8', errors = 'replace') as f:
            for line in f:
                data = json.loads(line)     
                if(fileType == REVIEW or fileType == TIP):  
                    data['text'] = ''.join([normalize_text(text) for text in data['text']])
                w.writerow(getData(fileType, data));
                if(count != None):
                    c = c + 1
                    if(c == count):
                        break;
                    
    print("File {} created successfully.".format(csv_file))

def main():
    type = USER
    
    json_file = "D:\\New folder\\yelp_academic_dataset_{}_restaurants.json".format(type)
    csv_file = '{0}.csv'.format(json_file.split('.json')[0]);
    
    json_to_csv(json_file, csv_file, type)
    
if(__name__ == "__main__"):
    main();