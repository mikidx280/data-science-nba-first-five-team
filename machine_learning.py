from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn import linear_model, metrics, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.linear_model import LogisticRegression

def do_more_samples(X, y):
    ros = RandomOverSampler(sampling_strategy=0.5, random_state=14)
    ros.fit(X, y)
    X, y = ros.fit_resample(X, y)
    return X, y

def predict_new(classifier, X_test):
    y_pred=classifier.predict(X_test)
    resDF = pd.DataFrame({"Predicted": y_pred})
    resDF["Predicted"] = y_pred
    return resDF

df=pd.read_csv('df_the_org.csv')
df2 = df.copy()
df2.rename(columns={'year played': 'year_played'}, inplace=True)
df2_names = df2.loc[df2['year_played'] == 2021]
df3=df2_names.copy()
df2_names = df2_names["Player_name"]
df2 = df2.drop(['Player_name','team name','age','position'], axis=1)
df2.loc[df2['year_played']>2020,'year_played']=np.nan
df2.dropna(inplace=True)



TRAINING_FEATURES = df2.columns[df2.columns != 'won']
TARGET_FEATURE = 'won'

X = df2[TRAINING_FEATURES]
y = df2[TARGET_FEATURE]

# Oversample with SMOTE for imbalanced dataset
from imblearn.over_sampling import RandomOverSampler
X, y = do_more_samples(X,y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)

model = LogisticRegression(max_iter=12000).fit(X_train, y_train)
y_pred = model.predict(X_test)
resDF = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

resDF["correct"] = abs((resDF["Actual"] ^ resDF["Predicted"]) - 1)
resDF[resDF["correct"] == 1]
evaluate_value = metrics.f1_score(y_test, y_pred)
print("F1_score is: ", evaluate_value)

import seaborn as sns

confusion_matrix = pd.crosstab(resDF["Actual"], resDF["Predicted"], rownames=['Actual'], colnames=['Predicted'])

sns.heatmap(confusion_matrix, fmt = ".0f", annot=True)
plt.show()
sns.heatmap(confusion_matrix/np.sum(confusion_matrix), annot=True, fmt = ".2%", cmap = 'magma')
plt.show()
# Predict on dataset which model has not seen before


X = df3[TRAINING_FEATURES]
y = df3[TARGET_FEATURE]

df3_res = predict_new(model, X)
df3_res.reset_index()
df2_names = df2_names.to_frame()
df2_names.reset_index(inplace=True)
df2_names = df2_names.drop('index', 1)
frames = [df3_res, df2_names]
predictions = pd.concat(frames, axis=1)

result_helper = predictions.loc[predictions['Predicted'] == 1]
result=result_helper.head().copy()
result.to_csv("result.csv",index=False)