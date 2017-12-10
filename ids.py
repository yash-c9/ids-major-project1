from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename

import tkMessageBox

from pgmpy.models import BayesianModel

from pgmpy.estimators import BayesianEstimator
from graph import Graph
import numpy as np
import pandas as pd
import pickle
import copy
import time
import TestModel

# Global Functions for ease of access of file
def prop(n):
	return 360.0*n/total

bayesianmodel = BayesianModel()
paramlist = ['Protocol_type','Service','Wrong_Fragmant','Land',
			'Num_Failed_Login','Logged_in','Root_Shell','Is_guest_login','attack']
data_frame = pd.DataFrame()
root_of_network = 'Protocol_type'

# GUI Segment
master = Tk()
master.title('Intrusion Detection System')
top_frame = Frame(master)
top_frame.pack(side=TOP, padx=10, pady=10)
bottom_frame = Frame(master)
bottom_frame.pack(side=BOTTOM, padx=10, pady=10)
left_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1)
left_frame.pack(side=LEFT, padx=10, pady=10)
right_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1)
right_frame.pack(side=RIGHT, padx=10, pady=10)

canvas_width = 800
canvas_height = 500

w = Canvas(left_frame, width=canvas_width,
		height=canvas_height)
c = Canvas(right_frame, width= 500, height=500)
c.pack(side=RIGHT)

file_name = Entry(top_frame, width=100)


# graph segment



def get_edges():
	l = len(paramlist)
	a = 0
	b = 0
	edge_list = []
	while(a<l-1):
		b = 0
		while(b<l):
			if(bayesianmodel.has_edge(paramlist[a], paramlist[b])):
				print "frkj"
				edge_list.append((paramlist[a], paramlist[b]))

			b+=1
		a+=1

	return edge_list
# gui command functions
def update_canvas(edge_list, vertex_list, root_vertex):
	# g = Graph(edge_list, root_vertex)
	# dag_height = g.get_height()
	# vertex_hash = {}
	# vertex_positions = {}
	# # initialising the vertex hash
	# for vertex in vertex_list:
	# 	vertex_hash[vertex] = 0
	# height_interval = canvas_height/(dag_height+2)
	# circle_width = 10
	# #print "height interval", height_interval
	# #print "canvas_height", canvas_height
	# # add circles
	# queue_vertex = []
	# queue_vertex.append(root_vertex)
	# #print queue_vertex
	# counth = 1
	# while len(queue_vertex) != 0:
	# 	len_queue = 0
	# 	for vertex in queue_vertex:
	# 		if vertex_hash[vertex] == 0:

	# 			len_queue += 1
	# 			print len_queue, vertex_hash[vertex], vertex
	# 	print vertex_hash
	# 	print len_queue
	# 	width_interval = canvas_width/(len_queue+1)
	# 	dlist = []
	# 	countw = 1
	# 	for vertex in queue_vertex:
	# 		if vertex_hash[vertex] == 0:
	# 			width_vertex = width_interval*countw
	# 			height_vertex = height_interval*counth

	# 			vertex_positions[vertex] = [width_vertex, height_vertex]
	# 			w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
	# 				width_vertex+ circle_width, height_vertex+circle_width,
	# 				outline="grey",fill="#1f1", width=0)
	# 			w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex))

	# 			vertex_hash[vertex]=1
	# 			if vertex in g.adj_list:
	# 				for v in g.adj_list[vertex]:
	# 					if v not in dlist:

	# 						dlist.append(v)
	# 			countw += 1

	# 	queue_vertex = dlist

	# 	print queue_vertex
	# 	counth += 1
	# print vertex_positions
	print vertex_list
	
	levels = (len(vertex_list)+3)/2
	length_level = canvas_height/(levels+1)
	height_vertex = length_level
	width_vertex = canvas_width/2
	circle_width = 10
	vertex_positions = {}
	print length_level
	print len(vertex_list)
	print levels

	# first vertex
	w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
					width_vertex+ circle_width, height_vertex+circle_width,
	 				outline="grey",fill="#1f1", width=0)
	w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex_list[0]))
	vertex_positions[vertex_list[0]] = [width_vertex, height_vertex]
	width_vertex = canvas_width/2
	height_vertex += length_level
	w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
				width_vertex+ circle_width, height_vertex+circle_width,
				outline="grey",fill="#1f1", width=0)
	w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex_list[1]))
	vertex_positions[vertex_list[1]] = [width_vertex, height_vertex]


	width_level = canvas_width/3
	width_vertex = width_level
	k=2
	for i in range(2,levels-1):
		height_vertex += length_level
		width_vertex = width_level
		w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
					width_vertex+ circle_width, height_vertex+circle_width,
	 				outline="grey",fill="#1f1", width=0)
		w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex_list[k]))
		vertex_positions[vertex_list[k]] = [width_vertex, height_vertex]
		k=k+1
		width_vertex += width_level
		w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
					width_vertex+ circle_width, height_vertex+circle_width,
	 				outline="grey",fill="#1f1", width=0)
		w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex_list[k]))
		vertex_positions[vertex_list[k]] = [width_vertex, height_vertex]
		k=k+1
	# last vertex
	width_vertex = canvas_width/2
	height_vertex += length_level
	w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
				width_vertex+ circle_width, height_vertex+circle_width,
				outline="grey",fill="#1f1", width=0)
	w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex_list[k]))
	vertex_positions[vertex_list[k]] = [width_vertex, height_vertex]





	for edge in edge_list:
	 	pos1 = vertex_positions[edge[0]]
	 	pos2 = vertex_positions[edge[1]]
	 	print "pos1", pos1
	 	print "pos2", pos2
	 	w.create_line(pos1[0], pos1[1]+circle_width,
	 	 pos2[0], pos2[1]-circle_width, tags=("line",), arrow="last")


def delete_canvas():
	w.delete('all')

def real_update_canvas():
	delete_canvas()

	update_canvas(get_edges(), paramlist, root_of_network)

def openfile():

    filename = askopenfilename(parent=master)
    file_name.delete(0, 'end')
    file_name.insert(0,filename)

def load_network():
	# complete
	filename = file_name.get()
	if len(filename) == 0:
		# enter file name
		tkMessageBox.showinfo("File Error", "Please enter file name")
		return

	
	

	global bayesianmodel
	bayesianmodel = copy.deepcopy(pickle.load(open('alpha', 'rb')))
	print bayesianmodel.has_edge('Protocol_type', 'Service')

	print type(bayesianmodel), get_edges()
	tkMessageBox.showinfo("Message", "Network Successfully Loaded")



def load_data_file():
	# complete
	filename = file_name.get()
	if len(filename) == 0:
		# enter file name
		tkMessageBox.showinfo("File Error", "Please enter file name")
		return

	try:
		global data_frame
		data_frame = pd.read_csv(filename)

		tkMessageBox.showinfo("Message", "File Successfully Loaded")

	except:
		tkMessageBox.showinfo("File Error", "File not present")

def save_network():

	if len(get_edges()) == 0:
		tkMessageBox.showinfo("Message", "No network to save")

	filename = asksaveasfilename()
	if filename is None:
		return
	pickle.dump(bayesianmodel, open(filename, 'wb'))


def train_network():
	print "network Trained"

	bayesianmodel.fit(data_frame, estimator=BayesianEstimator)

def print_statistics(values):
	c.delete('all')
	global total

	(total,tp, fp, tn, fn, tpr, tnr, ppv, npv, fnr, fpr, fdr, acc) = values
	print total
	c.create_text(200,270, text="True Positive Rate:  "+str(values[5]))
	c.create_text(200,300, text="True Negative Rate:  "+str(values[6]))
	c.create_text(200,330, text="Positive Prediction Value:  "+str(values[7]))
	c.create_text(200,360, text="Negative Prdiction Value:  "+str(values[8]))
	c.create_text(200,390, text="False Negative Rate: "+str(values[9]))
	c.create_text(200,420, text="False Positive Rate:  "+str(values[10]))
	c.create_text(200,450, text="Accuracy :  "+str(values[12]))



	c.create_arc((2,2,250,250), fill="#FAF402", outline="#FAF402", start = prop(0), extent = prop(tp))
	c.create_text(390,100, text="True Positive:"+str(values[1]))
	c.create_rectangle(300, 90, 320, 110, fill="#FAF402")

	c.create_arc((2,2,250,250), fill="#00AC36", outline="#00AC36", start = prop(tp), extent = prop(fp))
	c.create_text(390,130, text="False Positive:"+str(values[2]))
	c.create_rectangle(300, 120 , 320, 140, fill="#00AC36")

	c.create_arc((2,2,250,250), fill="#7A0871", outline="#7A0871", start = prop(tp+fp), extent = prop(tn))
	c.create_text(390,160, text="True Negative:"+str(values[3]))
	c.create_rectangle(300, 150, 320, 170, fill="#7A0871")

	c.create_arc((2,2,250,250), fill="#E00022", outline="#E00022", start = prop(tn+tp+fp), extent = prop(fn))
	c.create_text(390,190, text="False Negative:"+str(values[4]))
	c.create_rectangle(300, 180, 320, 200, fill="#E00022")

def test_network():
	print 'testing network'
	if data_frame.empty:
		tkMessageBox.showinfo("Message", "No data file loaded")
		return
	values =TestModel.test(data_frame, bayesianmodel)
	print_statistics(values)







# main packing for all buttons
w.pack()
file_name.pack(side=LEFT)


train = Button(bottom_frame, text="Train", command=train_network)
train.pack(side=LEFT)

test = Button(bottom_frame, text="Test", command=test_network)
test.pack(side=LEFT)

update = Button(left_frame, text="Update", command=real_update_canvas)
update.pack()

save = Button(left_frame, text="Save", command=save_network)
save.pack(side=LEFT)

delete_c = Button(left_frame, text="Delete", command=delete_canvas)
delete_c.pack(side=RIGHT)
im = PhotoImage('file_button.png')
file_button = Button(top_frame, text=':', command=openfile)
file_button.pack(side=LEFT)

load_data = Button(top_frame, text='Load Data File', command=load_data_file)
load_data.pack()
load_trained = Button(top_frame, text='Load Network', command=load_network)
load_trained.pack()

mainloop()
