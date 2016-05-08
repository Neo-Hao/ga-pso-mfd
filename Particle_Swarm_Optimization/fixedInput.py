# fixed input: c-matrix, prob vector, reverse prob vector
### fixed input 1
matrixRowNum = 11
matrixColNum = 25
## get prior probability vector and c matrix
# read file content and split by linebreaks
with open("data/TendencyMatrix10x25.txt") as f:
    content = f.read().splitlines() 

# make a tendency matrix
tendencyMatrix = [[float(content[matrixColNum*i + i + j]) for j in range(matrixColNum)] for i in range(matrixRowNum)]

# make a prior prob vector
priorProbVector = tendencyMatrix[0]
# make a prior prob-sub vector
priorProbVectorReverse = [0]*matrixColNum
for i in range(matrixColNum):
    priorProbVectorReverse[i] = 1 - priorProbVector[i]

# make a c matrix
cMatrix = tendencyMatrix[1:11]

### fixed input 2
table = [[0]*4]*1023
# read file content and split by linebreaks
with open("data/ExhaustiveResults10x25.txt") as f:
    count = 0
    lines = f.readlines()
    for line in lines:
        table[count] = line.split()
        count += 1
