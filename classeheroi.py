nome = "Nome"
xp = 0
classe = "Ferro"

if xp >= 10001:
    classe = "Radiante"
elif xp >= 9001 and xp <=10000:
    classe = "Imortal"
elif xp >= 8001 and xp <=9000:
    classe = "Ascendente"
elif xp >= 7001 and xp <=8000:
    classe = "Platina"
elif xp >= 5001 and xp <=7000:
    classe = "Ouro"
elif xp >= 2001 and xp <=5000:
    classe = "Prata"
elif xp >= 1001 and xp <=2000:
    classe = "Bronze"

print("O Herói de nome "+ nome +" está no nivel de "+ classe +".")