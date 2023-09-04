import json

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'contacts': []}

def add_contact():
    contact = {}
    contact['id'] = input("Enter ID: ")
    contact['name'] = input("Enter Name: ")
    contact['phone'] = input("Enter Phone: ")
    contact['email'] = input("Enter Email: ")
    contacts = load_contacts()
    contacts['contacts'].append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def update_contact():
    contacts = load_contacts()
    contact_id = input("Enter the ID of the contact to update: ")
    for contact in contacts['contacts']:
        if contact['id'] == contact_id:
            contact['name'] = input("Enter Name: ")
            contact['phone'] = input("Enter Phone: ")
            contact['email'] = input("Enter Email: ")
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    contacts = load_contacts()
    contact_id = input("Enter the ID of the contact to delete: ")
    for contact in contacts['contacts']:
        if contact['id'] == contact_id:
            contacts['contacts'].remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def display_contacts():
    contacts = load_contacts()
    if not contacts['contacts']:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts['contacts']:
            print("ID:", contact['id'])
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print()

def main():
    while True:
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()