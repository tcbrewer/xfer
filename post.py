# we'll have a struct, [["<TF name 1>", [<bit0>,<bit1>,...]],["<TF name 2>", [<bit0>,<bit1>,...]],...] 

name = "mor1kx_40000"
out_file = name + "_out.txt"
post_file = name + "_post.txt"

def extract(tuple):
	if tuple[1] and tuple[0]:
		return "x"
	if tuple[1]:
		return "1"
	if tuple[0]:
		return "0"
	return "_"

def post():
	file = open(out_file,"r")
	bits = []
	for line in file:
		splits = line.split("]==")
		field1 = [int(s) for s in splits[1][:4]]
		field2 = [int(s) for s in splits[2][:4]]
		start1 = int(splits[0].split(":")[2])
		start2 = int(splits[1].split(":")[2])
		for i in [line, field1, field2, start1, start2]:
			1 == 1
			# print(i)
		rhs = line[line.find("TF")+2:-3]
		new_rhs = True
		for event in bits:
			#print(rhs)
			#print(event[0])
			#print(rhs==event[0])
			if rhs == event[0]:
				new_rhs = False
				for i in range(4):
					event[1][start1+i][field1[3-i]] = True
					event[1][start2+i][field2[3-i]] = True
				event[2] = event[2] + 1
		if new_rhs:
			new = [rhs,[[False,False] for _ in range(32)],1]
			for i in range(4):
				new[1][start1+i][field1[3-i]] = True
				new[1][start2+i][field2[3-i]] = True
			bits.append(new)
	file.close()
	# now we have to output items
	# do _ for neither, 1 or 0 for either, x for both
	file = open(post_file,"w")
	for field in bits:
		file.write("insns[31:0]==")
		for i in range(32):
			file.write(extract(field[1][31 - i]))
		file.write(" & " + field[0] + " & " + str(field[2]) + " \\\\\n\hline\n")
post()