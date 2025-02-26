from tkinter import *

langas = Tk()
langas.title("Programa")
langas.iconbitmap(r'Programa.ico')
tekstas = StringVar()


# kintamasis = "Labas,  "

def spausdinti():
    vardas = laukas.get()
    tekstas.set(vardas)
    uzrasas1["text"] = f"Labas, {tekstas.get()}!"
    # uzrasas1["text"] = kintamasis + vardas + "!"
    status["text"] = "Sukurta"  ##uzduotis4.1


def isvalyti():
    uzrasas1["text"] = ""
    status["text"] = "Isvalyta"  ##uzduotis4.2


def grazinti():
    uzrasas1["text"] = f"Labas, {tekstas.get()}!"
    # uzrasas1["text"] = kintamasis + vardas + "!"
    status["text"] = "Atkurta"  ##uzduotis4.3????


def iseiti():
    langas.destroy()


langas.geometry("275x75")
meniu = Menu(langas)  # uzduotis3
langas.config(menu=meniu)  # uzduotis3
submeniu = Menu(meniu, tearoff=0)  # uzduotis3
meniu.add_cascade(label="Meniu", menu=submeniu)  # uzduotis3
#
uzrasas = Label(langas, text=" Iveskite varda ")
laukas = Entry(langas)
mygtukas = Button(langas, text="Patvritinti", command=spausdinti)
uzrasas1 = Label(langas, text="")
langas.bind("<Return>", lambda event: spausdinti())  ## uzduotis2
submeniu.add_command(label="Isvalyti", command=isvalyti)  # uzduotis3
submeniu.add_command(label="Atkurti paskutini", command=grazinti)  # uzduotis3
submeniu.add_separator()  # uzduotis3
submeniu.add_command(label="Iseiti", command=iseiti)  # uzduotis3
langas.bind("<Escape>", lambda event: iseiti())  ##uzduotis4.4
#
status = Label(langas, text="Nieko nedaro...", relief=SUNKEN, anchor=W)

uzrasas.pack()

uzrasas.grid(row=0, column=0, sticky=W)
laukas.grid(row=0, column=1, sticky=W)
mygtukas.grid(row=0, column=2, sticky=W)
uzrasas1.grid(row=1, column=1, sticky=W)
status.grid(row=2, columnspan=3, sticky=EW)  ###?????
langas.mainloop()
"# naujas" 
