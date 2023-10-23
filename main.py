from Veicolo import Utilitaria, Lusso
from Cliente import Cliente


class main():

    def __init__(self):
        self.__listaClienti = []
        self.__listaUtilitaria = []
        self.__listaLusso = []

    def inserisci_Utilitaria(self, m, c, t):

        self.__listaUtilitaria.append(Utilitaria(m, c, t))

    def inserisci_Lusso(self, m, c, t, a):

        self.__listaLusso.append(Lusso(m, c, t, a))

    def inserisci_dati_cliente(self, n, c, e, np, cf):

        self.__listaClienti.append(Cliente(n, c, e, np, cf))

    def nuovo_cliente(self, clienti, noleggi):
        cf = input("CF: ")
        if cf not in clienti:  # Nuovo cliente
            cliente = self.inserisci_dati_cliente()
            if isinstance(cliente, Cliente):
                clienti[cf] = cliente
                noleggi[cf] = []
                print("Cliente creato.")
        return cf

    def nuovo_noleggio(self, clienti, veicoli, noleggi):
        targa = input("Targa: ")
        if targa in veicoli:  # Il veicolo esiste

            for cf in noleggi:
                if targa in noleggi[cf]:  # Veicolo non noleggiabile
                    print("Veicolo non noleggiabile.")
                    return

            cf = self.nuovo_cliente(clienti, noleggi)
            if cf in clienti:  # Cliente esistente
                noleggi[cf].append(targa)

        else:
            print("Veicolo non trovato.")

    def toStringCliente(self):
        lista = []
        for a in self.__listaClienti:
            lista.append(a.toString())
        return lista

    def toStringVeicolo(self):
        lista = []
        for a in self.__listaLusso:
            lista.append(a.toString())
        return lista
