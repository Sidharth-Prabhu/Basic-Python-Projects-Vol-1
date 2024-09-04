word_meanings = {
    "apple": "A sweet, juicy, red fruit.",
    "dog": "A domesticated carnivorous mammal.",
    "house": "A building for human habitation.",
    # Add more words and meanings here...
}

def display_menu():
    print("\nMenu:")
    print("1. Add word and meaning")
    print("2. Search for word")
    print("3. Delete word")
    print("4. Display all words")
    print("5. Exit")

def add_word():
    word = input("Enter word: ")
    meaning = input("Enter meaning: ")
    word_meanings[word] = meaning
    print(f"Word '{word}' added successfully.")

def search_word():
    word = input("Enter word to search: ")
    if word in word_meanings:
        print(f"Meaning: {word_meanings[word]}")
    else:
        print(f"Word '{word}' not found.")

def delete_word():
    word = input("Enter word to delete: ")
    if word in word_meanings:
        del word_meanings[word]
        print(f"Word '{word}' deleted successfully.")
    else:
        print(f"Word '{word}' not found.")

def display_all():
    print("\nWords and Meanings:")
    for word, meaning in word_meanings.items():
        print(f"{word}: {meaning}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_word()
        elif choice == "2":
            search_word()
        elif choice == "3":
            delete_word()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
