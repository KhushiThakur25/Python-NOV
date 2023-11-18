'''N1 = int(input("Enter the number.."))
N2 = int(input("Enter the number.."))
print(N1 +N2)'''

'''for i in range(start,stop,update):
    start = 0(by default)
    update = 1(by default)'''
'''for i in range(1,6,2):
    print("I'm in loop")
print("outside the loop")
for i in range(6,0,-1):
    print("hello",i)'''
'''0 1 2 3 4 
   * * * * *    0
   * * * * *    1
   * * * * *    2
   * * * * *    3
   * * * * *    4 '''
'''for i in range(5):
    for j in range(5):
        print("*",end="")
    print()'''
'''    
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
