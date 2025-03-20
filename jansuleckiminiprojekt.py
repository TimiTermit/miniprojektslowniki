class Dictionary:
    def __init__(self):
        self.words = {}
        self.participants = {}

    # Słownik
    def add_word(self, word, definition):
        """Dodaje nowe słowo i jego definicję do słownika."""
        if word in self.words:
            print(f"Słowo '{word}' już istnieje w słowniku.")
        else:
            self.words[word] = definition
            print(f"Słowo '{word}' zostało dodane.")

    def remove_word(self, word):
        """Usuwa słowo z słownika."""
        if word in self.words:
            self.words[word] = None  # Oznaczamy słowo jako usunięte
            print(f"Słowo '{word}' zostało usunięte.")
        else:
            print(f"Słowo '{word}' nie istnieje w słowniku.")

    def find_word(self, word):
        """Zwraca definicję słowa, jeśli istnieje w słowniku."""
        return self.words.get(word, "Słowo nie znalezione.")

    def list_words(self):
        """Zwraca listę wszystkich słów w słowniku."""
        return [word for word in self.words if self.words[word] is not None]

    def update_definition(self, word, new_definition):
        """Aktualizuje definicję istniejącego słowa."""
        if word in self.words and self.words[word] is not None:
            self.words[word] = new_definition
            print(f"Definicja słowa '{word}' została zaktualizowana.")
        else:
            print(f"Słowo '{word}' nie istnieje w słowniku.")

    def clear_dictionary(self):
        """Czyści wszystkie słowa w słowniku."""
        self.words = {}
        print("Słownik został wyczyszczony.")

    def save_words_to_file(self, filename):
        """Zapisuje słowa do pliku tekstowego."""
        with open(filename, 'w') as file:
            for word, definition in self.words.items():
                if definition is not None:
                    file.write(f"{word}:{definition}\n")
        print(f"Słownik został zapisany do pliku '{filename}'.")

    def load_words_from_file(self, filename):
        """Ładuje słowa z pliku tekstowego."""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    word, definition = line.strip().split(':', 1)
                    self.add_word(word, definition)
            print(f"Słownik został załadowany z pliku '{filename}'.")
        except FileNotFoundError:
            print(f"Plik '{filename}' nie został znaleziony.")
        except Exception as e:
            print(f"Wystąpił błąd podczas ładowania pliku: {e}")

    # Uczestnicy
    def add_participant(self, first_name, last_name):
        """Dodaje nowego uczestnika."""
        participant_id = f"{first_name.lower()}_{last_name.lower()}"
        if participant_id in self.participants:
            print(f"Uczestnik '{first_name} {last_name}' już istnieje.")
        else:
            self.participants[participant_id] = {'first_name': first_name, 'last_name': last_name}
            print(f"Uczestnik '{first_name} {last_name}' został dodany.")

    def remove_participant(self, first_name, last_name):
        """Usuwa uczestnika."""
        participant_id = f"{first_name.lower()}_{last_name.lower()}"
        if participant_id in self.participants:
            self.participants[participant_id] = None  # Oznaczamy uczestnika jako usuniętego
            print(f"Uczestnik '{first_name} {last_name}' został usunięty.")
        else:
            print(f"Uczestnik '{first_name} {last_name}' nie istnieje.")

    def find_participant(self, first_name, last_name):
        """Zwraca dane uczestnika, jeśli istnieje."""
        participant_id = f"{first_name.lower()}_{last_name.lower()}"
        return self.participants.get(participant_id, "Uczestnik nie znaleziony.")

    def list_participants(self):
        """Zwraca listę wszystkich uczestników."""
        return [f"{data['first_name']} {data['last_name']}" for data in self.participants.values() if data is not None]

    def clear_participants(self):
        """Czyści wszystkich uczestników."""
        self.participants = {}
        print("Lista uczestników została wyczyszcz ona.")

    def sort_words(self):
        """Zwraca posortowaną listę słów w słowniku."""
        return sorted(self.list_words())

    def find_participants_by_first_name(self, first_name):
        """Zwraca uczestników według imienia."""
        return [f"{data['first_name']} {data['last_name']}" for data in self.participants.values() if data is not None and data['first_name'].lower() == first_name.lower()]

    def find_participants_by_last_name(self, last_name):
        """Zwraca uczestników według nazwiska."""
        return [f"{data['first_name']} {data['last_name']}" for data in self.participants.values() if data is not None and data['last_name'].lower() == last_name.lower()]

    def __str__(self):
        """Zwraca reprezentację słownika i uczestników jako string."""
        words_str = "\n".join([f"{word}: {definition}" for word, definition in self.words.items() if definition is not None])
        participants_str = "\n".join(self.list_participants())
        return f"Słownik:\n{words_str}\n\nUczestnicy:\n{participants_str}"

    def count_words(self):
        """Zwraca liczbę słów w słowniku."""
        return len(self.list_words())

    def count_participants(self):
        """Zwraca liczbę uczestników."""
        return len(self.list_participants())

    def clear_all(self):
        """Czyści zarówno słownik, jak i uczestników."""
        self.clear_dictionary()
        self.clear_participants()
        print("Wszystko zostało wyczyszczone.")

def display_menu():
    """Wyświetla menu użytkownika."""
    print("\n--- Słownik i Uczestnicy ---")
    print("1. Dodaj słowo")
    print("2. Usuń słowo")
    print("3. Znajdź słowo")
    print("4. Zaktualizuj definicję")
    print("5. Wypisz wszystkie słowa")
    print("6. Sortuj słowa")
    print("7. Dodaj uczestnika")
    print("8. Usuń uczestnika")
    print("9. Znajdź uczestnika")
    print("10. Wypisz wszystkich uczestników")
    print("11. Znajdź uczestników według imienia")
    print("12. Znajdź uczestników według nazwiska")
    print("13. Zapisz słowa do pliku")
    print("14. Wczytaj słowa z pliku")
    print("15. Zlicz słowa")
    print("16. Zlicz uczestników")
    print("17. Wyczyść wszystko")
    print("18. Wyjdź")

def main():
    dictionary = Dictionary()
    while True:
        display_menu()
        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            word = input("Podaj słowo: ")
            definition = input("Podaj definicję: ")
            dictionary.add_word(word, definition)
        elif choice == '2':
            word = input("Podaj słowo do usunięcia: ")
            dictionary.remove_word(word)
        elif choice == '3':
            word = input("Podaj słowo do znalezienia: ")
            print(dictionary.find_word(word))
        elif choice == '4':
            word = input("Podaj słowo do zaktualizowania: ")
            new_definition = input("Podaj nową definicję: ")
            dictionary.update_definition(word, new_definition)
        elif choice == '5':
            print(dictionary)
        elif choice == '6':
            print("Posortowane słowa:")
            print(dictionary.sort_words())
        elif choice == '7':
            first_name = input("Podaj imię uczestnika: ")
            last_name = input("Podaj nazwisko uczestnika: ")
            dictionary.add_participant(first_name, last_name)
        elif choice == '8':
            first_name = input("Podaj imię uczestnika do usunięcia: ")
            last_name = input("Podaj nazwisko uczestnika do usunięcia: ")
            dictionary.remove_participant(first_name, last_name)
        elif choice == '9':
            first_name = input("Podaj imię uczestnika do znalezienia: ")
            last_name = input("Podaj nazwisko uczestnika do znalezienia: ")
            print(dictionary.find_participant(first_name, last_name))
        elif choice == '10':
            print("Uczestnicy:")
            print(dictionary.list_participants())
        elif choice == '11':
            first_name = input("Podaj imię do wyszukania uczestników: ")
            print(dictionary.find_participants_by_first_name(first_name))
        elif choice == '12':
            last_name = input("Podaj nazwisko do wyszukania uczestników: ")
            print(dictionary.find_participants_by_last_name(last_name))
        elif choice == '13':
            filename = input("Podaj nazwę pliku do zapisania słów: ")
            dictionary.save_words_to_file(filename)
        elif choice == '14':
            filename = input("Podaj nazwę pliku do wczytania słów: ")
            dictionary.load_words_from_file(filename)
        elif choice == '15':
            print(f"Liczba słów w słowniku: {dictionary.count_words()}")
        elif choice == '16':
            print(f"Liczba uczestników: {dictionary.count_participants()}")
        elif choice == '17':
            dictionary.clear_all()
        elif choice == '18':
            print("Wyjście z programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()