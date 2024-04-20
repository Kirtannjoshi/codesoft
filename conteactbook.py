import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, sticky="w")
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, sticky="w")
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

        messagebox.showinfo("Success", "Contact added successfully.")

        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Empty", "No contacts to display.")
            return

        contact_list = ""
        for i, contact in enumerate(self.contacts, 1):
            contact_list += f"{i}. Name: {contact.name}, Phone: {contact.phone_number}\n"
        
        messagebox.showinfo("Contacts", contact_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
