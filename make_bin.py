import random, struct

def make_bin(size):
	fout = open('test.dat', 'wb')

	for i in range(2 * size):
		fout.write(struct.pack('>i', random.randint(0, 65535)))

	fout.close()
	
make_bin(1000)