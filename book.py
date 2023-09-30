class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the address book.")
        else:
            print("Contacts in the address book:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")

    def update_contact(self, index, new_name, new_email, new_phone):
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = new_name
            self.contacts[index].email = new_email
            self.contacts[index].phone = new_phone
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Deleted contact: {deleted_contact.name}")
        else:
            print("Invalid contact index.")

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = Contact(name, email, phone)
            address_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            address_book.view_contacts()
        elif choice == "3":
            index = int(input("Enter the index of the contact to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            new_phone = input("Enter new phone: ")
            address_book.update_contact(index, new_name, new_email, new_phone)
        elif choice == "4":
            index = int(input("Enter the index of the contact to delete: "))
            address_book.delete_contact(index)
        elif choice == "5":
            print("
