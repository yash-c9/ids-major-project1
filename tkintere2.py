from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
master = Tk()
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
statcanvas = Canvas(right_frame, width= 300, height=500)
statcanvas.pack(side=RIGHT)

file_name = Entry(top_frame, width=100)
class Graph:
	def __init__(self, edge_list, root_vertex):
		self.max_height = 1000
		self.adj_list = {}
		self.rootv = root_vertex
		self.get_adj_list(edge_list, root_vertex)
		print self.adj_list


	def dfs(self, root, height):

		height += 1
		
		if root == 'attack' or root not in self.adj_list:
			self.max_height = min(self.max_height, height)
			return
		for ver in self.adj_list[root]:
			self.dfs(ver, height)



	def get_adj_list(self, edge_list, root_vertex):
		
		for edge in edge_list:
			if edge[0] in self.adj_list:
				dlist = self.adj_list[edge[0]]
				dlist.append(edge[1])
				self.adj_list[edge[0]] = dlist
			else:
				dlist = [edge[1]]
				self.adj_list[edge[0]] = dlist
			


	def get_height(self):
		self.dfs(self.rootv, 0)
		return self.max_height




def update_canvas(edge_list, vertex_list, root_vertex):
	g = Graph(edge_list, root_vertex)
	dag_height = g.get_height()
	vertex_hash = {}
	vertex_positions = {}
	# initialising the vertex hash
	for vertex in vertex_list:
		vertex_hash[vertex] = 0
	height_interval = canvas_height/(dag_height+2)
	circle_width = 10
	#print "height interval", height_interval
	#print "canvas_height", canvas_height
	# add circles
	queue_vertex = []
	queue_vertex.append(root_vertex)
	#print queue_vertex
	counth = 1
	while len(queue_vertex) != 0:
		len_queue = 0
		for vertex in queue_vertex:
			if vertex_hash[vertex] == 0:

				len_queue += 1
				print len_queue, vertex_hash[vertex], vertex
		print vertex_hash
		print len_queue
		width_interval = canvas_width/(len_queue+1)
		dlist = []
		countw = 1
		for vertex in queue_vertex:
			if vertex_hash[vertex] == 0:
				width_vertex = width_interval*countw
				height_vertex = height_interval*counth

				vertex_positions[vertex] = [width_vertex, height_vertex]
				w.create_oval(width_vertex- circle_width, height_vertex-circle_width, 
					width_vertex+ circle_width, height_vertex+circle_width,
					outline="grey",fill="#1f1", width=0)
				w.create_text(width_vertex, height_vertex-circle_width-10, text=str(vertex))
				vertex_hash[vertex]=1
				if vertex in g.adj_list:
					for v in g.adj_list[vertex]:
						if v not in dlist:

							dlist.append(v)
				countw += 1

		queue_vertex = dlist

		print queue_vertex
		counth += 1
	print vertex_positions
	w.create_line(400-circle_width,100+circle_width, 266+circle_width,200-circle_width, tags=("line",), arrow="last")
	

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
	update_canvas([('Protocol_type','Wrong_Fragmant'), ('Protocol_type','Land'), 
	('Protocol_type','Service'), ('Wrong_Fragmant','Num_Failed_Login'), 
	('Wrong_Fragmant','Logged_in'), ('Land','Num_Failed_Login' ),
	('Land','Wrong_Fragmant'), ('Service','Num_Failed_Login' ), ('Service','Land' ),
	('Service','Root_Shell' ), ('Service','Is_guest_login' ),
	('Service','Logged_in' ),('Service', 'attack'), ('Logged_in','Is_guest_login' ), ('Logged_in','Root_Shell'),
	('Num_Failed_Login','Logged_in' ), ('Num_Failed_Login','Root_Shell' ),
	('Root_Shell','Is_guest_login' ), ('Root_Shell','attack' ), ('Is_guest_login', 'attack')

	 ], ['Protocol_type','Service','Land','Wrong_Fragmant','Num_Failed_Login','Logged_in','Root_Shell','Is_guest_login','attack'], 'Protocol_type')

def openfile():

    filename = askopenfilename(parent=master)
    file_name.insert(0,filename)

def load_network():
	filename = file_name.get()
	if len(filename) == 0:
		# enter file name
		tkMessageBox.showinfo("File Error", "Please enter file name")
		return

	try:
		f = open(filename, 'r')
		tkMessageBox.showinfo("Message", "Network Successfully Loaded")
		f.close()
	except:
		tkMessageBox.showinfo("File Error", "File not present")

def load_data_file():
	filename = file_name.get()
	if len(filename) == 0:
		# enter file name
		tkMessageBox.showinfo("File Error", "Please enter file name")
		return

	try:
		f = open(filename, 'r')
		tkMessageBox.showinfo("Message", "File Successfully Loaded")
		f.close()
	except:
		tkMessageBox.showinfo("File Error", "File not present")

w.pack()
file_name.pack(side=LEFT)

update_canvas([('Protocol_type','Wrong_Fragmant'), ('Protocol_type','Land'), 
	('Protocol_type','Service'), ('Wrong_Fragmant','Num_Failed_Login'), 
	('Wrong_Fragmant','Logged_in'), ('Land','Num_Failed_Login' ),
	('Land','Wrong_Fragmant'), ('Service','Num_Failed_Login' ), ('Service','Land' ),
	('Service','Root_Shell' ), ('Service','Is_guest_login' ),
	('Service','Logged_in' ),('Service', 'attack'), ('Logged_in','Is_guest_login' ), ('Logged_in','Root_Shell'),
	('Num_Failed_Login','Logged_in' ), ('Num_Failed_Login','Root_Shell' ),
	('Root_Shell','Is_guest_login' ), ('Root_Shell','attack' ), ('Is_guest_login', 'attack')

	 ], ['Protocol_type','Service','Land','Wrong_Fragmant','Num_Failed_Login','Logged_in','Root_Shell','Is_guest_login','attack'], 'Protocol_type')
train = Button(bottom_frame, text="Train")
train.pack(side=LEFT)

test = Button(bottom_frame, text="Test")
test.pack(side=LEFT)

update = Button(left_frame, text="Update", command=real_update_canvas)
update.pack()

delete_c = Button(left_frame, text="Delete", command=delete_canvas)
delete_c.pack()
im = PhotoImage('file_button.png')
file_button = Button(top_frame, text=':', command=openfile)
file_button.pack(side=LEFT)

load_data = Button(top_frame, text='Load Data File', command=load_data_file)
load_data.pack()
load_trained = Button(top_frame, text='Load Trained Network', command=load_network)
load_trained.pack()

mainloop()
