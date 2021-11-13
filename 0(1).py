import math
def DunN(A, x):
	Greenland = 14.8
	MDun = 0
	FeDun = 0
	MFRatio = 2/3
	Avrp = (A - (60.0 - Greenland)*x)/60.0
	MaleN = math.ceil(Avrp / (1 + 1/MFRatio))
	FemaleN = math.ceil(Avrp / (1 + MFRatio))
	if MaleN <= 100 :
		MDun = MaleN % 25
	else:
		MDun = 4 + (MaleN - 100) % 50
	if FemaleN < 100 :
		FeDun = FemaleN % 15
	else:
		FeDun = 6 + (FemaleN - 100) % 30
	print("Male : " + str(MDun))
	print("Female : " + str(FeDun))
	return [MDun, FeDun]

A = int(input("公园面积: "))
x = int(input("公园人数: "))
DunN(A, x)