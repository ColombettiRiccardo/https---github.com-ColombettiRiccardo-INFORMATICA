class Cliente:
    def __init__(self, nome, cognome, eta, n_patente, codice_fiscale):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__n_patente = n_patente
        self.__codice_fiscale = codice_fiscale

    def setNome(self, nome):
        self.__nome = nome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def setEta(self, eta):
        self.__eta = eta

    def setNPatente(self, n_patente):
        self.__n_patente = n_patente

    def setCodiceFiscale(self, c_fiscale):
        self.__codice_fiscale = c_fiscale

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getEta(self):
        return self.__eta

    def getNPatente(self):
        return self.__n_patente

    def getCFiscale(self):
        return self.__codice_fiscale

    def toString(self):
        return "Nome: " + self.__nome + "\nCognome: " + self.__cognome + "\nEta': " + str(self.__eta) + "\nN.Patente: " + self.__n_patente + "\nCodiceFiscale " + self.__codice_fiscale + "\n"
