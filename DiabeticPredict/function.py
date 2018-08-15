import pandas as pd
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.preprocessing import Imputer
from sklearn.linear_model import LogisticRegression


def predict_diabetic(model, test_data):

    train_df = pd.read_csv(model)
    logistic_model = LogisticRegression()
    columns = ["AGE", "weight(kg)", "height(cm)", "BMI", "Systolic pressure", "Diastolic pressure", "LDL", "HDL",
               "Triglyceride"]
    labels = train_df["Outcome"].values
    features = train_df[list(columns)].values
    kfold = StratifiedKFold(n_splits=10,random_state=0)
    logistic_model_score = cross_val_score(logistic_model, features, labels, cv=kfold, n_jobs=-1).mean()
    print("{0} -> Current Model Accuracy: {1})".format(columns, logistic_model_score))
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(features)

    test_df = pd.read_csv(test_data)
    logistic_model.fit(features, labels)

    predictions = logistic_model.predict(imp.transform(test_df[columns].values))
    test_df["Outcome"] = pd.Series(predictions)
    return test_df


def save_result(df, output):

    df.to_csv(output, columns=["AGE", "weight(kg)", "height(cm)", "BMI", "Systolic pressure",
                               "Diastolic pressure", "LDL", "HDL", "Triglyceride", "Outcome"], index=False)
