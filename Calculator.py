
number_1 = float(input("Enter first number: "))
Operation = input("Enter desired operation: ")
number_2 = float(input("Enter second number: "))


def Add(number_1,number_2):
    result =(number_1 + number_2)
    return result

def Substract(number_1,number_2):
    result =(number_1 - number_2)
    return result

def Divide(number_1,number_2):
    result =(number_1 / number_2)
    return result

def Multiply(number_1,number_2):
    result =(number_1 * number_2)
    return result

if (Operation == "+"): 
    Answer = Add(number_1,number_2)
elif (Operation == "-"):
    Answer = Substract(number_1,number_2)
elif (Operation == "/"):
    Answer = Divide(number_1,number_2)
elif (Operation == "*"):
    Answer = Multiply(number_1,number_2)

print(Answer)