class mazziere:

     def __init__(self):
        self.somma = 0
        self.carte = []
        self.punti = []


    def __str__(self):
        s = ""
        for i in range(len(
                self.carte)):  #ciclo per stampare tutte le carte del giocatore
            s = s + str(self.carte[i]) + "\n"
        s = s + "\n\n somma carte: " + str(self.somma)
        return s

		
	def riceviCarta(self, _carta, _mazzo):

        ListaValori = {
            "Asso": (1, 11),
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 10,
            "Regina": 10,
            "Re": 10
        }

        if isinstance(_carta, carta.carta):
            valoreAsso = 11
            if _carta.valore == "Asso":  #controllo se la carta è un Asso
                if (
                        self.somma + 11
                ) > 21:  #se somma è maggiore di 21 asso = 1 altrimenti continua
                    valoreAsso = 1

                else:
                    self.carte.append(
                        _carta)  #inserimento carta con valore a somma

                    self.somma = self.somma + valoreAsso

                    self.punti.append(
                        valoreAsso)  #salvo punti per futuri controllo assi

                    _mazzo.passata(_carta)  #tolgo carta pelata
            else:
                self.carte.append(
                    _carta)  #inserimento carta con valore a somma

                _mazzo.passata(_carta)  #tolgo carta pelata

                self.somma = self.somma + ListaValori[
                    _carta.
                    valore]  #aggiungo a somma il valore corrispondente alla lista di valori

                self.punti.append(
                    ListaValori[_carta.valore]
                )  #salvo il valore passato per un futuro controllo su Assi

        _mazzo.passata(_carta)  #chiamata metodo per togliere carta

    def stai(self):  #sono uguali, solo per ordine mentale
        return self.somma

    def controlloSomma(self):
        return self.somma

    def controlloBlackJack(self):  #controllo per blackjack iniziale
        if self.somma == 21:
            return True
        else:
            return False

    def controlloAssi(self):  #controllo su cambio valore assi
        if self.somma > 21:
            cont = 0
            for i in range(len(self.punti)):
                if self.somma < 21:
                    break  #se minore non continuo a cambiare valori
                if self.punti[i] == 11:
					cont += 1
					self.somma = self.somma - 10
					self.punti[i] = 1