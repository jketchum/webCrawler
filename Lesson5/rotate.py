'''
Created on Sep 8, 2014

@author: Jason
'''

##Define a procedure that takes an input string and a value.  

def rotate(string, n):
    index = list(string) # separate the string into characters
    ord_index = []
    
    for e in string: # iterate through elements and assign new numerical value then convert to character.
        if e !=' ':
            ord_index.append(chr(ord('a') + (ord(e)+ n - ord('a'))% 26))
        else:
            ord_index.append(" ")

    return("".join(ord_index)) # joins the individual character elements back into a string



    
    # Your code here

print (rotate ('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate('dave',5))
#>>>'ifaj'
print (rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                 "sv rscv kf ivru kyzj"),-17))


