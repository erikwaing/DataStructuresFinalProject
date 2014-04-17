from pulp import *
from GenerateILP import generateILP

def solve(points, integer=False):
	lp = generateILP(points)
	maximizationOptimization = lp[0]
	constraints = lp[1]
	problem, variables = inputProblemIntoPulp(maximizationOptimization, constraints, integer)
	problem.solve()
	#for i in range(len(maximizationOptimization)):
	#	print "Point (", i / len(points), ",", i % len(points), "): ", variables[i].varValue
	#print "Objective: ", value(problem.objective
	return problem


def inputProblemIntoPulp(optimization, constraints, integer=False):
	problem = LpProblem("Points in Plane", LpMaximize)
	variableIndexes = range(len(optimization))
	if integer:
		variables = LpVariable.dicts("Points", variableIndexes, 0, 1, LpBinary)
	else:
		variables = LpVariable.dicts("Points", variableIndexes, 0, 1)
	problem += lpSum(optimization[i]*variables[i] for i in variableIndexes)
	#print "Left: ", constraints[0]
	#print "Right: ", constraints[1]
	for i, left in enumerate(constraints[0]):
		problem += lpSum(variables[i]*left[i] for i in variableIndexes) <= constraints[1][i]
	return problem, variables