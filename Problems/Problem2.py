#Simple script to add even values of the Fibonacci sequence up to four million

#Standard fibonacci function with added check for evenness and maintenance of running total
#Calculates values up to and including the limit
def evenFibonacciSum( limit ):
    nextNum = 2;
    curNum  = 1;
    lastNum = 1;
    evenSum = 0;
    
    while ( curNum <= limit ):
    
        if ( curNum % 2 == 0 ):
            evenSum += curNum;
    
        #Change lastNum first to preserve the value of curNum
        lastNum = curNum;
        #Get the new curNum
        curNum = nextNum;
        #Calculate the nextNum
        nextNum = curNum + lastNum;
        
    return evenSum;
    
def main():
        print( evenFibonacciSum( 4000000 ) );

main();
