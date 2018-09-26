import itertools
import random

def computeSum(solution,activity,sumsArray,n):
	sums=0
	max_sum=0
	for i in range(n):
		for j in range(n):
			if solution[i][j]==1:
				sums+=activity[i][j]
	if sums>max_sum:
		max_sum=sums
	sumsArray.append(max_sum)

def solveNQueenProblem(solution,column,n,activity,sums,sumsArray):
	if column==n:
		computeSum(solution,activity,sumsArray,n)
		return True
	final=False
	sums=0
	for i in range(n):
		if checkIfPolicemanIsSafe(n,i,column,solution):
			solution[i][column]=1
			final=solveNQueenProblem(solution,column+1,n,activity,sums,sumsArray) or final
			solution[i][column]=0			
	return final	
	
def checkIfPolicemanIsSafe(n,row,col,solution):
	# Checking row on left side
	for i in range(col):
		if solution[row][i] == 1:
			return False
	# Checking row on right side
	for i in range(col,n):
		if solution[row][i] == 1:
			return False
	# Checking column above
	for i in range(row):
		if solution[i][col] == 1:
			return False
	# Checking column below
	for i in range(row,n):
		if solution[i][col] == 1:
			return False
    # Checking upper right diagonal
	i=row
	j=col
	while i>=0 and j<n:
		if solution[i][j] == 1:
			return False
		i-=1
		j+=1  
    # Checking lower right diagonal
	i=row
	j=col
	while i<n and j<n:
		if solution[i][j] == 1:
			return False
		i+=1
		j+=1  
	# Checking upper left diagonal
	i=row
	j=col
	while i>=0 and j>=0:
		if solution[i][j] == 1:
			return False
		i-=1
		j-=1  
	# Checking lower left diagonal
	i=row
	j=col
	while i<n and j>=0:
		if solution[i][j] == 1:
			return False
		i+=1
		j-=1  
	return True


def initialiseBoard(n):
	board = [[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			board[i][j]=0
	return board


def maximizeActivityPoints(l):
	max_points = 0
	for i in l:
		sumOfEachSafeSituation = 0
		ones = 0
		newBoard = initialiseBoard(n)
		for j in i:
			if checkIfPolicemanIsSafe(n,j[0],j[1],newBoard):
				newBoard[j[0]][j[1]] = 1
				ones+=1
				sumOfEachSafeSituation+=activity[j[0]][j[1]]
				if ones==p:
					if sumOfEachSafeSituation > max_points:
						max_points = sumOfEachSafeSituation
	return max_points


f = open("input.txt","r")
output= open("output.txt","w+")
lines=f.readlines()
n=int(lines[0])
p=int(lines[1])
s=int(lines[2])

activity = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
	for j in range(n):
		activity[i][j]=0

for l in range(3,(s*12)+3):
	myList = lines[l].strip().split(",")
	r=int(myList[0])
	c=int(myList[1])
	activity[c][r]+=1
	

if p<n:
	ListOfAllIndices = []
	for i in range(n):
		for j in range(n):
			k = (i,j)
			ListOfAllIndices.append(k)


	l = itertools.combinations(ListOfAllIndices,p)

	maxPoints = maximizeActivityPoints(l)
	output.write(str(maxPoints))
	
else:
	sumsArray =[]
	newBoard = initialiseBoard(n)
	solveNQueenProblem(newBoard,0,p,activity,0,sumsArray)
	sumsArray.sort(reverse=True)
	output.write(str(sumsArray[0]))
	
	





