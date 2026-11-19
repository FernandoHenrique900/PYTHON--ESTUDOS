# FizzBuzz program
#exercicio FizzBuzz que imprima os numeros de 1 a 50, mas para os multiplos de 3 imprima "Fizz" e para os multiplos de 5 imprima "Buzz" e para os multiplos de 3 e 5 imprima "FizzBuzz"

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)    