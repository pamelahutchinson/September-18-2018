
Fizz_Buzz = int(input("Please enter desired number: "))

def divisible(Fizz_Buzz):

    if(Fizz_Buzz % 3 == 0 and Fizz_Buzz % 5 == 0):
        print("Fizz Buzz")
    elif(Fizz_Buzz % 3 == 0):
        print("Fizz")
    elif(Fizz_Buzz % 5 == 0):
        print("Buzz")
   

divisible(Fizz_Buzz)

