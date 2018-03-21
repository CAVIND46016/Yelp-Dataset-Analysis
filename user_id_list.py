"""
Retrieve a list of user id's
"""
import json

def write_to_text(src_file, op_file):
    """
    Retreieve the list and write to text file.
    """
    txt_file = open(op_file, "w")
    with open(src_file, encoding='utf-8', errors='replace') as j_file:
        for line in j_file:
            data = json.loads(line)
            txt_file.write("{}\n".format(data['user_id']))         
                
    txt_file.close()
    print("List created successfully.")

def main():
    """
    Entry-point for the main function.
    """
    src_file = 'yelp_academic_dataset_review_restaurants.json'
    op_file = 'user_id.txt'
    
    write_to_text(src_file, op_file)

if __name__ == "__main__":
    main()
    
