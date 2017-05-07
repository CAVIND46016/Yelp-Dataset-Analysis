import json

""" Business yelp dataset file """
SOURCE = 'yelp_academic_dataset_review_restaurants.json';

def findNWriteListToTxt():
    txt_file = open("userID.txt", "w")
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
