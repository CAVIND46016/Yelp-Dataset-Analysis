# dsouza{c, d, m}@indiana.edu
# Fetches a list of restaurant business Id's so that review texts can be filtered easily based on restaurant category only.
import json

""" Business yelp dataset file """
SOURCE = 'yelp_academic_dataset_business.json';

def findNWriteListToTxt(catg):
    """
    catg ==> Category
    Checks for "categories" column under business dataset and writes only the business id's
    based on user entered category 'catg', into a text file.
    """
    txt_file = open("restaurantID.txt", "w")
    id_list = []
    with open(SOURCE, encoding='utf-8', errors = 'replace') as f:
        for line in f:
            data = json.loads(line);
            if(catg in str(data['categories'])):  
                txt_file.write("{}\n".format(data['business_id']));          
                
    txt_file.close();
    print("List created successfully.")

def main():
    catg = 'Restaurants'
    findNWriteListToTxt(catg);

if(__name__ == "__main__"):
    main();
