num1 = input('first number: ')
operator = input('operator sign: ')
num2 = input('second number: ')

if(operator == '+'):print(int(num1) + int(num2))
elif(operator == '-'):print(int(num1) - int(num2))
elif(operator == '*'):print(int(num1) * int(num2))
elif(operator == '/'):print(int(num1) / int(num2))
else:print(int(num1) % int(num2))
