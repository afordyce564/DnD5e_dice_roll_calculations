import random

#The Die class simulates a die that can be rolled

class Die:

    #init__ method initializes the
    #sideup data attribute with a random number between 1 and 6
    #for now
    #later we will create an attrbute that initializes a data attribute which says
    #how many sides the die will have
    def __init__(self):
        self.__sides = 6
        self.__num = 0

    def get_sides(self):
        return self.__sides

    def roll(self):
        if random.randint(0,6) == 1:
            self.__num = 1
        if random.randint(0,6)== 2:
            self.__num = 2
        if random.randint(0,6)==3:
            self.__num =3
        if random.randint(0,6)==4:
            self.__num =4
        if random.randint(0,6)==5:
            self.__num = 5
        if random.randint(0,6)==6:
            self.__num = 6

        return self.__num

die = Die()
#print(die)