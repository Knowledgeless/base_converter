###############################
#		 Base Converter. 	 #
#		By: Knowledgeless	 #
###############################

def convert(n, b):
	k = []
	i = 0
	while(n>0):
		k.insert(0, n%b)
		n = n//b
		c = len(k)
	for i in k:
		if(i == 10):
			i = "A"
		elif(i == 11):
			i = "B"
		elif(i == 12):
			i = "C"
		elif(i == 13):
			i = "D"
		elif(i == 14):
			i = "E"
		elif(i == 15):
			i = "F"
		print(i, end=" ")
	print("\n")
		

T = int(input())
for i in range(T):
	n = int(input())
	b = int(input())
	convert(n, b)
