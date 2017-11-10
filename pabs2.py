import pandas as pd
import numpy as np
import pickle
attack_node_global=-1
data_dict = {}


def initialize():
	for node in data_dict:
		data_dict[node] = 8*[0]
		if node == attack_node_global:
			data_dict[node][0] = 1

def add_new_node(node_id):

	i_value = 8*[0]
	i_value[1] = 1
	if node_id == attack_node_global:

		i_value[0] = 1
	data_dict[node_id] = i_value


def update_dict_data(node, index):
	data_dict[node][index] +=1

def analyse_file(file_name, attack_node):
	attack_node_global = attack_node
	print attack_node_global, type(attack_node_global)
	prev = 0
	nop = 4
	file = open(file_name, 'r')

	initialize()
	counter = 0

	for line in file:

		data = line.split('\t')



		start_node = int(data[1])

		reciever_nodes = data[2].split(',')


		if start_node not in data_dict:
			add_new_node(int(data[1]))

		for a in reciever_nodes:
			if str.isdigit(a):
				if int(a) not in data_dict:
					add_new_node(int(a))


		if 'DIS' in line:
			update_dict_data(start_node, 2)
			for x in reciever_nodes:
				if str.isdigit(x):
					update_dict_data(int(x), 3)

		if 'DAO' in line:
			update_dict_data(start_node, 4)
			for x in reciever_nodes:
				if str.isdigit(x):
					update_dict_data(int(x), 5)

		if 'DIO' in line:
			update_dict_data(start_node, 6)
			for x in reciever_nodes:
				if str.isdigit(x):
					update_dict_data(int(x), 7)


		counter += 1

		if counter == 200:
			print data_dict

			pickle.dump(data_dict, open( "save.p", "wb" ) )
			initialize()
			counter = 0

	if counter < 200:
		print data_dict
		pickle.dump(data_dict, open( "save.p", "wb" ) )


analyse_file('attacks/hello-mal.txt', 11)