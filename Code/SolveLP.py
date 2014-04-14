from pulp import *
from GenerateILP import generateILP

def solve(points):
	lp = generateILP(points)
	maximizationOptimization = lp[0]
	constraints = lp[1]
	problem = inputProblemIntoPulp(maximizationOptimization, constraints)
	GLPK().solve(problem)

def inputProblemIntoPulp(optimization, constraints):
	problem = LpProblem("Points in Plane", LpMaximize)
	
