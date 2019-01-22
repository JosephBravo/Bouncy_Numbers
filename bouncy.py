
print ("BOUNCY NUMBERS PROPORTION")

def bouncy_number(num):
    num_increment, num_descrement = False, False
    next_digit = num % 10 #Aqui identificamos el ultimo digito del numero
    num = num // 10  #Residuo del numero

    while num > 0:
        before_digit = num % 10   #identificamos el digito penultimo del numero a partir del residuo
        if before_digit < next_digit:   #comparamos los digitos penultimo < ultimo
            num_increment = True       #declaramos el numero en estado de incremento
        elif before_digit > next_digit:  #comparamos los digitos penultimo > ultimo
            num_descrement = True   #declaramos el numero en estado de decremento
        next_digit = before_digit
        num = num // 10
        if num_increment and num_descrement: #cuando un numero incrementa pero tambien decrementa
            return True
    return False

# Comparacion los numeros hasta que el recuento inflable es del 90% y 99%

count = 0
p = 90
while count < 0.90 * p:
    p = p + 1
    if bouncy_number(p):
        count = count + 1
print ("The number where proportion of bouncy numbers is equal to 90%:", + p)


count = 0
p = 99
while count < 0.99 * p:
    p = p + 1
    if bouncy_number(p):
        count = count + 1
print ("And the proportion of bouncy number is equal to 99% in:", + p)
