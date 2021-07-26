"""
Initial-Value Problems for Ordinary Differential Equations
Implementation of the algorithms in chapter 5 of Numerical Analysis by Richard L. Burden and J. Douglas Faires
"""
import math
DEC = 6
intro = """
B I S E C T I O N   M E T H O D
-------------------------------

       2
Given x  - 4 * sin (x) 

        y
        | -----f(c)   .   f(x)
        |       .    
     ---|======c============ x 
        | a  .         b
        |  .  


        """
def getFatX(x):
    #res = pow(x,2) - 4 * math.sin(x)
    res = pow(x,5)-3*pow(x,4) + 2*pow(x,3) -pow(x,2)+x-3
    return res

def bisect(a,b,TOL):
    ans = -1
    TAB = "\t"
    i = 0
    print("i \t a \t f(a) \t \t b \t f(b) \t  c \t f(c) \t sign")
    print("---------------------------------------------------------------")
    while ((b-a)/2 > TOL): 
        sign = "-ve"
        c = (a+b)/2
        f_at_a = getFatX(a)
        f_at_b = getFatX(b)
        f_at_c = getFatX(c)
        if (f_at_c>0):
            sign = "+ve"
        print(i,  TAB, round(a,DEC), TAB, round(f_at_a,DEC), TAB, 
        round(b,DEC), TAB, round(f_at_b,DEC), TAB, round(c,DEC), round(f_at_c,DEC),TAB,
        sign)
        ans = c
        if (getFatX(c) == 0): 
            return ans

        if (getFatX(a) * getFatX(c) < 0): 
            b = c 
        else: 
            a = c 
        f_at_c = getFatX(c)
        i += 1
        if i > 100: 
            break; 
    return ans
#################################################################### main
def main():       #################
    a = 3         # THE VALUE a
    b = 5         # THE VALUE b
    TOL = 0.0001  # TOLERANCE
    print(intro)
    ans = bisect(a,b,TOL)
    print("----------------------------------------------")
    print("c =  %f, with f(c) = %f"%(ans,getFatX(ans)))

    msg = """
    
                                          b-a
        The error is given by  | xc - r | <  ------
                                          n+1
                                         2
        
        ==>

        %f  -  %f
        ----------
                %f + 1
                2
        
        = %f.
        """
    ans = (b-a)/2**4
    print(msg%(b,a,3,ans))
if __name__ == '__main__':
    main()
