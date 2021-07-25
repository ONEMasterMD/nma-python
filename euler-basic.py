import math
#######################################################
# (c) Copyright  ONEMasterMD - 2021Jul25              #
#######################################################
"""
EULER METHOD
"""
intro = """

"""

def getFPrime(x,y):
    fprimeatp =  (1*x) #-1/2*(math.sqrt(x+3))
    #fatp = 3*x*x*x*x+ 21/2*x*x*x + 12*x*x+9/2*x
    #fatp = x*x-math.sqrt(x+3)-25.11
    #fprimeatp = 12*x*x*x + 63*x*x/2+24*x+9/2 
    return fprimeatp

def doEuler(x,y,to_approx_at_x,steps_h ):

    print ("n   |   xn     |    yn      |       F'atp")
    print ("------------------------------------------------------")
    i = 0
    while (i<14):
        if (x>to_approx_at_x): 
            print ("------------------------------------------------------")
            yn_plus_one = y - steps_h*fprimeatp
            break  
        fprimeatp = getFPrime(x,y)
        yn_plus_one = y + steps_h*fprimeatp

        print (i,'\t',x,'\t',y,'\t\t',fprimeatp)
        i += 1
        x = round(x+steps_h,3)
        y = round(yn_plus_one,3)

    return yn_plus_one
 
def main():
    to_approx_at_x = 1      # TO APPR. AT THIS VALUE
    initial_x = 0           #  x0
    initial_y = 1           #  y0
    steps_h = 0.1           # h

    intro = """
    Given: 

        initial_x = %.3f
        initial_y = %.3f
        steps_h = %.3f 

        required to approx_at_x = %.3f

        using Euler's method.

        i.e. 

        -------------------------------------
        |                                   |
        |   y   =  y     + h * f'(x,y)      |
        |    n+1    n                       |
        -------------------------------------


    """

    print (intro%(initial_x,initial_y,steps_h,to_approx_at_x))
    ans = doEuler(initial_x,initial_y,to_approx_at_x,steps_h )

    conclusion = """
        hence, the solution is
        (x , y) = (%.4f,%.4f)
    """
    print(conclusion%(to_approx_at_x,ans))
if __name__ == '__main__':
    main()
