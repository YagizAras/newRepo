class myClass :
    def __init__(self, number):
        self.number = number

num1 = int(input("Choose number: "))
num2 = int(input("Choose number: "))

num3 = num1 * num2
print(num3)

if num3 % 2 != 0:
    print ("your number odd")
else :
     print ("your number even")

