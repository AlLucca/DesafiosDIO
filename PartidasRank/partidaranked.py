vitorias = 0
derrotas = 0
saldo = vitorias - derrotas

def classificarRanked(vit, der):
    saldo = vit - der
    if(saldo >= 101):
        return "Imortal"
    elif(saldo >=91 and saldo <= 100):
        return "Lendário"
    
    elif(saldo >=81 and saldo <= 90):
        return "Diamante"   
    elif(saldo >=51 and saldo <= 80):
        return "Ouro"
    elif(saldo >=21 and saldo <= 50):
        return "Prata"
    elif(saldo >=11 and saldo <= 20):
        return "Bronze"
    else:
        return "Ferro"
    
print(f"O Herói tem de saldo de {saldo} está no nível de "+ classificarRanked(vitorias,derrotas))   
    

