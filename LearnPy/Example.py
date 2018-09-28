'''
Created on Sep 19, 2018

@author: Sutu_MeoLuoi
'''

#===============================================================================
# ******CLOSURE******
# **A closure is a function remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope
# **A function object remembers values in enclosing scopes regardless of whether those scopes are still present in memory
# **A functions that refer to variables from the scope in which they were defined
# **A function with an extended scope that encompasses nonglobal variables referenced in the body of the function 
# but not defined there. It does not matter whether the function is anonymous or not; what matters is that it can access nonglobal
# variables that are defined outside of its body. closures only matter when you have nested functions.
#===============================================================================

#===============================================================================
# a = [1, 2, 7, 9, 6]
# b = [3, 4]
# a.append(14) #add 14 to the same list
# a.extend(b)  #add b list to the same a list
# a = a + b    #create a new list joining old a and b
# a += b       #add b list to the same list. So, augmented assignment(iadd) is same ass extend()
#===============================================================================

#===============================================================================
# class Spam:
#     numInstances = 0
#     
#     def __init__(self):
#         Spam.numInstances = Spam.numInstances + 1
#         self.counter = 99
#     
#     def printNumInstances():
#         print("Number of instances created: %s" % Spam.numInstances)
#     
#     def printUnbound(self):
#         print('unbound {}', self.counter)
#         
# class Selfless:
#     def __init__(self, data):
#         self.data = data
#         
#     def selfless(arg1, arg2): # A simple function in 3.X
#         return arg1 + arg2
#     
#     def normal(self, arg1, arg2): # Instance expected when called
#         return self.data + arg1 + arg2
#===============================================================================

###### lambda TRAP!!!
## Expecting output: [2, 3, 4, 5, 6 ,7]; BUT print-out: [7, 7, 7, 7, 7, 7].
## I.e, expecting lambda closure to hold each x after each iteration, assume x going out of scope after each iteration
## Reason: each iteration creates an <function <listcomp>.<lambda> at 0x000000000222EBF8> object binding var 'x' to it. 
##         For loop never create new scope. 'x' belongs to enclosing scope of lambda(the scope where for loop belongs to),
##         so there is no closure in lambda. Closure only happens when var of local scope got encased into function object after that scope goes out
##         The function lambda objects got created with ref of 'x' of outer scope, so when outer scope call lambda obj, latest values of 'x'
##         got passed to lambda obj creates [7, 7, 7, 7, 7, 7].
## Note: for loop leak 'x' after loop finish while list comprehension doesn't. Thus, change x value after loop will change return of lambda.
##        However, changing x value after list comprehension, NOT change return value of lambda
##        Python 3, list comprehension creates own scope
## Ref: https://stackoverflow.com/questions/2295290/what-do-lambda-function-closures-capture/23557126
##        http://math.andrej.com/2009/04/09/pythons-lambda-is-broken/
##        https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
##        https://stackoverflow.com/questions/13905741/accessing-class-variables-from-a-list-comprehension-in-the-class-definition

lds = []
for x in range(6):
    lds.append(lambda: x + 2)
x = 10
print([ld() for ld in lds])

### assign x = 0 after list comprehension NOT change return value of lambda. Lambda got closure on x with the lastes value = 5 and 
### calculate to return 7 on every lambda object
### 
# lds = [lambda: x + 2 for x in range(6)]
# x = 10
# print([ld() for ld in lds])
# print(lds[0]())
# print(lds)

#===============================================================================
# ## list comprehension leak 'x' into outside scope in python 2. However, Python 3 fixed it.
# ## Thus, python 2 will print '6' and python 3 will error "name 'x' is not defined"
# ## Ref: https://stackoverflow.com/questions/4198906/python-list-comprehension-rebind-names-even-after-scope-of-comprehension-is-thi
# lds = [lambda: x + 2 for x in range(6)]
# print(x)
#===============================================================================
