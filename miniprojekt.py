class Dictionary:
    def __init__(self):
        self.words = {}

    def add_word(self, word, definition):
        """Dodaje nowe słowo i jego definicję do słownika."""
        if word in self.words:
            print(f"Słowo '{word}' już istnieje w słowniku.")
        else:
            self.words[word] = definition
            print(f"Słowo '{word}' zostało dodane.")

    def remove_word(self, word):
        """Usuwa słowo ze słownika."""
        if word in self.words:
            del self.words[word]
            print(f"Słowo '{word}' zostało usunięte.")
        else:
            print(f"Słowo '{word}' nie istnieje w słowniku.")

    def find_word(self, word):
        """Zwraca definicję słowa, jeśli istnieje w słowniku."""
        return self.words.get(word, "Słowo nie znalezione.")

    def display_words(self):
        """Wyświetla wszystkie słowa i ich definicje w słowniku."""
        if not self.words:
            print("Słownik jest pusty.")
        else:
            for word, definition in self.words.items():
                print(f"{word}: {definition}")

    def update_word(self, word, new_definition):
        """Aktualizuje definicję istniejącego słowa."""
        if word in self.words:
            self.words[word] = new_definition
            print(f"Definicja słowa '{word}' została zaktualizowana.")
        else:
            print(f"Słowo '{word}' nie istnieje w słowniku.")

    def clear_dictionary(self):
        """Czyści wszystkie słowa w słowniku."""
        self.words.clear()
        print("Słownik został wyczyszczony.")

    def save_to_file(self, filename):
        """Zapisuje słownik do pliku."""
        with open(filename, 'w') as file:
            for word, definition in self.words.items():
                file.write(f"{word}:{definition}\n")
        print(f"Słownik został zapisany do pliku '{filename}'.")

    def load_from_file(self, filename):
        """Ładuje słownik z pliku."""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    word, definition = line.strip().split(':', 1)
                    self.words[word] = definition
            print(f"Słownik został załadowany z pliku '{filename}'.")
        except FileNotFoundError:
            print(f"Plik '{filename}' nie został znaleziony.")
        except Exception as e:
            print(f"Wystąpił błąd podczas ładowania pliku: {e}")

    def search_by_prefix(self, prefix):
        """Zwraca słowa, które zaczynają się od danego prefiksu."""
        results = {word: definition for word, definition in self.words.items() if word.startswith(prefix)}
        return results if results else "Brak słów zaczynających się od tego prefiksu."

    def search_by_suffix(self, suffix):
        """Zwraca słowa, które kończą się na dany sufiks."""
        results = {word: definition for word, definition in self.words.items() if word.endswith(suffix)}
        return results if results else "Brak słów kończących się na ten sufiks."

    def search_by_definition(self, search_term):
        """Zwraca słowa, które zawierają dany termin w definicji."""
        results = {word: definition for word, definition in self.words.items() if search_term in definition}
        return results if results else "Brak słów zawierających ten termin w definicji."

    def count_words(self):
        """Zwraca liczbę słów w słowniku."""
        return len(self.words)

    def is_empty(self):
        """Sprawdza, czy słownik jest pusty."""
        return len(self.words) == 0

    def get_all_words(self):
        """Zwraca listę wszystkich słów w słowniku."""
        return list(self.words.keys())

    def get_definitions(self):
        """Zwraca listę wszystkich definicji w słowniku."""
        return list(self.words.values())

    def get_word_definition(self, word):
        """Zwraca definicję danego słowa lub informację, że słowo nie istnieje."""
        return self.words.get(word, " Słowo nie istnieje w słowniku.")

    def get_words_starting_with(self, letter):
        """Zwraca słowa zaczynające się na daną literę."""
        results = {word: definition for word, definition in self.words.items() if word.startswith(letter)}
        return results if results else "Brak słów zaczynających się na tę literę."

    def get_words_ending_with(self, letter):
        """Zwraca słowa kończące się na daną literę."""
        results = {word: definition for word, definition in self.words.items() if word.endswith(letter)}
        return results if results else "Brak słów kończących się na tę literę."

    def get_word_count(self):
        """Zwraca liczbę słów w słowniku."""
        return len(self.words)

    def get_definitions_containing(self, term):
        """Zwraca definicje, które zawierają dany termin."""
        results = {word: definition for word, definition in self.words.items() if term in definition}
        return results if results else "Brak definicji zawierających ten termin."

    def get_all_entries(self):
        """Zwraca wszystkie wpisy w słowniku jako listę krotek."""
        return list(self.words.items())

    def get_sorted_words(self):
        """Zwraca posortowaną listę słów w słowniku."""
        return sorted(self.words.keys())

    def get_sorted_definitions(self):
        """Zwraca posortowaną listę definicji w słowniku."""
        return sorted(self.words.values())

    def get_longest_word(self):
        """Zwraca najdłuższe słowo w słowniku."""
        if not self.words:
            return "Słownik jest pusty."
        longest_word = max(self.words.keys(), key=len)
        return longest_word, self.words[longest_word]

    def get_shortest_word(self):
        """Zwraca najkrótsze słowo w słowniku."""
        if not self.words:
            return "Słownik jest pusty."
        shortest_word = min(self.words.keys(), key=len)
        return shortest_word, self.words[shortest_word]

    def get_word_length(self, word):
        """Zwraca długość danego słowa."""
        return len(word) if word in self.words else "Słowo nie istnieje w słowniku."

    def get_definition_length(self, word):
        """Zwraca długość definicji danego słowa."""
        return len(self.words[word]) if word in self.words else "Słowo nie istnieje w słowniku."

    def get_words_with_length(self, length):
        """Zwraca słowa o określonej długości."""
        results = {word: definition for word, definition in self.words.items() if len(word) == length}
        return results if results else "Brak słów o tej długości."

    def get_definitions_with_length(self, length):
        """Zwraca definicje o określonej długości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) == length}
        return results if results else "Brak definicji o tej długości."

    def get_words_with_min_length(self, min_length):
        """Zwraca słowa o długości większej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) >= min_length}
        return results if results else "Brak słów o długości większej lub równej tej wartości."

    def get_definitions_with_min_length(self, min_length):
        """Zwraca definicje o długości większej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) >= min_length}
        return results if results else "Brak definicji o długości większej lub równej tej wartości."

    def get_words_with_max_length(self, max_length):
        """Zwraca słowa o długości mniejszej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) <= max_length}
        return results if results else "Brak słów o długości mniejszej lub równej tej wartości."

    def get_definitions_with_max_length(self, max_length):
        """Zwraca definicje o długości mniejszej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) <= max_length}
        return results if results else "Brak definicji o długości mniejszej lub równej tej wartości."

    def get_words_starting_with_vowel(self):
        """Zwraca słowa zaczynające się na samogłoskę."""
        vowels = ('a', 'e', 'i', 'o', 'u', 'y')
        results = {word: definition for word, definition in self.words.items() if word.startswith(vowels)}
        return results if results else "Brak słów zaczynających się na samogłoskę."

    def get_words_ending_with_vowel(self):
        """Zwraca słowa kończące się na samogłoskę."""
        vowels = ('a', 'e', 'i', 'o', 'u', 'y')
        results = {word: definition for word, definition in self.words.items() if word.endswith(vowels)}
        return results if results else "Brak słów kończących się na samogłoskę."

    def get_words_with_repeated_letters(self):
        """Zwraca słowa z powtarzającymi się literami."""
        results = {word: definition for word, definition in self.words.items() if len(set(word)) < len(word)}
        return results if results else "Brak słów z powtarzającymi się literami."

    def get_words_with_unique_letters(self):
        """Zwraca słowa z unikalnymi literami."""
        results = {word: definition for word, definition in self.words.items() if len(set(word)) == len(word)}
        return results if results else "Brak słów z unikalnymi literami."

    def get_words_with_specific_character(self, character):
        """Zwraca słowa zawierające określony znak."""
        results = {word: definition for word, definition in self.words.items() if character in word}
        return results if results else f"Brak słów zawierających znak '{character}'."

    def get_definitions_with_specific_character(self, character):
        """Zwraca definicje zawierające określony znak."""
        results = {word: definition for word, definition in self.words.items() if character in definition}
        return results if results else f"Brak definicji zawierających znak '{character}'."

    def get_words_with_length_range(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_range(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_greater_than(self, length):
        """Zwraca słowa o długości większej niż podana wartość."""
        results = {word: definition for word, definition in self.words.items() if len(word) > length}
        return results if results else "Brak słów o długości większej niż ta wartość."

    def get_definitions_with_length_greater_than(self, length):
        """Zwraca definicje o długości większej niż podana wartość."""
        results = {word: definition for word, definition in self.words.items() if len(definition) > length}
        return results if results else "Brak definicji o długości większej niż ta wartość."

    def get_words_with_length_less_than(self, length):
        """Zwraca słowa o długości mniejszej niż podana wartość."""
        results = {word: definition for word, definition in self.words.items() if len(word) < length}
        return results if results else "Brak słów o długości mniejszej niż ta wartość."

    def get_definitions_with_length_less_than(self, length):
        """Zwraca definicje o długości mniejszej niż podana wartość."""
        results = {word: definition for word, definition in self.words.items() if len(definition) < length}
        return results if results else "Brak definicji o długości mniejszej niż ta wartość."

    def get_words_with_length_equal_to(self, length):
        """Zwraca słowa o długości równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) == length}
        return results if results else "Brak słów o długości równej tej wartości."

    def get_definitions_with_length_equal_to(self, length):
        """Zwraca definic je o długości równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) == length}
        return results if results else "Brak definicji o długości równej tej wartości."

    def get_words_with_length_multiple_of(self, multiple):
        """Zwraca słowa o długości będącej wielokrotnością podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) % multiple == 0}
        return results if results else "Brak słów o długości będącej wielokrotnością tej wartości."

    def get_definitions_with_length_multiple_of(self, multiple):
        """Zwraca definicje o długości będącej wielokrotnością podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) % multiple == 0}
        return results if results else "Brak definicji o długości będącej wielokrotnością tej wartości."

    def get_words_with_length_not_equal_to(self, length):
        """Zwraca słowa o długości różnej od podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) != length}
        return results if results else "Brak słów o długości różnej od tej wartości."

    def get_definitions_with_length_not_equal_to(self, length):
        """Zwraca definicje o długości różnej od podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) != length}
        return results if results else "Brak definicji o długości różnej od tej wartości."

    def get_words_with_length_in_list(self, lengths):
        """Zwraca słowa o długości znajdującej się w podanej liście."""
        results = {word: definition for word, definition in self.words.items() if len(word) in lengths}
        return results if results else "Brak słów o długości w podanej liście."

    def get_definitions_with_length_in_list(self, lengths):
        """Zwraca definicje o długości znajdującej się w podanej liście."""
        results = {word: definition for word, definition in self.words.items() if len(definition) in lengths}
        return results if results else "Brak definicji o długości w podanej liście."

    def get_words_with_length_greater_than_or_equal_to(self, length):
        """Zwraca słowa o długości większej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) >= length}
        return results if results else "Brak słów o długości większej lub równej tej wartości."

    def get_definitions_with_length_greater_than_or_equal_to(self, length):
        """Zwraca definicje o długości większej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) >= length}
        return results if results else "Brak definicji o długości większej lub równej tej wartości."

    def get_words_with_length_less_than_or_equal_to(self, length):
        """Zwraca słowa o długości mniejszej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(word) <= length}
        return results if results else "Brak słów o długości mniejszej lub równej tej wartości."

    def get_definitions_with_length_less_than_or_equal_to(self, length):
        """Zwraca definicje o długości mniejszej lub równej podanej wartości."""
        results = {word: definition for word, definition in self.words.items() if len(definition) <= length}
        return results if results else "Brak definicji o długości mniejszej lub równej tej wartości."

    def get_words_with_length_in_range_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Br ak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_list_exclusive(self, lengths):
        """Zwraca słowa o długości znajdującej się w podanej liście (wyłącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(word) not in lengths}
        return results if results else "Brak słów o długości w podanej liście."

    def get_definitions_with_length_in_list_exclusive(self, lengths):
        """Zwraca definicje o długości znajdującej się w podanej liście (wyłącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(definition) not in lengths}
        return results if results else "Brak definicji o długości w podanej liście."

    def get_words_with_length_in_list_inclusive(self, lengths):
        """Zwraca słowa o długości znajdującej się w podanej liście (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(word) in lengths}
        return results if results else "Brak słów o długości w podanej liście."

    def get_definitions_with_length_in_list_inclusive(self, lengths):
        """Zwraca definicje o długości znajdującej się w podanej liście (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(definition) in lengths}
        return results if results else "Brak definicji o długości w podanej liście."

    def get_words_with_length_greater_than_or_equal_to_inclusive(self, length):
        """Zwraca słowa o długości większej lub równej podanej wartości (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(word) >= length}
        return results if results else "Brak słów o długości większej lub równej tej wartości."

    def get_definitions_with_length_greater_than_or_equal_to_inclusive(self, length):
        """Zwraca definicje o długości większej lub równej podanej wartości (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(definition) >= length}
        return results if results else "Brak definicji o długości większej lub równej tej wartości."

    def get_words_with_length_less_than_or_equal_to_inclusive(self, length):
        """Zwraca słowa o długości mniejszej lub równej podanej wartości (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(word) <= length}
        return results if results else "Brak słów o długości mniejszej lub równej tej wartości."

    def get_definitions_with_length_less_than_or_equal_to_inclusive(self, length):
        """Zwraca definicje o długości mniejszej lub równej podanej wartości (włącznie)."""
        results = {word: definition for word, definition in self.words.items() if len(definition) <= length}
        return results if results else "Brak definicji o długości mniejszej lub równej tej wartości."

    def get_words_with_length_in_range_exclusive_inclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_inclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_inclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_inclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_inclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_inclusive(self, min_length, max_length):
        """Zwraca słowa o długości w okre ślonym zakresie (włącznie dla min, wyłącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_inclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive_inclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu, włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive_inclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu, włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca defin icje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) <= max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_inclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) <= max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_exclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        results = {word: definition for word, definition in self.words.items() if min_length < len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."

    def get_words_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(word) < max_length}
        return results if results else "Brak słów w tym zakresie długości."

    def get_definitions_with_length_in_range_inclusive_exclusive_exclusive(self, min_length, max_length):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        results = {word: definition for word, definition in self.words.items() if min_length <= len(definition) < max_length}
        return results if results else "Brak definicji w tym zakresie długości."
