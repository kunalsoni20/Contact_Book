contacts = {}

def add_contact():
    name = input("Enter the contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
    else:
        number = input("Enter the contact number: ").strip()
        contacts[name] = number
        print(f"Contact '{name}' added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
        print()

def update_contact():
    name = input("Enter the contact name to update: ").strip()
    if name in contacts:
        number = input("Enter the new contact number: ").strip()
        contacts[name] = number
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter the contact name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        search_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
