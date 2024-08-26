from tkinter import *
from tkinter import  messagebox
from datetime import datetime

class Item:
    def __init__(self, id, itemName, price, quantity, totalprice):

        self.id = id
        self.itemName = itemName
        self.price = price
        self.quantity = quantity
        self.totalprice = totalprice

def save_bill_to_file(content):
    with open(f"{cName.get()}.txt", "w") as file:
        file.write(content)

messagebox.showinfo("discounted list","total bill\n "
                                      "      5000-9999 = 2%,\n"
                                      "    10000-14999 = 5%, \n"
                                      "    15000-49999 = 10%, \n"
                                      "    50000-99999 = 15%, \n"
                                      "100000-99999999 = 20%,  ")

def display_bill():

    item_list = []
    itemtotal = 0
    bill_content = ""

    now = datetime.now()
    formatted = now.strftime("%d/%m/%y")
    time = now.strftime(" %H:%M:%S")

    bill_content += "\t\t\t\tAntwal Store    \n"
    bill_content += "-----------------------------------------------------------------\n"
    bill_content += f"Date:-{formatted}\t\t\t\t\t\t Time:-{time}\n"
    bill_content += "-----------------------------------------------------------------\n"
    bill_content += f"Name : {cName.get()} \nAddress : {cAddress.get()}\nPhone : +91 {cphone.get()}\n"
    bill_content += "-----------------------------------------------------------------\n"
    bill_content += "Id : \t ItemName :  \t Price :  \t Quantity:  \t   total price :\n"
    bill_content += "-----------------------------------------------------------------\n"

    for i in range(len(item_name_entries)):
        id = i + 1
        name = item_name_entries[i].get()
        price = int(item_price_entries[i].get())
        quantity = int(item_quantity_entries[i].get())
        totalprice = price * quantity
        item = Item(id, name, price, quantity, totalprice)
        item_list.append(item)
        itemtotal += item.totalprice

        bill_content += f"{item.id} \t{item.itemName} \t\t{item.price} \t\t{item.quantity} \t  {item.totalprice}\n\n"

    bill_content += "-----------------------------------------------------------------\n"
    tax = itemtotal / 100 * 18
    gsttotal = tax + itemtotal
    bill_content += f"\t\t\t\t     cost of items :  {itemtotal}\n"
    bill_content += f"\t\t\t\t            tax is :+ {tax}\n"

    if 5000 <= gsttotal < 10000:
        dic = gsttotal / 100 * 2
    elif 10000 <= gsttotal < 15000:
        dic = gsttotal / 100 * 5
    elif 15000 <= gsttotal < 50000:
        dic = gsttotal / 100 * 10
    elif 50000 <= gsttotal < 100000:
        dic = gsttotal / 100 * 15
    elif 100000 <= gsttotal < 99999999:
        dic = gsttotal / 100 * 20
    else:
        dic = 0

    total = gsttotal - dic
    bill_content += f"\t\t\t\t        discounted :- {dic}\n"
    bill_content += "-----------------------------------------------------------------\n"
    bill_content += f"\t\t\t \t        total bill :  {total}\n"
    bill_content += "-----------------------------------------------------------------\n\n"
    bill_content += "\t\t\t Thanks for visiting\n\n\n"

    save_bill_to_file(bill_content)
    output_text.delete("1.0", END)
    output_text.insert(END, bill_content)

def add_item_entry():
    item_name_entry = Entry(window)
    item_name_entry.grid(row=len(item_name_entries) + 7, column=1)
    item_name_entries.append(item_name_entry)

    item_price_entry = Entry(window)
    item_price_entry.grid(row=len(item_price_entries) + 7, column=2)
    item_price_entries.append(item_price_entry)

    item_quantity_entry = Entry(window)
    item_quantity_entry.grid(row=len(item_quantity_entries) + 7, column=3)
    item_quantity_entries.append(item_quantity_entry)

# Set up the window
window = Tk()
window.title("Billing System")

Label(window, text="Customer Name").grid(row=0, column=0)
cName = Entry(window)
cName.grid(row=0, column=1)

Label(window, text="Address").grid(row=1, column=0)
cAddress = Entry(window)
cAddress.grid(row=1, column=1)

Label(window, text="Phone").grid(row=2, column=0)
cphone = Entry(window)
cphone.grid(row=2, column=1)

Label(window, text="Enter Items").grid(row=4, column=1)

Label(window, text="Item Name").grid(row=6, column=1)
Label(window, text="Price").grid(row=6, column=2)
Label(window, text="Quantity").grid(row=6, column=3)

item_name_entries = []
item_price_entries = []
item_quantity_entries = []

add_item_entry()

Button(window, text="Add Item", command=add_item_entry).grid(row=5, column=1)

Button(window, text="Generate Bill", command=display_bill).grid(row=20, column=1)

output_text = Text(window, height=20, width=100)
output_text.grid(row=21, column=0, columnspan=4)

window.mainloop()