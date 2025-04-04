num1 = int(input("write the first number: "))
num2 = int(input("Write the second number: "))
op = str(input("enter the operation e.g(+, -, *, / )"))
if op == "+":
    result = num1+num2
    print(num1, ("+"), num2, ("="), result)
elif op == "-":
    result = num1-num2
    print(num1, ("-"), num2, ("="), result)
elif op == "*":
    result = num1*num2
    print(num1, ("*"), num2, ("="), result)
else:
    result=num1/num2
    print(num1, ("/"), num2, ("="), result)