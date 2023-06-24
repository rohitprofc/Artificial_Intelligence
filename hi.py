import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
df = pd.read_csv('heart.csv')
df.head(5)
df.tail(5)
df.columns
df.info()
df.isnull().sum()
model = BayesianNetwork([('age','sex'),('fbs','chol')])
model.fit(df, estimator=MaximumLikelihoodEstimator)
print(model.get_cpds('age'))
