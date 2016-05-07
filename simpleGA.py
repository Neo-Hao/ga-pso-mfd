import random
import math

class SimpleGa:

    def __init__(self, popSize=5, selectionType=1, crossOverRate=0.6, mutationRate = 0.05):
        self.colNum = 25
        self.rowNum = popSize
        self.selectionType = selectionType
        self.crossOverRate = crossOverRate
        self.mutationRate = mutationRate

        self.population = [[random.getrandbits(1) for i in range(self.colNum)] \
                        for j in range(self.rowNum)]
        self.indFitVector = [0]*self.rowNum

    def __str__(self):
        output = ''
        output += 'This GA has the following parameters.\n'
        output += 'Population size: ' + str(self.rowNum) + '\n'
        output += 'Selection type: ' + str(self.selectionType) + '\n'
        output += 'Cross over rate: ' + str(self.crossOverRate) + '\n'
        output += 'Mutation Rate: ' + str(self.mutationRate) + '\n'
        return output

    ### selection
    def selection(self):
        if (self.selectionType == 1):
            self.tournamentSelect()
        else:
            self.rouletteSelect()

    ### tournament selection
    def tournamentSelect(self):
        tempoGen = [[0]*self.colNum]*self.rowNum

        for i in range(self.rowNum):
            tempoGen[i] = list(self.population[self.tourSelectInd()]);

        self.population = tempoGen

    # select a number
    def tourSelectInd(self):
        tournament = self.makeTournament();
        choice = 0
        base = -1

        for i in tournament:
            if (self.indFitVector[i] > base):
                base = self.indFitVector[i]
                choice = i

        return choice

    # generate some random numbers
    def makeTournament(self):
        selectedNum = 6
        tournament = [0]*selectedNum
        for i in range(selectedNum):
            tournament[i] = int(random.randrange(self.rowNum))
        return tournament;

    ### roulette selection
    def rouletteSelect(self):
        tempoGen = [[0]*self.colNum]*self.rowNum
        choices = roulSelectInd();

        count = 0
        for i in choices:
            tempoGen[count] = list(self.population[i]);
            count += 1

        self.population = tempoGen

    def roulSelectInd(self):
        fitVector = list(self.indFitVector)
        totalFit = sum(fitVector) + 0.0001
        for i in range(self.rowNum):
            fitVector[i] = fitVector[i]/totalFit

        fitProbV = [0]*self.rowNum
        for i in range(self.rowNum):
            count = 0
            while (count <= i):
                fitProbV[i] += fitVector[count]
                count += 1

        choices = [0] * self.rowNum
        for i in range(self.rowNum):
            choices[i] = chooseRoulette(fitProbV, self.rowNum)
        return choices

    def chooseRoulette(self, fitProbV):
        prob = random.random()

        for i in range(self.rowNum):
            if (prob < fitProbV[i]):
                return i

    ### crossover
    def crossover(self):
        count = 0;
        while (count < self.rowNum - 1):
            prob = random.random();
            if (prob < self.crossOverRate):
                self.population[count], self.population[count+1] = \
                    self.exchange(self.population[count], self.population[count+1])

            count += 2

    def exchange(self, ind1, ind2):
        xOverStart = int(random.randint(0, self.colNum-1));
        xOverEnd = int(random.randint(xOverStart, self.colNum));
        return (ind1[:xOverStart]+ind2[xOverStart:xOverEnd]+ind1[xOverEnd:], \
                ind2[:xOverStart]+ind1[xOverStart:xOverEnd]+ind2[xOverEnd:])

    ### mutation
    def mutation(self):   
        for i in range(self.rowNum):
            for j in range(self.colNum):
                prob = random.random();
                if (prob < self.mutationRate):

                    if(self.population[i][j] == 0):
                        self.population[i][j] = 1;
                    else:
                        self.population[i][j] = 0;
