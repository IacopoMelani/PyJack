# coding=utf-8
import carta


class mazzo:

    mazzo = []

    def __init__(self, carte):
        self.mazzo = carte
        self.passate = []

    def __str__(self):
        s = ""
        for i in range(len(self.mazzo)):
            s = s + str(self.mazzo[i]) + "\n"
        return s

    def mischia(self):  #metodo per shuffle
        import random
        random.shuffle(self.mazzo)

    def passata(self, _carta):  #metodo per togliere carte pelate
        if isinstance(_carta, carta.carta):
            pos = 0
            for i in self.mazzo:
                if isinstance(
                        i, carta.carta):  #rimuovo da mazzo e metto in passate
                    if (i.seme == _carta.seme) and (i.valore == _carta.valore):
                        self.mazzo.remove(i)
                        self.passate.append(i)