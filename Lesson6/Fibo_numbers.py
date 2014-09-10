'''
Created on Sep 8, 2014

@author: Jason
'''

def fibonacci(n):
    a, b, i = 1, 0, 0
    while i < n:
        i += 1
        a, b = b, a+b
    return b




# 
print (fibonacci(0))
# #>>> 0
print (fibonacci(1))
# # #>>> 1
print (fibonacci(36))
# #>>> 14930352
print (fibonacci(80))
#>>> 23416728348467685