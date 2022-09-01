''' Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''
import time
humor = 50
fome = 50
sono = 50
saude = 50
idade = 0

print("==== Criado por Raphael Cunha (peguei o do amigo pq está muito bacana!!!)==== \n Cuide do seu bichinho virtual - 2022\n")
nome = input("Digite um nome para o seu bichinho: ")
print("{} está prestes a nascer".format(nome))
time.sleep(10)
print("Parabéns! Agora você poderá cuidar de {}".format(nome))
print("===========")
while True:
    
    print("O que você deseja fazer? \n 1 - Brincar \n 2 - Alimentar \n 3 - Dormir \n 4 - Dar remédio \n 5 - Criar novo bichinho")
    resp = int(input("Escolha: "))
    print("===========")
    
    """Brincar com o pet"""
    if resp == 1:
        humor += 3
        fome -= 3
        sono -= 2
        saude += 2
        print("===========")
        print("{} adorou brincar com você! :)".format(nome))
        print("{} agora está com: \n Humor = {} \n Fome = {} \n Sono = {} \n Saúde = {}".format(nome, humor, fome, sono, saude))
        print("===========")
    
    """Alimentar o pet"""
    if resp == 2:
        print("Com o que você deseja alimentar {}? \n 1 - Fruta \n 2 - Sanduíche \n 3 - Sorvete \n 4 - Frango".format(nome))
        resp_alimento = int(input("Escolha: "))
        if resp_alimento == 1:
            humor += 1
            fome += 3
            sono -= 3
            saude += 3
        if resp_alimento == 2:
            humor += 2
            fome += 3
            sono -= 5
            saude -= 2
        if resp_alimento == 3:
            humor += 3
            fome += 3
            sono -= 3
            saude -= 2
        if resp_alimento == 4:
            humor += 5
            fome += 8
            sono -= 6
            saude += 4
        print("===========")
        print("{} gosta de saber que você lhe dá comida :)".format(nome))
        print("{} agora está com: \n Humor = {} \n Fome = {} \n Sono = {} \n Saúde = {}".format(nome, humor, fome, sono, saude))
        print("===========")
    
    """Descansar o pet"""
    if resp == 3:
        print("ZzZz...")
        time.sleep(5)
        sono = 100
        if humor < 80:
            humor = 80
        else:
            humor = humor
        if fome < 80:
            fome = 80
        else:
            fome = fome
        if saude < 80:
            saude = 80
        else:
            saude = saude
        print("{} agora está com: \n Humor = {} \n Fome = {} \n Sono = {} \n Saúde = {}".format(nome, humor, fome, sono, saude))
        print("===========")
    
    """Medicar o pet"""
    if resp == 4:
        humor -= 5
        fome += 2
        sono += 5
        saude += 7
        print("===========")
        print("{} adora quando você lhe dá o devido cuidado :)".format(nome))
        print("{} agora está com: \n Humor = {} \n Fome = {} \n Sono = {} \n Saúde = {}".format(nome, humor, fome, sono, saude))
        print("===========")
    
    """Criar um novo pet"""
    if resp == 5:
        print("Você não pode mais interagir com {} :(".format(nome))
        print("Deseja criar um novo bichinho? \n 1 - Sim ou 2 - Não")
        resp_reset = int(input("Escolha: "))
        if resp_reset == 1:
            nome = input("Digite um nome para o seu bichinho: ")
            print("{} está prestes a nascer".format(nome))
            time.sleep(10)
            print("Parabéns! Agora você poderá cuidar de {}".format(nome))
            print("===========")
        if resp_reset == 2:
            print("Esperamos vê-lo de volta em breve :)")
            break
    
    """Condições de humor"""
    if humor == 100:
        print("Seu bichinho está muito feliz!")
    if humor < 20:
        print("Seu bichinho precisa de atenção! O humor de {} está muito baixo".format(nome))
    elif humor == 0:
        print("Seu bichinho precisa de atenção!")
    elif humor >= 101:
        humor = 100
    else:
        humor = humor
    
    
    """Condições de Fome"""    
    if fome == 100:
        print("Seu bichinho está satisfeito!")
    elif fome == 0:
        print("Seu bichinho precisa de atenção!")
    elif fome <= 20:
        humor -= 8
        fome -= 5
        sono -= 8
        saude -= 10
        print("Seu bichinho precisa de atenção! {} está com fome!".format(nome))
    elif fome >= 101:
        fome = 100
    else:
        fome = fome
        
    """Condições de sono"""
    if sono == 100:
        print("Seu bichinho está descansado!")
    if sono < 0:
        sono = 0
    elif sono == 0:
        print("Seu bichinho precisa de atenção!")
    elif sono <= 20:
        humor -= 7
        fome -= 2
        saude -= 3
        print("Seu bichinho precisa de atenção! {} está com sono e precisa descansar".format(nome))
    elif sono > 101:
        sono = 100
    else:
        sono = sono
    
    """Condições de saúde"""
    if saude == 100:
        print("Seu bichinho está saudável!")
    elif saude < 20:
        humor -= 8
        fome -= 5
        sono -=10
        print("Seu bichinho precisa de atenção! {} precisa de remédios".format(nome))
    elif saude == 0:
        print("Infelizmente {} morreu :(".format(nome))
        print("Deseja criar um novo bichinho? \n 1 - Sim ou 2 - Não")
        resp_reset = int(input("Escolha: "))
        if resp_reset == 1:
            nome = input("Digite um nome para o seu bichinho: ")
            print("{} está prestes a nascer".format(nome))
            time.sleep(10)
            print("Parabéns! Agora você poderá cuidar de {}".format(nome))
            print("===========")
        if resp_reset == 2:
            print("Esperamos vê-lo de volta em breve :)")
            break
    elif saude >= 101:
        saude = 100
    else:
        saude = saude
    if saude < 0 or fome < 0 or sono < 0:
        print("{} agora está com: \n Humor = {} \n Fome = {} \n Sono = {} \n Saúde = {}".format(nome, humor, fome, sono, saude))
        print("Infelizmente {} morreu :(".format(nome))
        print("Deseja criar um novo bichinho? \n 1 - Sim ou 2 - Não")
        resp_reset = int(input("Escolha: "))
        if resp_reset == 1:
            nome = input("Digite um nome para o seu bichinho: ")
            print("{} está prestes a nascer".format(nome))
            time.sleep(10)
            print("Parabéns! Agora você poderá cuidar de {}".format(nome))
            print("===========")
        if resp_reset == 2:
            print("Esperamos vê-lo de volta em breve :)")
            break
        
    

