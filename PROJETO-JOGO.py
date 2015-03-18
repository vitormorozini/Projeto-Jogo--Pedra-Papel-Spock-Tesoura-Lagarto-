# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:34:43 2015

@author: vitor_000
"""
import random
list=['pedra','papel','tesoura','lagarto','spock']
jogar=True
while jogar==True:
    jogar=False
    player_computer=0
    player=0
    while player < 3 and player_computer < 3:
        pc=random.choice(list)
        jogador=str(input('Insira a sua opção de jogada:'))
        jogador = jogador.lower()
        print('O computador já selecionou a opção de jogada')
        
        if pc == 'pedra' and (jogador == 'tesoura' or jogador == 'lagarto'):
            player_computer += 1
            print('O computador venceu a rodada!', player_computer, ', Jogador ' ,player)
        elif jogador == 'pedra' and (player_computer == 'tesoura' or player == 'lagarto'):
            player += 1
            print('Você ganhou a rodada!', player_computer ,', Jogador ' ,player)
        elif player_computer == 'tesoura' and (jogador == 'papel' or jogador == 'lagarto'):
            player_computer += 1
            print('O computador venceu a rodada!', player_computer ,', Jogador ' ,player)
        elif jogador == 'tesoura' and (pc == 'papel' or pc == 'lagarto'):
            player += 1
            print('Você ganhou a rodada!' ,player_computer ,', Jogador ' ,player)
        elif pc == 'papel' and (jogador == 'pedra' or jogador == 'spock'):
            player_computer += 1
            print('O computador venceu a rodada!' ,player_computer ,', Jogador ' ,player)
        elif jogador == 'papel' and (pc == 'pedra' or pc == 'spock'):
            player += 1
            print('Você ganhou a rodada!' ,player_computer ,', Jogador ' ,player)
        elif pc == 'lagarto' and (jogador == 'spock' or jogador == 'papel'):
            player_computer += 1
            print('O computador venceu a rodada!' ,player_computer ,', Jogador ' ,player)
        elif jogador == 'lagarto' and (pc == 'spock' or jogador == 'papel'):
            player += 1
            print('Você ganhou a rodada!' ,player_computer ,', Jogador ' ,player)
        elif pc == 'spock' and (jogador == 'tesoura' or jogador == 'pedra'):
            player_computer += 1
            print('O computador venceu a rodada!' ,player_computer ,', Jogador ' ,player)
        elif jogador == 'spock' and (pc == 'tesoura' or pc == 'pedra'):
            player += 1
            print('Você ganhou a rodada!' ,player_computer ,', Jogador ' ,player)
        elif jogador == pc:
            print('Empate! \n Computador ',player_computer ,', Jogador ' ,player)
        else:
            print('Erro! Insira corretamente o seu comando (tesoura,lagarto,spock,papel,pedra)')
        if player_computer == 3:
            print('Tente novamente.O computador venceu! Resultado: Computador ' ,player_computer ,', Jogador ' ,player)
    else:
        print('Parabéns, você ganhou! Resultado: Computador ' ,player_computer ,', Jogador ' ,player)
    pl = str(input('Deseja jogar novamente?'))
    pl = pl.lower()
    if pl == 'sim':
        jogar = True
    else:
        jogar = False