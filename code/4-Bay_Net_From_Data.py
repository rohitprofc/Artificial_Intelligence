import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

df = pd.read_csv('heart.csv')
model = BayesianNetwork([('age','target'),('sex','target'),('exang','target'),('cp','target'),('target','restecg'),('target','chol')])
model.fit(df,estimator=MaximumLikelihoodEstimator)
infer = VariableElimination(model)

print('\n1. Probability of Heart Disease given evidence = restecg')
q1 = infer.query(variables = ['target'],evidence={'restecg':1})
print(q1)

print('\n2. Probability of Heart Disease given evidence = cp')
q2 = infer.query(variables = ['target'],evidence={'cp':2})
print(q2)

# Output:-

# 1. Probability of HeartDisease given evidence = restecg
# +-----------+---------------+
# | target    |   phi(target) |
# +===========+===============+
# | target(0) |        0.4354 |
# +-----------+---------------+
# | target(1) |        0.5646 |
# +-----------+---------------+

# 2. Probability of HeartDisease given evidence = cp
# +-----------+---------------+
# | target    |   phi(target) |
# +===========+===============+
# | target(0) |        0.3832 |
# +-----------+---------------+
# | target(1) |        0.6168 |
# +-----------+---------------+