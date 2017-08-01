import random
random.seed()
def run_it(n):
	prev = None
	for i in range(n):
		flip = random.random()
		if flip <= .8:
			prev = 1
		else:
			if prev == 0:
				return False
			prev = 0

	return True

total = 0
good = 0
for i in range(int(1e7)):
	if i % 1000000 == 0:
		print(i)
	total+=1
	if run_it(82):
		good+=1


for i in range(numTrials):
	for j in range(81):
		if ......
			

print(float(good/total))