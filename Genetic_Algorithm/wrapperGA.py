exec(open('fixedInput.py').read())
exec(open('simpleGA.py').read())
exec(open('fitnessMDF.py').read())
exec(open('validator.py').read())

class WrapperGa(SimpleGa):

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
    
    def evolution(self, manVector):
        self.indFitVector = self.popFit(manVector)
        best = max(self.indFitVector)
        
        limit = 60
        while (limit > 0):
            self.selection()
            self.crossover()
            self.mutation()
            self.indFitVector = self.popFit(manVector)
            best = max(self.indFitVector)
            limit -= 1
        
        print(best)