import random
import os
import time


def s_cleaner ():                #
    if os.name == 'nt':          #
        os.system("cls")         #       <--     limpa o terminal para não poluir
    else:                        #
        os.system("clear")       #


def show_menu ():
    print ("_____________________________ Pow Pow _____________________________")
    print ("|================== Hora de acertar as contas... =================|")
    print ("|=================================================================|")
    print ("|_______________                ___                _______________|")
    print ("|              /|            __|___|__             \\              |")
    print ("|             / |             (|o o|)          ________.          |")
    print ("|            /  |             _\\~^~/_________~(_]----'            |")
    print ("|           /   |            / /\\__/\\ ———————/_)    | \\           |")
    print ("|          /    |           /  }O  O{               |  \\          |")
    print ("|         /  /  |           \\  \\    /               |   \\         |")
    print ("|        /  /|  |            \\/ |  | \\              |    \\        |")
    print ("|       /  / |  |            / /(\\/)\\ \\             |     \\       |")
    print ("|———————  /  |  |           / /      \\ \\            |      ———————|")
    print ("|     /| /   |  |         (_||        ||_)          | |\\     |    |")
    print ("|    / | |   |  |            \\|  /\\  |/             | | \\    |    |")
    print ("|   /  | |   /  |             | |——| |              | |\\|    |    |")
    print ("|  /   | |  /   /             | |  | |              \\ |||    |    |")
    print ("| /    | | /   /              | |  | |               \\|\\|    |    |")
    print ("|/     | |/   /               |_|  |_|                \\ |    |    |")
    print ("|      |     /                /_\\  /_\\                 \\|    |    |")
    print ("|______|____/___________________________________________\\____|____|")

    print("                       Escolha seu caminho:")
    print("-------------------------------------------------------------------")
    print("                          1 - Jogar")
    print("                          2 - Como jogar")
    print("                          0 - Sair\n")

    while True:

        try:

            main_menu_choice = int(input().strip("!., "))

            if main_menu_choice == 1:
                return 'play'

            elif main_menu_choice == 2:
                return 'how_to_play'

            elif main_menu_choice == 0:
                return 0

            else:
                print('Insira um número válido\n')
            
        except ValueError:
            print("Insira um número inteiro\n")

def show_status():
    s_cleaner()
    print("__________________________________________________________________")
    print(f"| Vidas: {player['vidas']}            <-- Você | Inimigo -->            Vidas: {enemy['vidas']} |")
    print("|----------------------------------------------------------------|")
    print(f"| Balas no tambor: {player['atirar']}           |              Balas no tambor: {enemy['atirar']} |")
    print(f"| Esquivas: {player['defender']}                  |                     Esquivas: {enemy['defender']} |")
    print("|______________________________|_________________________________|")
    print()


def generate_machine_input():

    pesos = {
        "atirar": 1 + historico["recarregar"],
        "defender": 1 + historico["atirar"],
        "recarregar": 1 + historico["defender"],
    }

    if enemy["atirar"] == 0:
        pesos["atirar"] = 0

    if enemy["defender"] == 0:
        pesos["defender"] = 0
        
    if enemy["vidas"] == 1:
        pesos["recarregar"] //= 3
        if pesos["recarregar"] < 1:
            pesos["recarregar"] = 1

    return random.choices(list(pesos.keys()), weights=list(pesos.values()))[0]


def receive_player_input():

    while True:

        try:

            print("______________________")
            print("| Qual a sua jogada? |")
            print("|   1 - Atirar       |")
            print("|   2 - Defender     |")
            print("|   3 - Recarregar   |")
            print("----------------------")
            player_input = int(input().strip("!., "))

            if player_input == 1:

                if player["atirar"] > 0:
                    return 'atirar'
                
                else:
                    show_status()
                    print("Sem munição!")

            elif player_input == 2:

                if player["defender"] > 0:
                    return 'defender'
                
                else:
                    show_status()
                    print("Não tem mais onde se esconder!")

            elif player_input == 3:
                return 'recarregar'
            
            else:
                show_status()
                print("Fale certo!! (Insira um dos números na lista)1")

        except ValueError:
            show_status()
            print("Ocê é doido ou se faz?! (Insira um número)")

def recarregar(entity):
    if entity["atirar"] < 3:
        entity["atirar"] += 1
    entity["defender"] = 2


def show_animation(player_input, machine_input):
    p_shoot =[
        '                                 ',
        '                                 ',
        '  _                              ',
        '_|_|_    ______,                 ',
        ' ( )___~(_]""""                  ',
        ' /|   /_)                        ',
        ' \\|                              ',
        ' / \\                             ',
        '/   \\                            ',
        '_________________________________',
 
    ]
    e_shoot =[
        '                                 ',
        '                                 ',
        '                              _  ',
        '                 ,______    _|_|_',
        '                  """"[_)~___( ) ',
        '                       (_\\    |\\ ',
        '                              |/ ',
        '                             / \\ ',
        '                            /   \\',
        '_________________________________',
    ]
    p_shooted =[
        '  __/                             ',
        ' /_/                             ',
        '  /                              ',
        '                                 ',
        '( )__/                           ',
        ' /\\                              ',
        ' \\ \\___                          ',
        '    \\  \\                         ',
        '    /                            ',
        '_________________________________',
 
    ]
    e_shooted = [
        '                            \\__  ',
        '                             \\_\\ ',
        '                              \\  ',
        '                                 ',
        '                           \\__( )',
        '                              /\\ ',
        '                          ___/ / ',
        '                         /  /    ',
        '                            \\    ',
        '_________________________________',
    ]

    p_reload = [
        '                                 ',
        '                                 ',
        '   _                             ',
        ' _|_|_                           ',
        '  ( )                            ',
        '   /|\\                           ',
        ' _/ |/                           ',
        '/  / \\                           ',
        '  /   \\                          ',
        '_________________________________',
    ]

    e_reload = [
        '                                 ',
        '                                 ',
        '                             _   ',
        '                           _|_|_ ',
        '                            ( )  ',
        '                           /|\\   ',
        '                           \\| \\_ ',
        '                           / \\  \\',
        '                          /   \\  ',
        '_________________________________',
    ]
    p_defesa = [
        '                                 ',
        '                                 ',
        '                                 ',
        '    v                            ',
        ' v  _  v                         ',
        '  _|_|_                          ',
        ' |_( )/                          ',
        '   /\\/                           ',
        '  (\\                             ',
        '__/_\\____________________________',
    ]

    e_defesa = [
        '                                 ',
        '                                 ',
        '                                 ',
        '                            v    ',
        '                         v  _  v ',
        '                          _|_|_  ',
        '                          \\( )_| ',
        '                           \\/\\   ',
        '                             /)  ',
        '____________________________/_\\__',
    ]
    b_shoot =[
        '                                                                  ',
        '                                                                  ',
        '  _                                                            _  ',
        '_|_|_    ______,                                  ,______    _|_|_',
        ' ( )___~(_]""""                 =|=                """"[_)~___( ) ',
        ' /|   /_)                                               (_\\    |\\ ',
        ' \\|                                                            |/ ',
        ' / \\                                                          / \\ ',
        '/   \\                                                        /   \\',
        '__________________________________________________________________',
    
    ]

    waiting3 =[
        '                                                                  ',
        '                                                                  ',
        '     _                                                      _     ',
        '   _|_|_                                                  _|_|_   ',
        '    ( ) )                                                ( ( )    ',
        '    /|\\/                           ___                    \\/|\\    ',
        '    \\|                            /##\\\\                     | \\   ',
        '    / \\                          |\\#@/#|                   / \\    ',
        '   /   \\                          \\###/                   /   \\   ',
        '__________________________________________________________________',
    
    ]

    waiting2 =[
        '                                                                  ',
        '                                                                  ',
        '     _                                                      _     ',
        '   _|_|_                                                  _|_|_   ',
        '    ( ) )                                                ( ( )    ',
        '    /|\\/                                                  \\/|\\    ',
        '    \\|                            ___                       | \\   ',
        '    / \\                          /###\\                     / \\    ',
        '   /   \\                        |#/@#\\|                   /   \\   ',
        '_________________________________\\\\##/____________________________',
    
    ]

    waiting1 =[
        '                                                                  ',
        '                                                                  ',
        '     _                                                      _     ',
        '   _|_|_                                                  _|_|_   ',
        '    ( ) )                                                ( ( )    ',
        '    /|\\/                         ___                      \\/|\\    ',
        '    \\|                          /##\\\\                       | \\   ',
        '    / \\                        |\\#@/#|                     / \\    ',
        '   /   \\                        \\###/                     /   \\   ',
        '__________________________________________________________________',
    
    ]
    
    show_status()
    print(f"     {player_input:>10}               3...                                ")
    for linha in waiting3:
        print(linha)
    time.sleep(0.5)

    show_status()
    print(f"     {player_input:>10}               2...                                ")
    for linha in waiting2:
        print(linha)
    time.sleep(0.5)

    show_status()
    print(f"     {player_input:>10}               1...                                ")
    for linha in waiting1:
        print(linha)
    time.sleep(0.5)

    show_status()
    print(f"     {player_input:>10}                                    {machine_input:>10}     ")
    time.sleep(0.5)

    if player_input == 'atirar':

        if machine_input == 'atirar':
            for linha in b_shoot:
                print(linha)

        elif machine_input == 'defender':
            for i in range(10):
                print(p_shoot[i]+e_defesa[i])

        elif machine_input == 'recarregar':
            for i in range(10):
                print(p_shoot[i]+e_shooted[i])
    
                
    elif player_input == 'defender':
        if machine_input == 'atirar':
            for i in range(10):
                print(p_defesa[i]+e_shoot[i])

        elif machine_input == 'defender':
            for i in range(10):
                print(p_defesa[i]+e_defesa[i])

        elif machine_input == 'recarregar':
            for i in range(10):
                print(p_defesa[i]+e_reload[i])

    elif player_input == 'recarregar':
        if machine_input == 'atirar':
            for i in range(10):
                print(p_shooted[i]+e_shoot[i])

        elif machine_input == 'defender':
            for i in range(10):
                print(p_reload[i]+e_defesa[i])

        elif machine_input == 'recarregar':
            for i in range(10):
                print(p_reload[i]+e_reload[i])

    time.sleep(2)

def rodada():
    show_status()
    machine_input = generate_machine_input()
    player_input = receive_player_input()
    show_animation(player_input, machine_input)

    
    if player_input != 'recarregar' and machine_input != 'recarregar':
        player[player_input] -= 1
        historico[player_input] += 1
        enemy[machine_input] -= 1

    else:
        if player_input == 'recarregar':
            recarregar(player)
            historico["recarregar"] += 1
            if machine_input == "recarregar":
                recarregar(enemy)
            elif machine_input == "atirar":
                enemy['atirar'] -= 1
                player['vidas'] -= 1
            elif machine_input == "defender":
                enemy["defender"] -=1

        elif machine_input == 'recarregar':
            recarregar(enemy)
            if player_input == 'atirar':
                player["atirar"] -= 1
                enemy["vidas"] -= 1
                historico["atirar"] += 1
            elif player_input == 'defender':
                player["defender"] -= 1
                historico["defender"] +=1

def show_how_to_play():
    i = 1
    while True:
        s_cleaner()
        voltar = 1
        print("====================== POW-POW: O JOGO ======================")
        print("|                                                           |")
        print("|  Você e a máquina são dois pistoleiros frente a frente,   |")
        print("|  cada um com vidas, balas no tambor, esquivas e recarga.  |")
        print("|                                                           |")
        print("|   A cada rodada, os dois escolhem em segredo uma ação:    |")
        print("|              ATIRAR, DEFENDER ou RECARREGAR.              |")
        print("|   Ninguém sabe a jogada do outro até serem reveladas.     |")
        print("|                                                           |")
        print("|              COMO CADA CONFRONTO FUNCIONA:                |")
        print("|                                                           |")
        print("|  Atirar x Atirar -> os dois gastam uma bala, sem dano.    |")
        print("|  Atirar x Defender -> atirador gasta bala,                |")
        print("|  defensor gasta esquiva.                                  |")
        print("|  Defender x Defender -> os dois gastam uma esquiva.       |")
        print("|  Recarregar x Recarregar -> esquivas voltam ao máximo     |")
        print("|  e cada um ganha uma bala extra.                          |")
        print("|  Recarregar x Defender -> quem recarregou recupera        |")
        print("|  esquivas e ganha bala extra; defensor gasta esquiva.     |")
        print("|  Recarregar x Atirar -> quem recarregou perde uma vida,   |")
        print("|  mas recupera esquivas e ganha bala; atirador gasta bala  |")
        print("|                                                           |")
        print("|  Sem balas não dá pra atirar. Sem esquivas não dá         |")
        print("|  pra defender. Recarregar sempre está disponível.         |")
        print("|                                                           |")
        print("|     O jogo acaba quando alguém perde todas as vidas.      |")
        print("|   Vidas só se perdem no confronto Recarregar x Atirar.    |")
        print("|                                                           |")
        print("=============================================================")
        if i %2 == 0 and voltar != '0':
            voltar = input("INSIRA 0 PARA VOLTAR:\n")
        else:
            voltar = input("Insira 0 para voltar:\n")
        if voltar == '0':
            return
        i += 1

################################## loop principal do jogo ##################################
while True:
    s_cleaner()
    option = show_menu()
    if option == 0: # encerra o jogo
        exit()      #

    elif option == 'how_to_play':
        show_how_to_play()

    elif option == 'play':
        historico = {
            "atirar": 0,
            "defender": 0,
            "recarregar": 0,
        }

        #set inicial (recarregar está implicito porque sempre têm valor 1)
        player = {
            "vidas": 2,
            "atirar": 1,
            "defender": 2,
        }

        enemy = {
            "vidas": 2,
            "atirar": 1,
            "defender": 2,
        }
        while player['vidas'] > 0 and enemy['vidas'] > 0:
            rodada()
        if player["vidas"] == 0:
            show_status()
            print('Você perdeu!')
        else:
            show_status()
            print("Você ganhou!")
        time.sleep(3)
