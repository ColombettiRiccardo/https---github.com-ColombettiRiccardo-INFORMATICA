class Utilitaria:
    def __init__(self, modello, costo, targa):
        self.__modello = modello
        self.__costo = costo
        self.__targa = targa

    def setModello(self, modello):
        self.__modello = modello

    def setCosto(self, costo):
        self.__costo = costo

    def setTarga(self, targa):
        self.__targa = targa

    def getModello(self):
        return self.__modello

    def getCosto(self):
        return self.__costo

    def getTarga(self):
        return self.__targa

    def __str__(self):
        return "Modello: " + self.__modello + "\nCosto: " + str(self.__costo) + "\nTarga:" + self.__targa


class Lusso(Utilitaria):
    def __init__(self, modello, costo, targa, accessori):
        Utilitaria.__init__(self, modello, costo, targa)
        self.__accessori = accessori

    def setAccessori(self, accessori):
        self.__accessori = accessori

    def getAccessori(self):
        return self.__accessori

    def toString(self):

        return self.__str__() + "\nAccessori: " + self.__accessori + "\n"
