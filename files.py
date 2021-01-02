ref1 = open("/home/liam/Documents/Code/Python Learning/reference.txt", "r")

print(ref1.read())

ref1.close()

ref2 = open("/home/liam/Documents/Code/Python Learning/reference3.txt", "a+")
ref2.write("\n" + input("input something: "))
print(ref2.readable())
print(ref2.read())
ref2.close()
