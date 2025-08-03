import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv('bank_data.csv')
X = df.drop('subscribed', axis=1)
y = df['subscribed'].map({'yes': 1, 'no': 0})

categorical = ['job', 'marital']
numerical = ['age', 'balance', 'duration']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), categorical)
], remainder='passthrough')

pipeline = Pipeline([
    ('prep', preprocessor),
    ('model', LogisticRegression())
])

pipeline.fit(X, y)

joblib.dump(pipeline, 'logreg_model.pkl')
