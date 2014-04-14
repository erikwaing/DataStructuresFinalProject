
'''
This will set the Integer Linear Program up.
We assume that all points are inside {0,...,n-1} x {0,...,n-1}
where n is the number of points.
'''

def generateILP(points):
	optimization = generateOptimization(points)
	constraints = generateConstraints(points)
	return optimization, constraints

'''
Here we want return what would be the sum of all points not in the set
This will just be all the variables. We return a vector where the variables are ordered according to
the dictionary order
'''
def generateOptimization(points):
	return [-1 for i in len(points)*len(points)]

def generateConstraints(points):
	firstType = generateFirstContraints(points)
	secondType = generateSecondConstraints(points)
	leftConstraints = firstType[0] + secondType[0]
	rightConstraints = firstType[1] + secondType[1]
	return leftConstraints, rightConstraints

'''
First Contraints are the ones that set the values of the points in the variables to 1
All the constraints are constraintsLeft * x \leq constraintsRight
'''
def generateFirstContraints(points):
	constraintsLeft = []
	constraintsRight = []
	for point in points:
		lessThanOrEqualTo = [0 for i in len(points)*len(points)]
		lessThanOrEqualTo[point[0]*len(points) + point[1]] = 1
		constraintsLeft.append(lessThanOrEqualTo)
		constraintsRight.append(1)

		greaterThanOrEqualTo = [0 for i in len(points)*len(points)]
		greaterThanOrEqualTo[point[0]*len(points) + point[1]] = -1
		constraintsLeft.append(greaterThanOrEqualTo)
		constraintsRight.append(-1)
	return constraintsLeft, constraintsRight

'''
These contraints say that each rectangle is satified
'''
def generateSecondConstaints(points):
	n = len(points)
	constraintsLeft = []
	constraintsRight = []
	for i in range(n):
		for j in range(n):
			for x in range(n):
				for y in range(n):
					one = [i,j]
					two = [x,y]
					if abs((one[0]-two[0])*(one[1]-two[1])) > 0: # there is an area between the two points
						constraint = [0 for k in n*n]
						for l in range(one[0], two[0]+1)+range(two[0], one[0]+1):
							constraint[l*n + one[1]] = -1
							constraint[l*n + two[1]] = -1
						for l in range(one[1], two[1]+1)+range(two[1], one[1]+1):
							constraint[one[0]*n + l] = -1
							constraint[two[1]*n + l] = -1
						constraint[i*n + j] = 1
						constraint[x*n + y] = 1
						constraintsLeft.append(contraint)
						constraintsRight.append(1)
	return constraintsLeft, constraintsRight

