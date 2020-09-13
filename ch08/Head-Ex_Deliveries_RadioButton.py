from tkinter import *

app = Tk()
app.title('Head_Ex Deliveries')

def save_data():
    file = open("deliveries.txt","a")
    file.write("Depot: \n")
    file.write(depot.get() + "\n")
    file.write("Description:; \n")
    file.write(description.get() + "\n")
    file.write("Address: \n")
    file.write(address.get("1.0", END))
    file.close()
    depot.delete(0,END)
    description.delete(0,END)
    address.delete("1.0",END)


Label(app, text = "Depot: ").pack()
depot = StringVar()
depot.set(None)
Radiobutton(app, variable = depot, text = "Cambridge, MA", value = "Cambridge, MA").pack()
Radiobutton(app, variable = depot, text = "Cambridge, UK", value = "Cambridge, UK").pack()
Radiobutton(app, variable = depot, text = "Seattle, WA", value = "Seattle, WA").pack()

Label(app, text = "Description: ").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address: ").pack()
address = Text(app)
address.pack()

Button(app, text = "save", width = 10, height = 3 ,command = save_data).pack()

app.mainloop()
