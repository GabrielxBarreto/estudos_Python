listas = []
i = 0
while 0 == 0:
    enter_value = input("Digite as notas (press F to finish):")
    if enter_value != "F" and enter_value != "f": 
        lista=float(enter_value)
        listas += [lista]
    else:
        break
media = sum(listas)/len(listas)
maior  = max(listas)
menor =  min(listas)
print(f"A média final foi:{media:.2f}\nA maior nota foi: {maior:.2f}\nA menor nota foi: {menor:.2f}")