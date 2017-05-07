import json

""" Business yelp dataset file """
SOURCE = 'D:\\New folder\\yelp_academic_dataset_review_restaurants.json';

def findNWriteListToTxt():
    """
    catg ==> Category
    Checks for "categories" column under business dataset and writes only the business id's
    based on user entered category 'catg', into a text file.
    """
    txt_file = open("D:\\New folder\\userID.txt", "w")
    with open(SOURCE, encoding='utf-8', errors = 'replace') as f:
        for line in f:
            data = json.loads(line); 
            txt_file.write("{}\n".format(data['user_id']));          
                
    txt_file.close();
    print("List created successfully.")

def main():
    findNWriteListToTxt();

if(__name__ == "__main__"):
    main();