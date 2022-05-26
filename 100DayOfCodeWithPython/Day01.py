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

factorial(4)

# solution using recursion and time complexity of O(n)
def factorialRecursion(num):
    # return the recursion when base case is reached to stop infinite loop
    if num == 1:
        return num
    return num * factorialRecursion(num-1) #this line is basically 4! = 4 * 3!
        

factorialRecursion(4)


# Question 3
    # With a given integral number n, write a program to generate a dictionary that contains 
    # (i, i x i) such that is an integral number between 1 and n (both included). and then 
    # the program should print the dictionary.Suppose the following input is supplied to the
    #  program: 8 Then, the output should be:

    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def dictionary(num):
    ans = {}
    for i in range(1, num+1):
        ans[i] = i*i
    return ans

print(dictionary(8))

# Using dictionary Comprehension
def dictionaryComprehension(num):
    ans = {i: i*i for i in range(1, num+1)}
    print(ans)

dictionaryComprehension(8)

# Using while loop
def dictionaryWhile(num):
    ans = {}
    i = 1
    while i < num+1:
        ans[i] = i*i
        i+=1
    return ans

print(dictionaryWhile(8))

