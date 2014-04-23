from SolveLP import *
import random
import math

def getIntegralityGap(n):
	points = generatePointsRandomly(n)
	integerSolution = solve(points, integer=True)
	print "*********"
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

def runOnInverseBinarySequence(filename, startN, endN):
	with open(filename, 'a') as outputfile:
		for i in range(startN, endN +1):
			points = generateInverseBinaryPoints(int(math.pow(2, i)))
			integerSolution = solve(points, integer=True)
			print '****'
			lpSolution = solve(points, integer=False)
			integralityGap = value(integerSolution.objective) / value(lpSolution.objective)
			outputfile.write(str(i) + ", " + str(integralityGap) + "\n")

def generateInverseBinaryPoints(n):
	l = len(bin(n-1)) - 2
	sequence = [reverseBinary(i, l) for i in range(n)]
	return [(i, sequence[i]) for i in range(len(sequence))]

def reverseBinary(i, l):
	binaryString = bin(i)
	reversedBinaryString = binaryString[2:][::-1]
	while len(reversedBinaryString) < l:
		reversedBinaryString = reversedBinaryString + "0"
	return int(reversedBinaryString, 2)

runOnInverseBinarySequence("inverseBinary.txt", 3, 6)
#runTestAndStoreIn("tests.txt", 100, 1, 10)