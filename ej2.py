import collections

var = """The constants defined in this module are:The constants defined in␣
this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
described below. This value is not locale dependent
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
locale-dependent and will not change.
"""

var = ''.join(filter(lambda letra: letra.isalnum() or letra.isspace(), var))
var = var.lower().split()

print (var)
print ("----")
print ("----")
var2 = collections.Counter(var)
print (var2)
print(var2.most_common(1))




