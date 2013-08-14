#Prime factorization

#Given a number, return a list of that number's prime factors
def factor( num ):
    #The number to divide by as a factorization test
    factor = 2;
    resultList = [];
    
    #if factor = num, there are no more factors to test.
    while ( factor < num ):
        if ( num % factor == 0 ):
            num /= factor;
            resultList.append( factor );
        else:
            #Inefficient: tests non-prime numbers. To optimize, include prime number test function.
            factor += 1;
    
    #add the last prime factor
    resultList.append( factor);
        
    return resultList;
            
def main():
    resultList = factor( 600851475143 );
    resultList.sort();
    print( resultList.pop() );
    
main();
