# Quetion 1
    #Write a program which will find all such numbers which are divisible by 7 but 
    # are not a multiple of 5, between 2000 and 3200 (both included).The numbers 
    # obtained should be printed in a comma-separated sequence on a single line.

for item in range(2000, 3201):
    if item % 5 != 0 and item % 7 == 0:
        print(item, end=", ")
print('\n')


#  Question 2
    # Write a program which can compute the factorial of a given numbers.The results 
    # should be printed in a comma-separated sequence on a single line.Suppose the 
    # following input is supplied to the program: 8 Then, the output should be:40320


# Solution using for loop and time complexity Of O(n) where n is number of loop
def factorial(num):
    # let (ans) as a storing value of multiplication in each iteration
    ans = 1
    # iterate through 1 to num+1(we are taking 4) therefore we iterate till i become 4
    for i in range(1, num+1):
        ans *= i
    return ans
# solution using recursion and time complexity of O(n)
def factorialRecursion(num):
    # return the recursion when base case is reached to stop infinite loop
    if num == 1:
        return num
    return num * factorialRecursion(num-1) #this line is basically 4! = 4 * 3!
        

print(factorialRecursion(4))


