# post processing unit, must be used in z3 directory

from z3 import *
from time import time

# we'll have a struct, [["<TF name 1>", [<bit0>,<bit1>,...]],["<TF name 2>", [<bit0>,<bit1>,...]],...] 

name = "riscv_1234_1500"
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
	start = time()
	file = open(out_file,"r")
	bits = []
	lines = 0
	for line in file:
		splits = line.split("]==")
		field1 = [int(s) for s in splits[1][:4]]
		field2 = [int(s) for s in splits[2][:4]]
		start1 = int(splits[0].split(":")[1]) # depends on architecture, 2 for mor1kx, 1 otherwise
		start2 = int(splits[1].split(":")[1])
		rhs = line[line.find("TF")+2:-3]
		new_rhs = True
		for event in bits:
			#print(rhs)
			#print(event[0])
			#print(rhs==event[0])
			if rhs == event[0]:
				#print("Prv rhs: " + rhs)
				new_rhs = False
				exp = []
				for i in range(4):
					if field1[3-i] == 1:
						exp.append(event[3][start1+i])
					else:
						exp.append(Not(event[3][start1+i]))
					if field2[3-i] == 1:
						exp.append(event[3][start2+i])
					else:
						exp.append(Not(event[3][start2+i]))
				event[2] = event[2]+1
				event[1].append(And(exp))
		if new_rhs:
			#print("New rhs: " + rhs)
			exp = []
			new = [rhs,[],1,[Bool(rhs + str(i)) for i in range(32)]]
			for i in range(4):
				if field1[3-i] == 1:
					exp.append(new[3][start1+i])
				else:
					exp.append(Not(new[3][start1+i]))
				if field2[3-i] == 1:
					exp.append(new[3][start2+i])
				else:
					exp.append(Not(new[3][start2+i]))
			new[1].append(And(exp))
			bits.append(new)
		lines = lines + 1
		if lines > 10000:
			file.close()
			file = open(post_file,"w")
			for event in bits:
				#print(event[1])
				file.write(str(Tactic('ctx-solver-simplify')(Or(event[1])))+"\n\n")
			file.write(str(time()-start))
			quit()
			
post()