def hash_string(keyword,buckets):
    string = []
    location = 0
    
    for chr in keyword:
        string.append(chr)
    for e in string:
        location += ord(e)
    location = location % buckets
        
    return location

        





print (hash_string('a',12))
#>>> 1

print (hash_string('b',12))
#>>> 2

print(hash_string('a',13))
#>>> 6

print (hash_string('au',12))
#>>> 10

print (hash_string('udacity',12))
#>>> 11
