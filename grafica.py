from tkinter import *
from main import main


class Cliente():

    def __init__(self, parent):
        self.parent = parent
        self.att = main()

        # TOP LEVEL --------------------------------------------------------------------------------

        self.frame1 = Frame(parent)
        self.frame1.pack()

        # CASELLE CLIENTE --------------------------------------------------------------------------
        self.root = parent
        self.root.title("Gestione Clienti")

        self.frame = Frame(parent)

        self.label_nome = Label(self.frame1, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = Entry(self.frame1)
        self.entry_nome.grid(row=0, column=1)

        self.label_cognome = Label(self.frame1, text="Cognome:")
        self.label_cognome.grid(row=1, column=0)
        self.entry_cognome = Entry(self.frame1)
        self.entry_cognome.grid(row=1, column=1)

        self.label_eta = Label(self.frame1, text="Età:")
        self.label_eta.grid(row=2, column=0)
        self.entry_eta = Entry(self.frame1)
        self.entry_eta.grid(row=2, column=1)

        self.label_patente = Label(self.frame1, text="Numero Patente:")
        self.label_patente.grid(row=3, column=0)
        self.entry_patente = Entry(self.frame1)
        self.entry_patente.grid(row=3, column=1)

        self.label_Codice_Fiscale = Label(self.frame1, text="Codice Fiscale:")
        self.label_Codice_Fiscale.grid(row=4, column=0)
        self.entry_Codice_Fiscale = Entry(self.frame1)
        self.entry_Codice_Fiscale.grid(row=4, column=1)

        # BOTTONI ----------------------------------------------------------------------------------
        self.bCarica = Button(self.frame1, text="Carica",
                              command=self.Button_CaricaC)
        self.bCarica.grid(column=0, row=7)

        self.bVisualizza = Button(
            self.frame1, text="Visualizza", command=self.Button_VisualizzaC)
        self.bVisualizza.grid(column=0, row=8)

        self.bPulisci = Button(self.frame1, text="Pulisci",
                               command=self.MyButton_Pulisci)
        self.bPulisci.grid(column=0, row=9)
        # TEXTBOX -----------------------------------------------------------------------------------
        self.listaC = Text(self.frame1, height=5, width=20)
        self.listaC.grid(column=1, row=8)


# FUNZIONI CLIENTE ----------------------------------------------------------------------------------


    def Button_CaricaC(self):

        self.att.inserisci_dati_cliente(self.entry_nome.get(), self.entry_cognome.get(
        ), self.entry_eta.get(), self.entry_patente.get(), self.entry_Codice_Fiscale.get())

    def Button_VisualizzaC(self):
        self.listaC.delete("1.0", "end")
        self.listaC.insert(1.0, "\n".join(self.att.toStringCliente()))

    def MyButton_Pulisci(self):
        self.parent.deiconify()
        self.entry_nome.delete(0, END)
        self.entry_cognome.delete(0, END)
        self.entry_eta.delete(0, END)
        self.entry_patente.delete(0, END)
        self.entry_Codice_Fiscale.delete(0, END)


class Veicolo():

    def __init__(self, parent):
        self.parent = parent
        self.att = main()

        # TOP LEVEL --------------------------------------------------------------------------------

        self.frame2 = Frame(parent)
        self.frame2.pack()

# FRAME 2

        self.frame2 = Frame(parent)
        self.frame2.pack()

        self.label_modello = Label(self.frame2, text="modello:")
        self.label_modello.grid(row=0, column=0)
        self.entry_modello = Entry(self.frame2)
        self.entry_modello.grid(row=0, column=1)

        self.label_costo = Label(self.frame2, text="costo:")
        self.label_costo.grid(row=1, column=0)
        self.entry_costo = Entry(self.frame2)
        self.entry_costo.grid(row=1, column=1)

        self.label_targa = Label(self.frame2, text="targa:")
        self.label_targa.grid(row=2, column=0)
        self.entry_targa = Entry(self.frame2)
        self.entry_targa.grid(row=2, column=1)

        self.label_Accessorio = Label(self.frame2, text="Accessorio:")
        self.label_Accessorio.grid(row=3, column=0)
        self.entry_Accessorio = Entry(self.frame2)
        self.entry_Accessorio.grid(row=3, column=1)
        # BOTTONI--------------------------------------------------------------------------------------

        self.bCarica = Button(self.frame2, text="Carica",
                              command=self.Button_CaricaV)
        self.bCarica.grid(column=0, row=7)

        self.bVisualizza = Button(
            self.frame2, text="Visualizza", command=self.Button_VisualizzaV)
        self.bVisualizza.grid(column=0, row=8)

        self.bPulisci = Button(self.frame2, text="Pulisci",
                               command=self.Button_PulisciV)
        self.bPulisci.grid(column=0, row=9)

        # TEXTBOX--------------------------------------------------------------------------------------

        self.listaV = Text(self.frame2, height=5, width=20)
        self.listaV.grid(column=1, row=8)

    def Button_CaricaV(self):

        self.att.inserisci_Lusso(self.entry_modello.get(), self.entry_costo.get(
        ), self.entry_targa.get(), self.entry_Accessorio.get())

    def Button_VisualizzaV(self):
        self.listaV.delete("1.0", "end")
        self.listaV.insert(1.0, "\n".join(self.att.toStringVeicolo()))

    def Button_PulisciV(self):
        self.parent.deiconify()
        self.entry_modello.delete(0, END)
        self.entry_costo.delete(0, END)
        self.entry_targa.delete(0, END)
        self.entry_Accessorio.delete(0, END)


class Noleggio(Cliente, Veicolo):

    def __init__(self, parent):
        self.parent = parent
        self.att = main()

        # TOP LEVEL --------------------------------------------------------------------------------

        self.frame3 = Frame(parent)
        self.frame3.pack()

        self.label_targa_noleggio = Label(self.frame3, text="targa:")
        self.label_targa_noleggio.grid(row=0, column=0)
        self.entry_targa_noleggio = Entry(self.frame3)
        self.entry_targa_noleggio.grid(row=0, column=1)
