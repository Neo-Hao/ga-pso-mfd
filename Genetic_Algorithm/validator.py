class Validator:
    def __init__(self, table):
        self.table = table

    def getBestDi(self, rowNum):
        rowNum = rowNum - 1;
        theList = table[rowNum][1:4];
        for i in range(len(theList)):
            theList[i] = math.ceil(float(theList[i])*1000000)/1000000;
        print(theList);
        #return theList;