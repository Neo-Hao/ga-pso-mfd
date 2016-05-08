import random
import numpy as np

class BinaryPso:
    def __init__(self, popSize=5, inertia = 0.7, c1= 2, c2 = 2):
        # parameters
        self.colNum = 25
        self.rowNum = popSize
        self.w = 0.7
        self.c1 = 2
        self.c2 = 2
        self.colNum = 25
        # population and fitness
        self.population = [[random.getrandbits(1) for i in range(self.colNum)] \
                        for j in range(self.rowNum)]
        self.indFitVector = [0]*self.rowNum
        # current velocity
        self.vcurMatrix = [[0 for i in range(self.colNum)] for j in range(self.rowNum)]
        # pbestMatrix
        self.pbestMatrix = list(self.population)
        self.pbestFit = list(self.indFitVector)
        # gbest
        self.gbestFit = max(self.pbestFit);
        self.gbest = list(self.pbestMatrix[self.pbestFit.index(self.gbestFit)])
        
    def __str__(self):
        output = ''
        output += 'This binary PSO has the following parameters.\n'
        output += 'Population size: ' + str(self.rowNum) + '\n'
        output += 'Inertia: ' + str(self.w) + '\n'
        output += 'Global influence: ' + str(self.c1) + '\n'
        output += 'Cognitive influence: ' + str(self.c2) + '\n'
        return output
    
    # update Vcur Matrix
    def updateVcurMatrix(self):
        for i in range(self.rowNum):
            self.updateVcurInd(i)
    
    # updateVcurMatrix helper
    def updateVcurInd(self, id):
        individual = self.population[id]
        vcurs = list(self.vcurMatrix[id])
        pbest = self.pbestMatrix[id]
        
        newV = [0 for i in range(self.colNum)]
        
        for i in range(self.colNum):
            newV[i] = vcurs[i] + \
                self.c1*random.random()*(pbest[i] - individual[i]) + \
                self.c2*random.random()*(self.gbest[i] - individual[i])
        for i in range(self.colNum):
            if (newV[i] > 4):
                newV[i] = 4
            if (newV[i] < -4):
                newV[i] = -4

        self.vcurMatrix[id] = newV

    ## relocate
    def relocate(self):
        for i in range(self.rowNum):
            self.relocateInd(i)
    
    # relocate helper
    def relocateInd(self, id):
        newIndividual = [0 for i in range(self.colNum)]
        vnews = self.vcurMatrix[i]

        for j in range(self.colNum):
            if (random.random() < self.sigmoid(vnews[j])):
                newIndividual[j] = 1;
            else:
                newIndividual[j] = 0;
                
        self.population[id] = newIndividual

    def sigmoid(self, value):
        return 1.0/(1.0 + np.exp(-(value)))

    # update pbest
    def updatePbest(self):
        for i in range(self.rowNum):
            self.updatePbestInd(i)

    def updatePbestInd(self, id):
        pFit = self.pbestFit[id]
        gFit = self.indFitVector[id]

        if (pFit < gFit):
            self.pbestMatrix[id] = list(self.population[id])
            self.pbestFit[id] = gFit
    
    # update gbest
    def updateGbest(self):
        if (max(self.pbestFit) > self.gbestFit):
            self.gbestFit = max(self.pbestFit)
            self.gbest = list(self.pbestMatrix[self.pbestFit.index(self.gbestFit)])