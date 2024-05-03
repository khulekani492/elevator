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
             



user_name = input("Name: ")
num = int(input("Enter floor number: ")) 
_elavator(levels,num)