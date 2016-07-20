#Retrieved from cuLearn: https://www.carleton.ca/culearn/. (Summer 2016).
#
#Howard, N., "Lecture Notes for Comp1405A -  Introduction to functions [PDF Document]
#Retrieved from cuLearn: https://www.carleton.ca/culearn/. (Summer 2016)
#
#Howard, N., "Lecture Notes for Comp1405B -  Advance List [PDF Document]
#Retrieved from cuLearn: https://www.carleton.ca/culearn/. (Summer 2016)
#
#Howard, N., "Lecture Notes for Comp1405B -  Strings [PDF Document]
#Retrieved from cuLearn: https://www.carleton.ca/culearn/. (Summer 2016)
#
#Howard, N., "Lecture Notes for Comp1405B -  File [PDF Document]
#Retrieved from cuLearn: https://www.carleton.ca/culearn/. (Summer 2016)
#






#gets user input making sure it isnt a floating point number
try:

    usrinput = int(input("Please enter an integer that you would like to find"))

except:

    usrinput = int(input("Incorrect input please make sure you enter an integer not a floating point number."))
#calculates factorial based on user input
def factorial (usrinput):

    mn = 1
    
    for i in range (1,usrinput+1):
        #multiplies the sum times the current number
        mn = i*mn
    #returns the sum of the factorial
    return mn

def combination (n,k):
    #using the factorial formula for combination
    combo = factorial(n)/(factorial(k)*factorial(n-k))
    combo = int(combo)
    return combo

#the triangle
def main(usrinput):
    #creates a flag
    flag = False
    
    triangle = ""
    row = 0
    while True:
        #loops through out the current row
        for i in range (0, row + 1):
            #calls the combination function to get the value at the row, position
                combin = combination(row, i)
                
                #adds the value to the string for the table
                triangle = triangle + str(combin) + " "
                #checks the value that the user typed to see if it was found
                if usrinput == combin:
                    flag=True
        

        print(triangle.center(73))

        if flag==True:
            break
        #increases the number of rows
        row = row + 1
        triangle = ""

main(usrinput)