import random
import math

class FitnessCalc:
    def __init__(self, cMatrix, priorProbVector, priorProbVectorReverse):
        self.__cMatrixRowNum = 10
        self.__cMatrixColNum = 25
        self.cMatrix = cMatrix
        self.priorProbVector = priorProbVector
        self.priorProbVectorReverse = priorProbVectorReverse
        
    # calculate population fitness
    def popFit(theGen, manVector):
        rowNum = len(theGen);
        indFitVector = [0]*rowNum
        for i in range(rowNum):
            individual = theGen[i]
            indFitVector[i] = self.indFit(individual, manVector);
        return indFitVector
    
    # calculate individual fitness
    def indFit(self, disVector, manVector):
        fitValue = self.fit(disVector, manVector)
        return fitValue
    
    def fit(self, disVector, manVector):
        fitValue = self.fit1(disVector, manVector) * \
                self.fit2(disVector, manVector) * \
                self.fit3(disVector);
        return fitValue;
    
    # fit1 function
    def fit1(self, disVector, manVector):
        fitValue = 1.0;
        for i in range(self.__cMatrixRowNum):
            if (manVector[i] != 0):
                fitValue = fitValue * (1 - self.fitHelper(i, disVector));
        return fitValue;

    # helper function for fit1
    def fitHelper(self, theRowNum, disVector):
        result = 1.0;
        for i in range(self.__cMatrixColNum):
            if (disVector[i] != 0):
                result = result * (1 - self.cMatrix[theRowNum][i]);
        return result;

    # fit2 function
    def fit2(self, disVector, manVector):
        fitValue = 1.0;
        for i in range(self.__cMatrixRowNum):
            if (manVector[i] == 0):
                for j in range(self.__cMatrixColNum):
                    if (disVector[j] != 0):
                        fitValue = fitValue* (1 - self.cMatrix[i][j]);
        return fitValue;

    # fit3 function
    def fit3(self, disVector):
        fitValue = 1.0;
        for i in range(self.__cMatrixColNum):
            if (disVector[i] != 0):
                fitValue = fitValue * (self.priorProbVector[i] / self.priorProbVectorReverse[i]);
        return fitValue;


class ManGenerator:
    def getBit(self, num):
        bitVec = [int(x) for x in bin(num)[2:]];
        aManVector = [0] * 10;
        
        count = -1;
        for i in range(len(bitVec)):
            aManVector[count] = bitVec[-(i+1)];
            count -= 1;
        return aManVector;

    def getInt(self, theVector):
        for i in range(10):
            theVector[i] = str(theVector[i]);
        theStr = ''.join(theVector);
        return int(theStr, 2)