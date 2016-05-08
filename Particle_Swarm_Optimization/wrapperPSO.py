exec(open('fixedInput.py').read())
exec(open('binaryPSO.py').read())
exec(open('fitnessMDF.py').read())
exec(open('validator.py').read())

class WrapperPso(BinaryPso):

    fitnessCore = FitnessCalc(cMatrix, priorProbVector, priorProbVectorReverse)
    
    # calculate population fitness
    def popFit(self, manVector):
        indFitVector = [0]*self.rowNum
        for i in range(self.rowNum):
            individual = self.population[i]
            indFitVector[i] = self.indFit(individual, manVector);
        return indFitVector
    
    # calculate individual fitness
    def indFit(self, disVector, manVector):
        fitValue = self.fitnessCore.fit(disVector, manVector)
        return fitValue
    
    def fly(self, manVector):
        self.indFitVector = self.popFit(manVector)
        # initialize pbestMatrix
        self.pbestMatrix = list(self.population)
        self.pbestFit = list(self.indFitVector)
        # initialize gbest
        self.gbestFit = max(self.pbestFit);
        self.gbest = list(self.pbestMatrix[self.pbestFit.index(self.gbestFit)])
        
        rounds = 60
        for i in range(rounds):
            # updat vcurMatrix
            self.updateVcurMatrix()
            # relocate
            self.relocate()
            self.indFitVector = self.popFit(manVector)
            # update pbest
            self.updatePbest()
            # update gbest
            self.updateGbest()
        
        print(self.gbestFit)
        print(self.gbest)