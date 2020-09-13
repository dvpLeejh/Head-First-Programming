from tkinter import *

app = Tk()
app.title('Head_Ex Deliveries')

def save_data():
    try:
        file = open("deliveries.txt","a")
        file.write("Depot: \n")
        file.write(depot.get() + "\n")
        file.write("Description:; \n")
        file.write(description.get() + "\n")
        file.write("Address: \n")
        file.write(address.get("1.0", END))
        file.close()
        depot.set(None)
        description.delete(0,END)
        address.delete("1.0",END)
    except Exception as ex:
        app.title("Can't write to the file %s" % ex)

def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

Label(app, text = "Depot: ").pack()
depot = StringVar()
depot.set(None)
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description: ").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address: ").pack()
address = Text(app)
address.pack()

Button(app, text = "save", width = 10, height = 3 ,command = save_data).pack()

app.mainloop()
