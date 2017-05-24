# coding=utf-8
import carta
import mazzo
import giocatore
import mazziere

ListaSemi = ["Fiori", "Quadri", "Cuori", "Picche"]
ListaRanghi = [
    "Asso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Regina",
    "Re"
]

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


def distribuisciIniziale(_mazzo, _giocatore, _mazziere):  #metodo distribuzione carte
    if isinstance(_mazzo, mazzo.mazzo):  #controllo sulle instanze di classe
        if isinstance(_giocatore, giocatore.giocatore):
            for i in range(2):
                _giocatore.riceviCarta(_mazzo.mazzo[i], _mazzo)


def distribuisciCarta(_mazzo, _giocatore):  #metodo "carta"
    if isinstance(_mazzo, mazzo.mazzo):  #controllo sulle instanze di classe
        if isinstance(_giocatore, giocatore.giocatore):

            _giocatore.riceviCarta(_mazzo.mazzo[0],
                                   _mazzo)  #distribuisci la prima carta


def stai(_giocatore):
    if isinstance(
            _giocatore, giocatore.
            giocatore):  #comunica di stare e chide di far ritornare risultato
        risultato = _giocatore.stai()
        return risultato


def controlloSomma(_giocatore):  #ritorno della somma del giocatore
    if isinstance(_giocatore, giocatore.giocatore):
        somma = _giocatore.controlloSomma()
        return somma


def controlloBlackJack(_giocatore):  #esito blackjack iniziale
    if isinstance(_giocatore, giocatore.giocatore):
        esito = _giocatore.controlloBlackJack()
        return esito


def menu(_giocatore, _mazzo, _mazziere):  #menu -> da riordinare(forse)
    if isinstance(_mazziere, mazziere.mazziere):   
        if isinstance(_giocatore, giocatore.giocatore):
            if isinstance(_mazzo, mazzo.mazzo):

                distribuisciIniziale(_mazzo,
                                    _giocatore)  # distribuzione carte iniziale

                print "\n %s \n" % _giocatore

                #risposta da esito del blackjack iniziale
                esito = controlloBlackJack(_giocatore)

                if esito == True:
                    print "complimenti hai fatto BlackJack :)"
                    return

                continua = True  #booleano per continuità della partina, verra messo a false quando giocatore "sta" o "sfora"

                while continua:

                    print "\n%s decidi la tua mossa" % _giocatore.nome
                    print "1) carta"
                    print "2) stai"
                    scelta = input(("\ninserire scelta: "))

                    if scelta == 1:  #distribuzione carta
                        distribuisciCarta(_mazzo, _giocatore)

                        #controllo assi dopo ricevuta la carta 
                        _giocatore.controlloAssi()

                        print "\n%s" % _giocatore
                        somma = controlloSomma(
                            _giocatore
                        )  #controlla che si possa richiedere ancora carta

                        if somma == 21:  #controllo se 21 o sforato a carta
                            print "\nhai fatto 21 - you win!\n"
                            continua = False
                        elif somma > 21:
                            print "\nhai sforato con: %d\n" % somma
                            continua = False

                    elif scelta == 2:  #stop e controllo ritorno somma -> implementare controllo blackjack
                        risultato = stai(_giocatore)
                        continua = False
                        print "\nhai fatto: %d\n" % risultato


def main():

    tempMazzo = []  #lista di carte temporanea

    for a in ListaSemi:
        for b in ListaRanghi:

            tempCarta = carta.carta(a,
                                    b)  #carta da inserire in lista temporanea

            tempMazzo.append(tempCarta)

    _mazzo = mazzo.mazzo(
        tempMazzo)  #creo oggetto mazzo con la lista preparata prima

    for i in range(0, 100):  #shuffle del mazzo per 100 volte
        _mazzo.mischia()

    nomeGiocatore = raw_input(
        "\n\n\ninserisci il tuo nome: ")  #inserimento giocatore

    _giocatore = giocatore.giocatore(nomeGiocatore)
    print "\n\n\n benvenuto %s" % _giocatore.nome

    _mazziere = mazziere.mazziere()

    menu(_giocatore, _mazzo, _mazziere)


while True:
    main()

#-----------------------------------------------------------------------------------------------
# 23/01/17 18:30
# 1 -   trovato problema su controllo assi, se somma sfora ma è presente un asso in modo 
#       da transformare valore in 1 da comunque sforato -> 
#       da implementare quando sfora un controllo e cambiare il valore di tutti gli assi in 1 ->
#       non tutti solo quelli che compromettono la somma
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# 23/01/17 23:30
# 1 -   risolto in modo parziale problema su gli assi ma si presenta di conseguenza un secondo problema
#       quando, dopo aver compiuto in modo corretto il controllo su gli assi, riscontra problemi 
#       nel aggiungere i successivi valori -> probabilmente problema logico -> forse dovuto alla lista dei punti

# 2 -   da implementare la classe mazziere, probabilmente simile a giocatore e rivedere il metodo della distribuzione
#       iniziale(se ho voglia!)

# 3 -   da implementare una componente con un patrimonio per non star ogni volta a riavviare in modo forzato lo script
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#24/01/17 00:00
# 1 -   problema rilevato nel cotrollo degli assi sembra compleatamente sistemato - auguri a me!
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#24/01/17 8:20
# 1 -	problema relativo nel controllo degli assi sembra essere ancora persistente	
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#24/01/17 9:10
# 1 -	il problema dell'asso sembra essere risolto, altri test e posso passare all'implementazione
#		del mazziere
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#27/01/17 1:45
# 1 -   i test sul controllo dell'asso sembrano andare bene posso iniziare l'implementazione
#       dell'IA del mazziere -> sarà da riguardare anche la distribuzione delle carte all'inizio
#       della partita in modo da dividere le prime due carte tra mazziere e giocatore (la prima 
#       al mazziere sarà coperta) e le altre due
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#15/02/17 14:30
# 1-	ho optato per la distribuzione non mischiata ma dare prima tutte le carte al giocatore e 
# 		successivamente al mazziere
#-----------------------------------------------------------------------------------------------
