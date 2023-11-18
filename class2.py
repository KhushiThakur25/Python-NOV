'''import time

print("Hello",flush="True")
time.sleep(5)
print("Bye")'''

a,b = 3,6
c= a+b
#%d int - use in c
print("Sum is %d"%c)
print("Sum of",a,"and",b,"is",c)
print("Sum of %d and %d is %d"%(a,c,b))
print("Sum is {}".format(c))
print("Sum of {0} and {2} is {1}".format(a,c,b))
#f-string method
print(f"Sum of {a} and {b} is {c}")




