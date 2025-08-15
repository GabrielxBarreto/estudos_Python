def pertence(item,lista):
    if str(item) in str(lista):
        return True
    else:
        return False
    
itens = [1,"oi",3.14,7,True]
item  =  input("Qual o valor para pesquisa?")
print(pertence(item,itens))