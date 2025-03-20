class Dictionary:
    def __init__(self):
        self.words = {}

    def add_word(self, word, definition):
        """Dodaje nowe slowo i jego definicje do slownika."""
        if word in self.words:
            print(f"Slowo '{word}' juz istnieje w slowniku.")
        else:
            self.words[word] = definition
            print(f"Slowo '{word}' zostalo dodane.")

    def remove_word(self, word):
        """Usuwa slowo ze slownika."""
        if word in self.words:
            del self.words[word]
            print(f"Slowo '{word}' zostalo usuniete.")
        else:
            print(f"Slowo '{word}' nie istnieje w slowniku.")

    def find_word(self, word):
        """Zwraca definicje slowa, jesli istnieje w slowniku."""
        return self.words.get(word, "Slowo nie znalezione.")

    def display_words(self):
        """Wyswietla wszystkie slowa i ich definicje w slowniku."""
        if not self.words:
            print("Slownik jest pusty.")
        else:
            for word, definition in self.words.items():
                print(f"{word}: {definition}")

    def update_word(self, word, new_definition):
        """Aktualizuje definicje istniejacego slowa."""
        if word in self.words:
            self.words[word] = new_definition
            print(f"Definicja slowa '{word}' zostala zaktualizowana.")
        else:
            print(f"Slowo '{word}' nie istnieje w slowniku.")

    def clear_dictionary(self):
        """Czysci wszystkie slowa w slowniku."""
        self.words.clear()
        print("Slownik zostal wyczyszczony.")

    def save_to_file(self, filename):
        """Zapisuje slownik do pliku."""
        with open(filename, 'w') as file:
            for word, definition in self.words.items():
                file.write(f"{word}:{definition}\n")
        print(f"Slownik zostal zapisany do pliku '{filename}'.")

    def load_from_file(self, filename):
        """Laduje slownik z pliku."""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    word, definition = line.strip().split(':', 1)
                    self.words[word] = definition
            print(f"Slownik zostal zaladowany z pliku '{filename}'.")
        except FileNotFoundError:
            print(f"Plik '{filename}' nie zostal znaleziony.")
        except Exception as e:
            print(f"Wystapil blad podczas ladowania pliku: {e}")

    def search_by_prefix(self, prefix):
        """Zwraca slowa, ktore zaczynaja sie od danego prefiksu."""
        results = {word: definition for word, definition in self.words.items() if word.startswith(prefix)}
        return results if results else "Brak slow zaczynajacych sie od tego prefiksu."

    def search_by_suffix(self, suffix):
        """Zwraca slowa, ktore koncza sie na dany sufiks."""
        results = {word: definition for word, definition in self.words.items() if word.endswith(suffix)}
        return results if results else "Brak slow konczacych sie na ten sufiks."

    def search_by_definition(self, search_term):
        """Zwraca slowa, ktore zawieraja dany termin w definicji."""
        results = {word: definition for word, definition in self.words.items() if search_term in definition}
        return results if results else "Brak slow zawierajacych ten termin w definicji."

    def count_words(self):
        """Zwraca liczbe slow w slowniku."""
        return len(self.words)

    def is_empty(self):
        """Sprawdza, czy slownik jest pusty."""
        return len(self.words) == 0

    def get_all_words(self):
        """Zwraca liste wszystkich slow w slowniku."""
        return list(self.words.keys())

    def get_definitions(self):
        """Zwraca liste wszystkich definicji w slowniku."""
        return list(self.words.values())

    def get_word_definition(self, word):
        """Zwraca definicje danego slowa lub informacje, ze slowo nie istnieje."""
        return self.words.get(word, "Slowo nie istnieje w slowniku.")

    def get_words_starting_with(self, letter):
        """Zwraca slowa zaczynajace sie na dana litere."""
        results = {word: definition for word, definition in self.words.items() if word.startswith(letter)}
        return results if results else "Brak slow zaczynajacych sie na te litere."

    def get_words_ending_with(self, letter):
        """Zwraca slowa konczace sie na dana litere."""
        results = {word: definition for word, definition in self.words.items() if word.endswith(letter)}
        return results if results else "Brak slow konczacych sie na te litere."

    def get_longest_word(self):
        """Zwraca najdluzsze slowo w slowniku."""
        if not self.words:
            return "Slownik jest pusty."
        longest_word = max(self.words.keys(), key=len)
        return longest_word, self.words[longest_word]

    def get_shortest_word(self):
        """Zwraca najkrotsze slowo w slowniku."""
        if not self.words:
            return "Slownik jest pusty."
        shortest_word = min(self.words.keys(), key=len)
        return shortest_word, self.words[shortest_word]

    def get_words_with_length(self, length):
        """Zwraca slowa o okreslonej dlugosci."""
        results = {word: definition for word, definition in self.words.items() if len(word) == length}
        return results if results else "Brak slow o tej dlugosci."

    def get_definitions_with_length(self, length):
        """Zwraca definicje o okreslonej dlugosci."""
        results = {word: definition for word, definition in self.words.items() if len(definition) == length}
        return results if results else "Brak definicji o tej dlugosci."

    def get_words_with_min_length(self, min_length):
        """Zwraca slowa o dlugosci wiekszej lub rownej podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(word) >= min_length}
        return results if results else "Brak slow o dlugosci wiekszej lub rownej tej wartosci."

    def get_definitions_with_min_length(self, min_length):
        """Zwraca definicje o dlugosci wiekszej lub rownej podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(definition) >= min_length}
        return results if results else "Brak definicji o dlugosci wiekszej lub rownej tej wartosci."

    def get_words_with_max_length(self, max_length):
        """Zwraca slowa o dlugosci mniejszej lub rownej podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(word) <= max_length}
        return results if results else "Brak slow o dlugosci mniejszej lub rownej tej wartosci."

    def get_definitions_with_max_length(self, max_length):
        """Zwraca definicje o dlugosci mniejszej lub rownej podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(definition) <= max_length}
        return results if results else "Brak definicji o dlugosci mniejszej lub rownej tej wartosci."

    def get_words_with_length_range(self, min_length, max_length):
        """Zwraca slowa o dlugosci w okreslonym zakresie."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak slow w tym zakresie dlugosci."

    def get_definitions_with_length_range(self, min_length, max_length):
        """Zwraca definicje o dlugosci w okreslonym zakresie."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie dlugosci."

    def get_words_with_length_greater_than(self, length):
        """Zwraca slowa o dlugosci wiekszej niz podana wartosc."""
        results = {word: definition for word, definition in self.words.items() if len(word) > length}
        return results if results else "Brak slow o dlugosci wiekszej niz ta wartosc."

    def get_definitions_with_length_greater_than(self, length):
        """Zwraca definicje o dlugosci wiekszej niz podana wartosc."""
        results = {word: definition for word, definition in self.words.items() if len(definition) > length}
        return results if results else "Brak definicji o dlugosci wiekszej niz ta wartosc."

    def get_words_with_length_less_than(self, length):
        """Zwraca slowa o dlugosci mniejszej niz podana wartosc."""
        results = {word: definition for word, definition in self.words.items() if len(word) < length}
        return results if results else "Brak slow o dlugosci mniejszej niz ta wartosc."

    def get_definitions_with_length_less_than(self, length):
        """Zwraca definicje o dlugosci mniejszej niz podana wartosc."""
        results = {word: definition for word, definition in self.words.items() if len(definition) < length}
        return results if results else "Brak definicji o dlugosci mniejszej niz ta wartosc."

    def get_words_with_length_equal_to(self, length):
        """Zwraca slowa o dlugosci rownej podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(word) == length}
        return results if results else "Brak slow o dlugosci rownej tej wartosci."

    def get_definitions_with_length_equal_to(self, length):
        """Zwraca definicje o dlugosci rownej podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(definition) == length}
        return results if results else "Brak definicji o dlugosci rownej tej wartosci."

    def get_words_with_length_multiple_of(self, multiple):
        """Zwraca slowa o dlugosci bedacej wielokrotnoscia podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(word) % multiple == 0}
        return results if results else "Brak slow o dlugosci bedacej wielokrotnoscia tej wartosci."

    def get_definitions_with_length_multiple_of(self, multiple):
        """Zwraca definicje o dlugosci bedacej wielokrotnoscia podanej wartosci."""
        results = {word: definition for word, definition in self.words.items() if len(definition) % multiple == 0}
        return results if results else "Brak definicji o dlugosci bedacej wielokrotnoscia tej wartosci."

    def get_words_with_repeated_letters(self):
        """Zwraca slowa z powtarzajacymi sie literami."""
        results = {word: definition for word, definition in self.words.items() if len(set(word)) < len(word)}
        return results if results else "Brak slow z powtarzajacymi sie literami."

    def get_words_with_unique_letters(self):
        """Zwraca slowa z unikalnymi literami."""
        results = {word: definition for word, definition in self.words.items() if len(set(word)) == len(word)}
        return results if results else "Brak slow z unikalnymi literami."

    def get_words_with_specific_character(self, character):
        """Zwraca slowa zawierajace okreslony znak."""
        results = {word: definition for word, definition in self.words.items() if character in word}
        return results if results else f"Brak slow zawierajacych znak '{character}'."

    def get_definitions_with_specific_character(self, character):
        """Zwraca definicje zawierajace okreslony znak."""
        results = {word: definition for word, definition in self.words.items() if character in definition}
        return results if results else f"Brak definicji zawierajacych znak '{character}'."

    def get_words_starting_with_vowel(self):
        """Zwraca slowa zaczynajace sie na samogloske."""
        vowels = ('a', 'e', 'i', 'o', 'u', 'y')
        results = {word: definition for word, definition in self.words.items() if word.startswith(vowels)}
        return results if results else "Brak slow zaczynajacych sie na samogloske."

    def get_words_ending_with_vowel(self):
        """Zwraca slowa konczace sie na samogloske."""
        vowels = ('a', 'e', 'i', 'o', 'u', 'y')
        results = {word: definition for word, definition in self.words.items() if word.endswith(vowels)}
        return results if results else "Brak slow konczacych sie na samogloske."

    def get_words_with_length_in_range(self, min_length, max_length):
        """Zwraca slowa o dlugosci w okreslonym zakresie."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak slow w tym zakresie dlugosci."

    def get_definitions_with_length_in_range(self, min_length, max_length):
        """Zwraca definicje o dlugosci w okreslonym zakresie."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie dlugosci."


if __name__ == "__main__":
    dictionary = Dictionary()
    dictionary.add_word("Python", "Jezyk programowania.")
    dictionary.add_word("Java", "Inny jezyk programowania.")
    dictionary.add_word("C++", "Jezyk programowania ogolnego przeznaczenia.")
    dictionary.add_word("JavaScript", "Jezyk skryptowy uzywany w przegladarkach.")
    dictionary.add_word("HTML", "Jezyk znacznikow do tworzenia stron internetowych.")
    dictionary.add_word("CSS", "Kaskadowe arkusze stylow.")
    dictionary.add_word("SQL", "Jezyk zapytan do baz danych.")
    dictionary.add_word("Ruby", "Jezyk programowania dynamicznego.")
    dictionary.add_word("Swift", "Jezyk programowania stworzony przez Apple.")
    dictionary.add_word("Go", "Jezyk programowania stworzony przez Google.")
    
    print("\nWyswietlenie wszystkich slow:")
    dictionary.display_words()
    
    print("\nWyszukiwanie slowa 'Python':")
    print(dictionary.find_word("Python"))
    
    print("\nAktualizacja definicji slowa 'Python':")
    dictionary.update_word("Python", "Jezyk programowania wysokiego poziomu.")
    
    print("\nWyswietlenie wszystkich slow po aktualizacji:")
    dictionary.display_words()
    
    print("\nUsuniecie slowa 'Java':")
    dictionary.remove_word("Java")
    
    print("\nWyswietlenie wszystkich slow po usunieciu:")
    dictionary.display_words()
    
    print("\nZapis do pliku 'dictionary.txt':")
    dictionary.save_to_file("dictionary.txt")
    
    print("\nWyczyszczenie slownika:")
    dictionary.clear_dictionary()
    
    print("\nLadowanie slownika z pliku 'dictionary.txt':")
    dictionary.load_from_file("dictionary.txt")
    
    print("\nWyswietlenie wszystkich slow po zaladowaniu:")
    dictionary.display_words()
    
    print("\nWyszukiwanie slow zaczynajacych sie na 'J':")
    print(dictionary.search_by_prefix("J"))
    
    print("\nWyszukiwanie slow konczacych sie na 'a':")
    print(dictionary.search_by_suffix("a"))
    
    print("\nWyszukiwanie slow zawierajacych 'programowania':")
    print(dictionary.search_by_definition("programowania"))
    
    print("\nLiczba slow w slowniku:")
    print(dictionary.count_words())
    
    print("\nSprawdzenie, czy slownik jest pusty:")
    print(dictionary.is_empty())
    
    print("\nZwrócenie wszystkich slow:")
    print(dictionary.get_all_words())
    
    print("\nZwrócenie wszystkich definicji:")
    print(dictionary.get_definitions())
    
    print("\nZwrócenie definicji slowa 'Python':")
    print(dictionary.get_word_definition("Python"))
    
    print("\nZwrócenie slow zaczynajacych sie na 'C':")
    print(dictionary.get_words_starting_with("C"))
    
    print("\nZwrócenie slow konczacych sie na 's':")
    print(dictionary.get_words_ending_with("s"))
    
    print("\nZwrócenie najdluzszego slowa:")
    print(dictionary.get_longest_word())
    
    print("\nZwrócenie najkrotszego slowa:")
    print(dictionary.get_shortest_word())
    
    print("\nZwrócenie slow o dlugosci 6:")
    print(dictionary.get_words_with_length(6))
    
    print("\nZwrócenie definicji o dlugosci 30:")
    print(dictionary.get_definitions_with_length(30))
    
    print("\nZwrócenie slow o dlugosci wiekszej lub rownej 5:")
    print(dictionary.get_words_with_min_length(5))
    
    print("\nZwrócenie definicji o dlugosci wiekszej lub rownej 10:")
    print(dictionary.get_definitions_with_min_length(10))
    
    print("\nZwrócenie slow o dlugosci mniejszej lub rownej 4:")
    print(dictionary.get_words_with_max_length(4))
    
    print("\nZwrócenie definicji o dlugosci mniejszej lub rownej 20:")
    print(dictionary.get_definitions_with_max_length(20))
    
    print("\nZwrócenie slow o dlugosci w zakresie 4-10:")
    print(dictionary.get_words_with_length_in_range(4, 10))
    
    print("\nZwrócenie definicji o dlugosci w zakresie 10-30:")
    print(dictionary.get_definitions_with_length_in_range(10, 30))
    
    print("\nZwrócenie slow o dlugosci wiekszej niz 3:")
    print(dictionary.get_words_with_length_greater_than(3))
    
    print("\nZwrócenie definicji o dlugosci wiekszej niz 15:")
    print(dictionary.get_definitions_with_length_greater_than(15))
    
    print("\nZwrócenie slow o dlugosci mniejszej niz 5:")
    print(dictionary.get_words_with_length_less_than(5))
    
    print("\nZwrócenie definicji o dlugosci mniejszej niz 10:")
    print(dictionary.get_definitions_with_length_less_than(10))
    
    print("\nZwrócenie slow o dlugosci rownej 5:")
    print(dictionary.get_words_with_length_equal_to(5))
    
    print("\nZwrócenie definicji o dlugosci rownej 20:")
    print(dictionary.get_definitions_with_length_equal_to(20))
    
    print("\nZwrócenie slow o dlugosci bedacej wielokrotnoscia 3:")
    print(dictionary.get_words_with_length_multiple_of(3))
    
    print("\nZwrócenie definicji o dlugosci bedacej wielokrotnoscia 5:")
    print(dictionary.get_definitions_with_length_multiple_of(5))
    
    print("\nZwrócenie slow z powtarzajacymi sie literami:")
    print(dictionary.get_words_with_repeated_letters())
    
    print("\nZwrócenie slow z unikalnymi literami:")
    print(dictionary.get_words_with_unique_letters())
    
    print("\nZwrócenie slow zawierajacych znak 'a':")
    print(dictionary.get_words_with_specific_character('a'))
    
    print("\nZwrócenie definicji zawierajacych znak 'e':")
    print(dictionary.get_definitions_with_specific_character('e'))
    
    print("\nZwrócenie slow zaczynajacych sie na samogloske:")
    print(dictionary.get_words_starting_with_vowel())
    
    print("\nZwrócenie slow konczacych sie na samogloske:")
    print(dictionary.get_words_ending_with_vowel())
    
    print("\nZwrócenie slow o dlugosci w zakresie 3-8:")
    print(dictionary.get_words_with_length_in_range(3, 8))
    
    print("\nZwrócenie definicji o dlugosci w zakresie 10-25:")
    print(dictionary.get_definitions_with_length_in_range(10, 25))