#Making a contact book application in Python
import json
import os
#defining the name of the file to store contacts
Contacts_file="contacts.json" #path to store contacts

def load_contacts():
    if not os.path.exists(Contacts_file):
        return {}
    with open(Contacts_file, 'r') as my_file:
        try:
            return json.load(my_file)
        except json.JSONDecodeError:
            return {}


def save_contacts(contacts):
    with open(Contacts_file, 'w') as my_file:
        json.dump(contacts, my_file)

def display_menu():
    print("#"*5,"Contact Book Menu:", "#"*5)
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("-"*30)
    
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("-----All Contacts-----")
    for name, details in contacts.items():
        print(f"Name: {name}, ")
        print(f" Phone: {details['phone']}")
        print(f" Email: {details['email']}")
        print("-"*30)

def add_contact(contacts):  
    print("\n-----Add New Contact-----")
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    name_find = input("Enter the name of the contact to search: ")
    if name_find in contacts:
        details = contacts[name_find]
        print(f"Contact found: Name: {name_find}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact not found.")   

def delete_contact(contacts):
    name_delete = input("Enter the name of the contact to delete: ")
    if name_delete in contacts:
        del contacts[name_delete]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name_update = input("Enter the name of the contact to update: ")
    if name_update in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        if phone:
            contacts[name_update]['phone'] = phone
        if email:
            contacts[name_update]['email'] = email
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

#-----main program-----
def main():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice=="5":
            search_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__=="__main__":
    main()