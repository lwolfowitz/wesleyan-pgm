import sys

wesdagssfile = sys.argv[1]
numcolumns = int(sys.argv[2])
outputfilename = sys.argv[3] + '.csv'

my_input_file = open(wesdagssfile, "r")
my_output_file = open(outputfilename, "w")

for line in my_input_file:
	my_output_file.write(line)

my_input_file.seek(0)
v_str = my_input_file.readline()
my_input_file.close()

v_list = v_str.split(", ")
v_list = v_list[1:]
v_list[-1] = (v_list[-1])[:-2]
#print v_list

my_output_file.write("NUM OBSERVATIONS, " + str(numcolumns) + "\n")
my_output_file.write("Vertex, ")
for x in range(1, numcolumns + 1):
	my_output_file.write("obs" + str(x) + ", ")
my_output_file.write("\n")
for item in v_list:
	my_output_file.write(str(item) + ",	,	\n")
my_output_file.close()