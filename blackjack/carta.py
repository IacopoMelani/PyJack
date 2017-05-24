# coding=utf-8
class carta:

    ListaSemi = ["Fiori", "Quadri", "Cuori", "Picche"]
    ListaRanghi = [
        "Asso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Regina",
        "Re"
    ]

    seme = ""
    valore = ""

    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore
        #self.passata = False

    def __str__(self):
        return "seme: " + self.seme + " valore: " + self.valore + "\n"
