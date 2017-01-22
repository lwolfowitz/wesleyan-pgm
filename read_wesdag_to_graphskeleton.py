import sys

wesdagfile = sys.argv[1]
outputfilename = wesdagfile[:-4] + "GS" + ".txt"

my_input_file = open(wesdagfile, "r")
my_output_file = open(outputfilename, "w")

my_input_file.seek(0)
v_str = my_input_file.readline()
e_str = my_input_file.readline()
my_input_file.close()

v_list = v_str.split(", ")
v_list = v_list[1:]
v_list[-1] = (v_list[-1])[:-2]

e_list = e_str.split(", ")
e_list = e_list[1:]
e_list[-1] = (e_list[-1])[:-2]
for x in range(0, len(e_list)):
	e_list[x] = '[' + '"' + str(e_list[x]).replace("->", '"' + ", " + '"') + '"' + '] '
#	e_list[x] = str(e_list[x])
#	e_list[x] = (e_list[x])[3:]
#	print e_list[x]

my_output_file.write( "{ \n")
my_output_file.write("	" + '"' + "V" + '"' + ": [" )
for x in range(0, len(v_list) - 1):
	my_output_file.write('"' + str(v_list[x]) + '"' + ", ")
my_output_file.write('"' + str(v_list[-1]) + '"')
my_output_file.write("], \n")

my_output_file.write("	" + '"' + "E" + '"' + ": [")
my_output_file.write(str(e_list[0])[:-1] + ", \n")
for x in range(1, len(e_list) - 1):
	my_output_file.write(str(e_list[x])[:-1] + ", \n")
my_output_file.write("	    " + str(e_list[-1])[:-1] + "] \n")
# + str(e_list) + "], \n")
my_output_file.write( "}")
my_output_file.close()

#print e_list