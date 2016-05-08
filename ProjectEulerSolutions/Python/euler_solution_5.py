#############################################################################################################
# Project Euler Problem 5
#
# By Mike Kane
#
# # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
#############################################################################################################

def getAnswer():
    '''
        If answer is evenly divisible by all numbers 1 - 20, then it is also divisible
        by all numbers 1 - 10.  Therefore, answer is a multiple of 2520

        1) let x = 2520.
        2) iterate through 11-20 checking to see if x is evenly divisible.
            --if yes, return answer.
            -- if no, x += 2520
        3) repeat step 2
    '''

    x = 5040
    i = 11
    while i < 21:
        if x % i == 0:
            i += 1
        else:
            x += 2520
            i = 11

    return x

if __name__ == "__main__":
    print(getAnswer())

#answer == 232792560
