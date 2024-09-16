#START
from random import choice

player1:str=input("enter player's name:");
player2:str=input("enter player's name:");
player3:str=input("enter player's name:");
player4:str=input("enter player's name:");
winner:str=choice([player1,player2,player3,player4]);
print(f"the winner is:{winner}");

#same question improved but not learned yet:
players:list=[];
for _ in range(4):
    player:str=input("enter player's name:");
    players.append(player)
winner:str=choice(players);
print(f"the winner is:{winner}")
#END