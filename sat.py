# make a list of rhs and a list of cnfs
# combine similar lhs'similar
# output human readable

from pycosat import itersolve
import itertools

# filename
f_name = "mor1kx_40000"

def post():
	file_i = open(f_name + "_out.txt", "r")
	bits = []
	for line in file_i:
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
	file_i.close()
	for field in bits:
		#print(field[0])
		#print(field[1])
		#print(field[1][30][0])
		for i in range(32):
			#print(31 - i)
			#print(field[1][31 - i][0])
			#print(field[1][31 - i][1])
			field[1][31 - i] = (field[1][31 - i][0] and field[1][31 - i][1])
		field.append([])
		#print(field[0])
		#print(field[1])
	return bits

def lhs_to_cnf(lhs,check):
	# first we get the two clauses
	splits = lhs.split("\"")
	clauses = [splits[1], splits[3]]
	# we split clauses on the equality token to get values and locations
	out = []
	for i in range(len(clauses)):
		# get two parts - the bits, and where the bits are
		inner_splits = clauses[i].split("]==")
		bits = [int(b)*2-1 for b in inner_splits[1]]
		bits.reverse()
		start = inner_splits[0].split(":")
		start.reverse()
		start = int(start[0])
		offset = 0
		while (check[offset] == False):
			offset = offset + 1
		for b in bits:
			if check[start]:
				out.append((start-offset+1)*b) # offset for pycosat
			start = start + 1
	# return the created output
	return out	


def do_sat():
	file_i = open(f_name + "_out.txt", "r")
	file_o = open(f_name + "_sat.txt", "w")
	struct = post()
	for line in file_i:
		# lets get RHS and LHS
		splits = line.split("TF")
		rhs = splits[1].split("\"")[0]
		lhs = splits[0]
		for i in struct:
			if i[0] == rhs:
				new = lhs_to_cnf(lhs,i[1])	
				if new != []:
					i[3].append(new)
	file_i.close()
	lhs_set = set()
	for e in struct:
		#print("\n\nPrinting e[3] for "+e[0] + "\n\n")
		#print(e[3])
		# e[1] = list(itertools.islice(itersolve(e[1]), 100))
		e[3] = list(itersolve(e[3]))
		# once we're through the sat solver, we move over to tuples so we can use sets.
		for i in range(len(e[3])):
			e[3][i] = tuple(e[3][i])
		e[3] = tuple(e[3])
		lhs_set.add(e[3])
	lhs_lst = [[e,set()] for e in lhs_set]
	for e in struct:
		for lhs in lhs_lst:
			if lhs[0] == e[3]:
				splits = e[0].split("==")
				for split in splits:
					lhs[1].add(split)
	#print(struct)
	# ok, so next we want to do the lhs combine
	# this gives the number of satisfying arrangements, the number of bits varied, and the register names
	for lhs in lhs_lst:
		if (len(lhs[0]) > 0):
			print(str(len(lhs[0])) + " " + str(len(lhs[0][0])) + " " + str(lhs[1]))
	# now we want to take a look to see if any bits never vary
	bitcheck = [set() for lhs in lhs_lst]
	for i in range(len(lhs_lst)):
		for bitlist in lhs_lst[i][0]:
			for bit in bitlist:
				bitcheck[i].add(bit)
	#print(bitcheck)
	# actually we didn't want to check that LOL
	
do_sat()