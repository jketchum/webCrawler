'''
Created on Sep 8, 2014

@author: Jason
'''


def is_palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return (is_palindrome(s[1:-1]))
        return False
 
            

    
    
print (is_palindrome(''))
#>>> True
print (is_palindrome('abab'))
#>>> False
print (is_palindrome('abba'))
#>>> True
print(is_palindrome('andrea'))
#>>>False
print(is_palindrome('abaaba'))
#>>>True
    
    