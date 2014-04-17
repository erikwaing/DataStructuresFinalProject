import matplotlib.pyplot as plt

def visualizeResults(filename):
	inputFile = open(filename)
	x = []
	y = []
	for line in inputFile:
		if "," in line:
			values = line.split(",")
			x.append(float(values[0]))
			y.append(float(values[1]))
	plt.plot(x, y, 'ro')
	plt.ylabel('Integrality Gap')
	plt.xlabel('Randomly Generated n points')
	plt.show()