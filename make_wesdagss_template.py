import sys

wesdagfile = sys.argv[1]
outputfilename = sys.argv[2] + '.csv'

my_input_file = open(wesdagfile, "r")
my_output_file = open(outputfilename, "w")

for line in my_input_file:
	my_output_file.write(line)

my_input_file.seek(0)
v_str = my_input_file.readline()
my_input_file.close()

v_list = v_str.split(", ")
v_list = v_list[1:]
v_list[-1] = (v_list[-1])[:-2]
print v_list

my_output_file.write("VERTEX STATES \n")
my_output_file.write("Vertex,	num_states \n")
for item in v_list:
	my_output_file.write(str(item) + ",	,	\n")
my_output_file.close()