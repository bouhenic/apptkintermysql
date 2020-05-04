from tkinter import *
import pymysql

from Request import Bdd


class Interface(Frame):


    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        self.message = Label(self, text="Choisissez votre requête")
        self.message.pack()

        self.temp = Label(self, text="TEMP :")
        self.temp.pack(side="left")
        self.var_texte = IntVar()
        self.ligne_texte = Entry(self, textvariable=self.var_texte, width=10)
        self.ligne_texte.pack(side="left")

        self.temp = Label(self, text="ID :")
        self.temp.pack(side="left")
        self.var_indice = IntVar()
        self.ligne_indice = Entry(self, textvariable=self.var_indice, width=10)
        self.ligne_indice.pack(side="left")

        self.bouton_quitter = Button(self, highlightbackground ='#3E4149',text="PUT", command=self.update)
        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, highlightbackground ='#3E4149',text="GET", command=self.cliquer)
        self.bouton_cliquer.pack(side="left")

        self.bouton_soumettre = Button(self, highlightbackground='#3E4149', text="POST", command=self.soumettre)
        self.bouton_soumettre.pack(side="left")

        self.bouton_delete = Button(self, highlightbackground='#3E4149', text="DELETE", command=self.delete)
        self.bouton_delete.pack(side="left")




    def cliquer(self):
        self.bdd = Bdd('localhost', 3306, 'root', 'root', 'METEO')
        self.temp=self.bdd.Lastselect()
        self.message["text"] = "TEMPERATURE : {} °C.".format(self.temp)

    def soumettre(self):
        self.bdd = Bdd('localhost', 3306, 'root', 'root', 'METEO')
        self.temp=self.var_texte.get()
        self.bdd.insert(self.temp)

    def update(self):
        self.bdd = Bdd('localhost', 3306, 'root', 'root', 'METEO')
        self.temp=self.var_texte.get()
        self.id = self.var_indice.get()
        self.bdd.update(self.temp,self.id)

    def delete(self):
        self.bdd = Bdd('localhost', 3306, 'root', 'root', 'METEO')
        self.id = self.var_indice.get()
        self.bdd.delete(self.id)




fenetre = Tk()
fenetre.title('Fenêtre requête SQL')
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()