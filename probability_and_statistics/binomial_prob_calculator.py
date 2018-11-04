#!/usr/bin/env python
"""This function calculates the probability of finding
k successes in n trials, given a probability of success of
p (arguments are int, int, float, respectively)."""

import sys

def main():
    #Load data
    n, k, p= int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    
    #Print calculation
    print(round(binomial(n,k,p),3))


def calc_factorial(k):
    """Calculates k factorial. If k=0, just
    returns 1."""
    
    if k==0:
        total_prod= 1
    
    else:
        total_prod= k
        while k >1:
            total_prod= total_prod*(k-1)
            k-=1
        
    return total_prod


def binomial(n,k,p_success):
    """Uses choose function to calculate the 
    probability of k successes in n events if p(success)
    equals p_success."""
    
    #Choose function terms
    numerator= calc_factorial(n)
    denominator= calc_factorial(k)*calc_factorial(n-k)
    
    #Multiplies terms by prob. of success and failure
    prob_success= (numerator/denominator)*(p_success**k)*(1-p_success)**(n-k)
    
    return prob_success

def calc_geom_prob(num_events, p_success):
    """Calculates the prob. of a success in exactly the num_events tries."""
    p_first= p_success*((1-p_success)**(num_events-1))
    return p_first

if __name__ == "__main__":
    main()