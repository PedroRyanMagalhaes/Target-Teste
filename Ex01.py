
print ("Veirficando se o número pertence a Sequencia de FIBONACCI")
print("-"*30)
n = int (input("Digite um numero:  "))
fib1 = 0
fib2 = 1
numeroPertence = False


while fib2 <= n: #Enquanto o fib2 ser menor que o n ou igual o n tem chance do numero estar na sequencia quando ele ficar maior que 'n" signfica que nao tem como mais ele estar presente
    if fib2 == n:
        numeroPertence = True
        break
    x = fib1
    fib1 = fib2
    fib2 = x + fib2

if numeroPertence or n == 0:
    print (f"o numero {n} pertence a sequência")
else:
    print(f"o numero {n} não pertence a sequência")