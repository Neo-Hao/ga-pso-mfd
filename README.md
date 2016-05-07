# Implementation of the Genetic Algorithm (GA) on the Multiple Fault Diagnosis (MFD) problems

This repo contains the implementation of the Genetic Algorithm (GA) on the Multiple Fault Diagnosis (MFD) problems.

## Files

1. fixedInput.py --- Get the input data for fitness calculation and verification
2. simpleGA.py --- Implementation of GA (<i>fitness calculation not included</i>)
3. fitnessMDF.py --- Fitness calculation based on the likelyhood function proposed by Dr. Potter from University of Georgia (<a href="http://cobweb.cs.uga.edu/~potter/CompIntell/MFD-GA.pdf" target="_blank"><i>Link to the paper</i></a>)
4. wrapperGA.py --- Combination of other essential elements of GA and generational fitness calculation
5. validator.py --- Verification of whether the implementation of GA works

## Data

<i>Note: The source of data is <a href="http://cobweb.cs.uga.edu/~potter/" target="_blank">Dr. Potter</a> from University of Georgia</i>

1. TendencyMatrix10x25.txt --- The likelyhood matrix and prior probability vector
2. ExhaustiveResults10x25.txt --- The source for verification

## Testing

Keep the file structure. Run wrapperGA.py firstly, then use the classes. An example is shown as the following:

```python
# assuming you have run wrapperGA.py
# get the optimization result from GA
manGenerator = ManGenerator()
manVector = manGenerator.getBit(350)

test = WrapperGa(1000, 1, 0.8, 0.05)
test.evolution(manVector)

# verify the GA result by comparing to 
# the "truely optimized results" retrieved from ExhaustiveResults10x25.txt
vali = Validator(table)
vali.getBestDi(350)
```

## Usage

If you have a customized fitness function, you can easily plug in your code to replace what is currently in <strong>FitnessCalc</strong> class.
