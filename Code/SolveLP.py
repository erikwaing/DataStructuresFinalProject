from pulp import *
from GenerateILP import generateILP

def solve(points):
	lp = generateILP(points)
	maximizationOptimization = lp[0]
	constraints = lp[1]
	problem, variables = inputProblemIntoPulp(maximizationOptimization, constraints)
	problem.solve()
	for i in range(len(maximizationOptimization)):
		print "Point (", i / len(points), ",", i % len(points), "): ", variables[i].varValue 


def inputProblemIntoPulp(optimization, constraints):
	problem = LpProblem("Points in Plane", LpMaximize)
	variableIndexes = range(len(optimization))
	variables = LpVariable.dicts("Points", variableIndexes, 0, 1, LpBinary)
	problem += lpSum(optimization[i]*variables[i] for i in variableIndexes)
	print "Left: ", constraints[0]
	print "Right: ", constraints[1]
	for i, left in enumerate(constraints[0]):
		problem += lpSum(variables[i]*left[i] for i in variableIndexes) <= constraints[1][i]
	return problem, variables

points = [(0,0), (1, 1), (2,2), (3, 3), (4, 4), (5,5)]
solve(points)