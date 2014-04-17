from SolveLP import *
import random

def getIntegralityGap(n):
	points = generatePointsRandomly(n)
	integerSolution = solve(points, integer=True)
	lpSolution = solve(points, integer=False)
	return value(integerSolution.objective) / value(lpSolution.objective)

def generatePointsRandomly(n):
	points = []
	for i in range(n):
		pick = random.randint(0, i)
		points.append((i, pick))
	return points

def runTestAndStoreIn(filename, numberOfTestsPerN, startN, endN):
	with open(filename, "a") as outputfile:
		for i in range(startN,endN+1):
			for j in range(numberOfTestsPerN):
				answer = getIntegralityGap(i)
				outputfile.write(str(i) + ", " + str(answer) + "\n")

runTestAndStoreIn("tests.txt", 4, 1, 100)