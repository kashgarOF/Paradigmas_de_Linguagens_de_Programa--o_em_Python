def pergunta_sim_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in ("s", "uhum", "vamos", "sim"):
            return "sim"
        elif resposta in ("não", "nao", "n"):
            return "não"
        else:
            print('Não entendi sua resposta, por favor use "sim" ou "não"')


#codigo principal

nome = input('Ola, qual o seu nome? ')
print(f'Oi {nome}')

respostaTd = pergunta_sim_nao("Tudo bem contigo?")
if respostaTd == "sim":
    print('Que otimo, fico feliz!')
else:
    print('Poxa, vai dar tudo certo, você vai ver!')


respostaCv = pergunta_sim_nao('Vamos conversar um pouco ?')
if respostaCv == "sim":
    print("Massa!")
    hobby = input('O que gosta de fazer no tempo livre? ')
    print(f'Que legal, então você gosta de {hobby}')
else:
    print('Poxa :(')