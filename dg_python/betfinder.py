import os

for x in range(1,1001,1):
	for a in range(1,1001,1):
		for b in range(1,1001,1):
			for c in range(1,1001,1):
				for d in range(1,1001,1):
					for e in range(1,1001,1):
						for f in range(1,1001,1):
							print("calculating ......................................... %{}".format(x))
							os.system('cls' if os.name == 'nt' else 'clear')

							if (a%7==0) and  (b%7==0) and  (c%7==0) and  (d%7==0) and  (e%7==0) and  (f%7==0) and  (x%7==0) :
								if ((2*a)>=x) and  ((3*b)>=x) and  ((6*c)>=x) and  ((11*d)>=x) and  ((21*e)>=x) and  ((41*f)>=x) :
									print("\n")
									print("*********************************************************")
									print("*********************************************************")
									print("\n")
									print("\t")
									print("a : {}".format(a))
									print("\n")
									print("b : {}".format(b))
									print("\n")
									print("c : {}".format(c))
									print("\n")
									print("d : {}".format(d))
									print("\n")
									print("e : {}".format(e))
									print("\n")
									print("f : {}".format(f))
									print("\n")
									print("x : {}".format(x))
									print("\n")
									print("*********************************************************")
									print("*********************************************************")
								else :
									print("\n")
									print("*********************************************************")
									print("*********************************************************")
									print("\n")
									print("  THESE NUMBERS DOES NOT EXISTS   ")
									print("\n")									 
									print("*********************************************************")
									
