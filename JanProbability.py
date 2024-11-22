import matplotlib.pyplot as plot1;
import numpy as np;

def calculateBinomialDistributionValues(trialsAmount, numArray, binomialDistribution):
    for x in range(0, trialsAmount+1):
        computedCombinatrion = (computeFactorial(trialsAmount)) / (computeFactorial(x) * computeFactorial(trialsAmount-x));
        probOfk = computedCombinatrion * (binomialDistribution[0]**x) * (binomialDistribution[1]**(trialsAmount-x));
        numArray.append(probOfk);
    return numArray;


def computeFactorial(value):
    returnValue = 1;
    for x in range(1, value+1):
        returnValue *= x; 
    return returnValue;



xCoordinates1 = [0, 1, 2, 3, 4, 5, 6, 7];
xCoordinates2 = ["X=Arrived", "X=Late/Absent"];
yCoordinates = [];

successes = 1;
failures = 1;
total = successes + failures;

distribution = [successes/total, failures/total]; #distribution[0] = P(X=success), distribution[1] = P(X=failure)

yCoordinates = calculateBinomialDistributionValues(7, yCoordinates, distribution);

for x in range(0, 8):
    print(xCoordinates1[x], yCoordinates[x]);

plot1.hist(xCoordinates1, bins=8, weights=yCoordinates, edgecolor='black', linewidth=1.2);
plot1.xlabel("Days Jan is not late/did not come");
plot1.ylabel("Probability Jan will be late/did not come");

plot1.show();