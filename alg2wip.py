import sys
from operator import mul
import itertools


def iterate(stateslist, iterobj):
	vlength = len(iterobj)
	for x in range(1, vlength + 1):
		curr_index = vlength - x
		if iterobj[curr_index] < (stateslist[curr_index] - 1):
			iterobj[curr_index] = iterobj[curr_index] + 1
			return iterobj
		else: 
			iterobj[curr_index] = 0

def parent_tree(vertex, edge_list):
	parent_list = [vertex]
	e_list_clone = list(edge_list)
	vertex = vertex.rstrip()
	vertex = vertex.lstrip()
	for item in e_list_clone:
		item = item.rstrip()
		item = item.lstrip()
		if item.endswith(vertex):
			item_list = item.split("->")
			parent_list.append(item_list[0])
	return parent_list

def gen_matrix_simple(pro_p_list, raw_dict, product):
	current_state = []
	stateslist = []
	for x in range(0, len(pro_p_list)):
		current_state.append(0)
	#print current_state
	my_output_file.write("\n")
	for item in pro_p_list:
		my_output_file.write(str(item) + ",	")
		stateslist.append(raw_dict[item])
	my_output_file.write("\n")
#my_output_file.write(current_state)
	for x in range(0, product):
		for item in current_state:
			my_output_file.write(str(item) + ", ")
		iterate(stateslist, current_state)
		my_output_file.write("\n")

def gen_matrix_hill(pro_p_list, raw_dict, product):
	stateslist = []
	listolists = []
	inv_prod = 1
	running_repeat = int(product)
	for item in pro_p_list:
		my_output_file.write(str(item) + ",	")
		stateslist.append(raw_dict[item])
		listolists.append([])
	my_output_file.write("\n")
	for x in range(0, len(pro_p_list)):
		running_repeat = (running_repeat / stateslist[x])
		#print (len(pro_p_list))
		for y in range (0, inv_prod):
			for z in range(0, stateslist[x]):
				temp_write = list(itertools.repeat(z, (running_repeat)))
				(listolists[x]).extend(temp_write)
				#y = y + 1
		inv_prod = inv_prod * stateslist[x]
		#print (listolists)
	for x in range(0, product):
		for y in range(0, len(pro_p_list)):
			#print len(listolists[y])
			#print ("1")
			#print len(pro_p_list)
			my_output_file.write(str(((listolists[y])[x])))
			my_output_file.write(",")
		my_output_file.write("\n")



wesdagssfile = sys.argv[1]
outputfilename = sys.argv[2] + '.csv'

my_input_file = open(wesdagssfile, "rU")
my_output_file = open(outputfilename, "w")

#for line in my_input_file:
	#my_output_file.write(line)

my_input_file.seek(0)
v_str = my_input_file.readline()
#print v_str

v_list = v_str.split(", ")
v_list = v_list[1:]
v_list[-1] = (v_list[-1])[:-2]
numVerticies = len(v_list)
#print v_list

my_input_file.seek(0)
my_input_file.readline()
e_str = my_input_file.readline()
e_list = e_str.split(", ")
e_list = e_list[1:]
e_list[-1] = (e_list[-1])[:-2]
#print e_list

num_states_data = []
my_input_file.seek(0)
for line in my_input_file:
	cells = line.split(",")
	num_states_data.append(cells[1])
my_input_file.close()
num_states_data = num_states_data[4:(numVerticies + 4)]
num_states_data = map(int, num_states_data)

raw_dict = dict(zip(v_list, num_states_data))
#print raw_dict
#print num_states_data

#e_list_clone = list(e_list)
#to_work_on_list = []
#to_work_on_list.append(parent)
#for item in e_list_clone:
#	if item.startswith(parent):
#		item_list = item.split("->")
#		to_work_on_list.append(item_list[1])
#for item in e_list_clone:
#	if item.startswith(parent):
#		e_list_clone.remove(item)

for key in raw_dict:
	pro_p_list = parent_tree(key, e_list)
	product = 1
	for item in pro_p_list:
		product = product * raw_dict[item]
	my_output_file.write("Here is the data for " + key +":" +"\n")
	gen_matrix_hill(pro_p_list, raw_dict, product)

my_output_file.close()