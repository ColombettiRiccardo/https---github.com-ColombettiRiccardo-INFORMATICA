from grafica import *
from tkinter import *


def apriCliente(root):
    root = Tk()
    root.title("Cliente")
    Cliente(root)
    root.mainloop()


def apriVeicolo(root):
    root = Tk()
    root.title("Veicolo")
    Veicolo(root)
    root.mainloop()


def apriNoleggio(root):
    root = Tk()
    root.title("Noleggio")
    Noleggio(root)
    root.mainloop()


def main():
    root = Tk()
    root.geometry("200x100")
    root.title("start")

    b1 = Button(root, text='CARICA CLIENTE', command=lambda: apriCliente(root))
    b1.grid(column=0, row=2)

    b2 = Button(root, text='CARICA VEICOLO', command=lambda: apriVeicolo(root))
    b2.grid(column=0, row=4)

    b3 = Button(root, text='CARICA NOLEGGIO',
                command=lambda: apriNoleggio(root))
    b3.grid(column=0, row=6)

    root.mainloop()


main()
