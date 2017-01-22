import sys

#cyjs_file = raw_input('Enter cyjs file: ')
#csv_file = raw_input('Name output file: ') + '.csv'
cyjs_file = sys.argv[1]
csv_file = sys.argv[2] + '.csv'

my_input_file = open(cyjs_file, "r")
ret_vlist = []
ret_elist = []
#i = 0
for line in my_input_file.readlines():
	li = line.lstrip()
	if li.startswith("name", 1):
		if "(interacts with)" in li:
			ret_elist.append(li[10:-3].replace(" (interacts with) ", "->"))
		else:
			ret_vlist.append(li[10:-3])
my_input_file.close()
my_output_file = open(csv_file, "w")
ret_vlist = ret_vlist[1:]
#print ret_vlist
#print ret_elist

#string_vlist = str(ret_vlist[1:])[1:-1]
string_vlist = ""
string_elist = ""
for item in ret_vlist:
	string_vlist = string_vlist + (str(item)) + ", "
for item in ret_elist:
	string_elist = string_elist + (str(item)) + ", "

my_output_file.write('VERTEX SET, ' + string_vlist[:-2] + ' \n')
my_output_file.write('EDGE SET, ' + string_elist[:-2] + ' \n')
my_output_file.close()