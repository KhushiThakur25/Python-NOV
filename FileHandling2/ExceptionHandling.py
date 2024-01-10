try:
    num_1 = int(input("Enter the number1.."))
    num_2 = int(input("Enter the number2.."))

    add = num_1 + num_2
    

    sub = num_1 - num_2
    

    mul = num_1 * num_2
   

    div = num_1 / num_2
   

except ValueError :
    print("Invalid Input,Please enter the valid number")
except Exception as ex:
    print(ex)
else :
    print("Sum is",add)
    print("Sub is",sub)
    print("mul is",mul)
    print("div is",div)
finally:
    print("I'm always executed")