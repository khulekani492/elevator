#Project a simply elevator
#Aim manipulating strings based on the user input
#Author Khulekani Zondo DAte :02 May 2022



levels = ['floor10','floor8','floor7','floor6','floor5','floor4','floor3','floor2','floor1',]


def _elavator(floor,num):
    for i in floor:
        if int(i[5]) == num:
             print(i,"(*_*)",f"{user_name}")
             print("_" * 6)
        else:
             print(i)
             print("_"* 6)
             

# create a deck 
Card = []
numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]
cards = {'Red ':numbers,'Yellow ':numbers,'blue ':numbers,'green ':numbers}






special_cards = []
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      c = "+2" + i
      special_cards.append(c)
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      b = "REV_" + i
      special_cards.append(b)
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
    b = "SKIP^" + i
    special_cards.append(b)

print(special_cards)
#print(c)'''
  
   
    #return n


for k,v in cards.items():
        for i in v:
            a = [k , str(i)]
            Card.append(a)



user_name = input("Name: ")
num = int(input("Enter floor number: ")) 
_elavator(levels,num)



import random
rng = random.Random()
# create a deck 
Card = []
numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]
cards = {'Red ':numbers,'Yellow ':numbers,'blue ':numbers,'green ':numbers}

special_cards = []
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      c = "+2" + i
      special_cards.append(c)
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
      b = "REV_" + i
      special_cards.append(b)
for i in ['Red','RED','YELLOW','YELLOW','GREEN','GREEN','BLUE', 'BLUE']:
    b = "SKIP^" + i
    special_cards.append(b)

for i in range(1,5):
      wild_card = 'wild' + str(i)
      special_cards.append(wild_card)


for i in range(1,5):
      wild_card = 'wildraw' + str(i)
      special_cards.append(wild_card)
for k,v in cards.items():
        for i in v:
            a = [k , str(i)]
            Card.append(a)
Card.extend(special_cards)


#shuffle_the_card 
rng.shuffle(Card)
#print((Card))
# Games main logic 
Computer_hand = Card[1:8]
players_hand = Card[8:15] 


print('computer hand ',Computer_hand)
print('player_hand ',players_hand)

Discarded_pile = []
