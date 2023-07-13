import sys

output = "concat(INS)"
insert = ""
for char in sys.argv[1]:
    insert += "char({})".format(ord(char))

print(output.replace("INS", insert))
    
