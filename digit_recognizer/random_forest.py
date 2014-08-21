from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import csv_io
import scipy

def main():
    #read in the training file
    train = csv_io.read_csv("input_data/train.csv")
    train = train.values

    #set the training responses
    target = [x[0] for x in train]

    #set the training features
    train = [x[1:] for x in train]
    
    #read in the test file
    realtest = csv_io.read_csv("input_data/test.csv")
    realtest = realtest.values

    # random forest code
    rf = RandomForestClassifier(n_estimators=150, min_samples_split=2, n_jobs=-1)
    
    # fit the training data
    print('fitting the model')
    rf.fit(train, target)
    print("Fitting complete!!!")

    # run model against test data
    predicted_probs = rf.predict_proba(realtest)
        
    predicted_probs = ["%d" % x[1] for x in predicted_probs]

    total_len = len(predicted_probs)

    result_df = pd.DataFrame({"ImageId" : range(1, total_len + 1), "Label" : predicted_probs[:]})

    csv_io.write_csv("random_forest_solution.csv", result_df)
    
    print ('Random Forest Complete! You Rock! Submit random_forest_solution.csv to Kaggle')

if __name__=="__main__":
    main()