import random

palavras = ["santos","palmeiras","corinthians"]
sorteada = random.choice(palavras)

secreta = []
for i in sorteada:
    secreta.append("*")

while True:
    palavra_secreta = "".join(secreta)
    print(palavra_secreta)
    if palavra_secreta == sorteada:
        print("Você acertou!")
        break
    while True:
        chute = str(input('Dê o seu chute: '))
        if len(chute) > 1:
            print("digite só uma letra!")
            continue
        else:
            break
    for i in range(0, len(sorteada)):
        if chute == sorteada[i]:
            secreta[i] = chute