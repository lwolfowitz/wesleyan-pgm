import sys
from operator import mul

def subtree(parent_list, edge_list):
	e_list_clone = list(edge_list)
	for parent in parent_list:
		elength = len(e_list_clone)
		print parent
		parent = parent.rstrip()
		parent = parent.lstrip()
		for item in e_list_clone:
			item = item.lstrip()
			if item.startswith(parent):
				item_list = item.split("->")
				parent_list.append(item_list[1])
		e_list_clone = [x for x in e_list_clone if not x.startswith(parent)]
	print e_list_clone
	return parent_list

def iterate(stateslist, iterobj):
	vlength = len(iterobj)
	for x in range(1, vlength + 1):
		curr_index = vlength - x
		#print curr_index
		if iterobj[curr_index] < (stateslist[curr_index] - 1):
			iterobj[curr_index] = iterobj[curr_index] + 1
			return iterobj
		else: 
			iterobj[curr_index] = 0

wesdagssfile = sys.argv[1]
outputfilename = sys.argv[2] + '.csv'

my_input_file = open(wesdagssfile, "rU")
my_output_file = open(outputfilename, "w")

for line in my_input_file:
	my_output_file.write(line)


my_input_file.seek(0)
v_str = my_input_file.readline()
#print v_str


v_list = v_str.split(", ")
v_list = v_list[1:]
v_list[-1] = (v_list[-1])[:-2]
numVerticies = len(v_list)
#print v_list

num_states_data = []
my_input_file.seek(0)
for line in my_input_file:
	cells = line.split(",")
	num_states_data.append(cells[1])
my_input_file.close()
num_states_data = num_states_data[4:(numVerticies + 4)]
num_states_data = map(int, num_states_data)
print num_states_data
product = reduce(mul, num_states_data, 1)
print product

current_state = []
for x in range(0, numVerticies):
	current_state.append(0)
print current_state
my_output_file.write("\n")
for item in v_list:
	my_output_file.write(str(item) + ",	")
my_output_file.write("\n")
#my_output_file.write(current_state)


for x in range(0, product):
	for item in current_state:
		my_output_file.write(str(item) + ", ")
	iterate(num_states_data, current_state)
	my_output_file.write("\n")




my_output_file.close()