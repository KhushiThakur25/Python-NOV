file = open('mysticker_2.png','rb')
data = file.read()
print(data)
file.close()

file = open('mysticker.png','wb')
file.write("jkdflsidhfwiudfhsuofhewuf")
file.close()