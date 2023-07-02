from pgmpy.models import BayesianNetwork 
from pgmpy.factors.discrete import TabularCPD 
import networkx as nx 
import pylab as plt

# Defining Bayesian Structure
model=BayesianNetwork([('Guest','Host'),('Price','Host')])
# Defining the CPDs:
cpd_guest=TabularCPD('Guest',3,[[0.33],[0.33],[0.33]])
cpd_price=TabularCPD('Price',3,[[0.33],[0.33],[0.33]])
cpd_host=TabularCPD('Host',3,[[0,0,0,0,0.5,1,0,1,0.5],[0.5,0,1,0,0,0,1,0,0.5],[0.5,1,0,1,0.5,0,0,0,0]],evidence=['Guest','Price'],evidence_card=[3,3])

# Associating the CPDs with the network structure.
model.add_cpds(cpd_guest,cpd_price,cpd_host)

model.check_model()

# Infering the posterior probability
from pgmpy.inference import VariableElimination 

infer=VariableElimination(model)
posterior_p=infer.query(['Host'],evidence={'Guest':2,'Price':2})
print(posterior_p)

# Output:-
# +---------+-------------+
# | Host    |   phi(Host) |
# +=========+=============+
# | Host(0) |      0.5000 |
# +---------+-------------+
# | Host(1) |      0.5000 |
# +---------+-------------+
# | Host(2) |      0.0000 |
# +---------+-------------+
