import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import BayesianEstimator
import pickle

def get_edges(bayesianmodel, node_list):
	print "hello"
	l = len(node_list)
	a = 0
	b = 0
	edge_list = []
	while(a<l-1):
		b = 0
		while(b<l):
			if(bmodel.has_edge(node_list[a], node_list[b])):
				print "frkj"
				edge_list.append((node_list[a], node_list[b]))

			b+=1
		a+=1

	return edge_list


data = pd.read_csv('kdd_required2.csv')
print data
# 'Protocol_type','Service','Land','Wrong_Fragmant','Num_Failed_Login','Logged_in','Root_Shell','Is_guest_login','attack'

model = BayesianModel([('Protocol_type','Wrong_Fragmant'), ('Protocol_type','Land'), 
	('Protocol_type','Service'), ('Wrong_Fragmant','Num_Failed_Login'), 
	('Wrong_Fragmant','Logged_in'), ('Land','Num_Failed_Login' ),
	('Land','Wrong_Fragmant'), ('Service','Num_Failed_Login' ), ('Service','Land' ),
	('Service','Root_Shell' ), ('Service','Is_guest_login' ),
	('Service','Logged_in' ),('Service', 'attack'), ('Logged_in','Is_guest_login' ), ('Logged_in','Root_Shell'),
	('Num_Failed_Login','Logged_in' ), ('Num_Failed_Login','Root_Shell' ),
	('Root_Shell','Is_guest_login' ), ('Root_Shell','attack' ), ('Is_guest_login', 'attack')

	 ])
model.fit(data, estimator=BayesianEstimator)



# print coin_model.has_edge('X','Y')

# x = model.get_cpds('attack')
# print x

# pickle.dump(model, open('alpha', 'wb'))

from pgmpy.inference import VariableElimination
restaurant_inference = VariableElimination(model)

# 0,2,0,0,0,0,0,0,not-normal


b=restaurant_inference.query(variables=['attack'],
		evidence={ 'Protocol_type':0,'Service':3,'Land':0,'Wrong_Fragmant':0
		,'Num_Failed_Login':0,'Logged_in':1,'Root_Shell':0,'Is_guest_login':0})
print b['attack'].values[0]

# print get_edges(coin_model, ['X', 'Y'])