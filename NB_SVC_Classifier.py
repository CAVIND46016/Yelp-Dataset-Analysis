#dsouza{c, d, m}@indiana.edu
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

def predictClassifier(type):
    df = pd.read_csv("D:\\YELP Dataset\\tobesubmitted\\yelp_academic_dataset_review.csv");
     
    tv = TfidfVectorizer(min_df = 50);
    x = tv.fit_transform(df['text'].values.astype('U'))
    y = df['stars']
     
    x, y = shuffle(x, y)
     
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 3057)
    
    if(type == 0):
        clf = MultinomialNB().fit(x_train, y_train)
    else:  
        clf = SVC(kernel = 'linear')
        
    clf.fit(x_train, y_train)
     
    y_pred = clf.predict(x_test);
    
    print(accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test.values.tolist(), y_pred.tolist(), labels=[1, 2, 3, 4, 5]))
    print("Completed.")

def main():
    #Naive Bayes = 0, SVM = 1
    type = 0
    predictClassifier(type)
    
if(__name__ == "__main__"):
    main()