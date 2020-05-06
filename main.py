from tkinter import *
from Request import Bdd


class Interface(Frame):


    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=450, height=250, **kwargs)
        self.pack(fill=BOTH)

        self.host = Label(self, text="HOST :")
        self.host.place(width=60, x=0, y=10)
        self.var_host = StringVar()
        self.ligne_host = Entry(self, textvariable=self.var_host, width=20)
        self.ligne_host.place(x=60, y=10)

        self.port = Label(self, text="PORT :")
        self.port.place(width=60, x=0, y=50)
        self.var_port = IntVar()
        self.ligne_port = Entry(self, textvariable=self.var_port, width=20)
        self.ligne_port.place(x=60, y=50)

        self.bouton_setip = Button(self, highlightbackground='#3E4149', text="CONNEXION", command=self.setip)
        self.bouton_setip.place(x=270, y=10)

        # Création de nos widgets
        self.message = Label(self, text="Choisissez votre requête")
        self.message.place(x=10, y=100)

        self.temp = Label(self, text="TEMP :")
        self.temp.place(x=0, y=150)
        self.var_texte = DoubleVar()
        self.ligne_texte = Entry(self, textvariable=self.var_texte, width=10)
        self.ligne_texte.place(x=50, y=150)


        self.indice = Label(self, text="ID :")
        self.indice.place(x=170, y=150)
        self.var_indice = IntVar()
        self.ligne_indice = Entry(self, textvariable=self.var_indice, width=10)
        self.ligne_indice.place(x=200, y=150)

        self.bouton_quitter = Button(self, highlightbackground ='#3E4149',text="PUT", command=self.update)
        self.bouton_quitter.place(x=30, y=200)

        self.bouton_cliquer = Button(self, highlightbackground ='#3E4149',text="GET", command=self.cliquer)
        self.bouton_cliquer.place(x=105, y=200)

        self.bouton_getById = Button(self, highlightbackground='#3E4149', text="GETBYID", command=self.getById)
        self.bouton_getById.place(x=180, y=200)

        self.bouton_soumettre = Button(self, highlightbackground='#3E4149', text="POST", command=self.soumettre)
        self.bouton_soumettre.place(x=275, y=200)

        self.bouton_delete = Button(self, highlightbackground='#3E4149', text="DELETE", command=self.delete)
        self.bouton_delete.place(x=350, y=200)


    def setip(self):
        self.ip=self.var_host.get()
        self.port = self.var_port.get()

    def setlogin(self):
        self.login=self.var_login.get()

    def setpassword(self):
        self.password=self.var_password.get()


    def cliquer(self):
        self.bdd = Bdd(self.ip, self.port, 'root', 'root', 'METEO')
        self.temp=self.bdd.Lastselect()[2]
        self.Id = self.bdd.Lastselect()[0]
        self.message["text"] =f"ENREGISTREMENT ID : {self.Id}, TEMPERATURE : {self.temp} °C."

    def getById(self):
        self.bdd = Bdd(self.ip, self.port, 'root', 'root', 'METEO')
        self.id = self.var_indice.get()
        try:
            self.temp=self.bdd.selectById(self.id)[2]
            self.Id = self.bdd.selectById(self.id)[0]
            self.message["text"] = f"ENREGISTREMENT ID : {self.Id}, TEMPERATURE : {self.temp} °C."
        except:
            self.message["text"] = f"PAS D'ENREGISTREMENT  A L'ID : {self.id}."


    def soumettre(self):
        self.bdd = Bdd(self.ip, self.port, 'root', 'root', 'METEO')
        self.temp=self.var_texte.get()
        self.bdd.insert(self.temp)

    def update(self):
        self.bdd = Bdd(self.ip, self.port, 'root', 'root', 'METEO')
        self.temp=self.var_texte.get()
        self.id = self.var_indice.get()
        self.bdd.update(self.temp,self.id)

    def delete(self):
        self.bdd = Bdd(self.ip, self.port, 'root', 'root', 'METEO')
        self.id = self.var_indice.get()
        self.bdd.delete(self.id)



fenetre = Tk()
fenetre.title('Fenêtre requête SQL')
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()