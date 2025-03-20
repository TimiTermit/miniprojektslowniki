class Slownik:
    def __init__(self):
        self.slowka = {}

    def dodaj_slowo(self, slowo, definicja):
        """Dodaje nowe słowo i jego definicję do słownika."""
        if slowo in self.slowka:
            print(f"Słowo '{slowo}' już istnieje w słowniku.")
        else:
            self.slowka[slowo] = definicja
            print(f"Słowo '{slowo}' zostało dodane.")

    def usun_slowo(self, slowo):
        """Usuwa słowo ze słownika."""
        if slowo in self.slowka:
            del self.slowka[slowo]
            print(f"Słowo '{slowo}' zostało usunięte.")
        else:
            print(f"Słowo '{slowo}' nie istnieje w słowniku.")

    def znajdz_slowo(self, slowo):
        """Zwraca definicję słowa, jeśli istnieje w słowniku."""
        return self.slowka.get(slowo, "Słowo nie znalezione.")

    def wyswietl_slowka(self):
        """Wyświetla wszystkie słowa i ich definicje w słowniku."""
        if not self.slowka:
            print("Słownik jest pusty.")
        else:
            for slowo, definicja in self.slowka.items():
                print(f"{slowo}: {definicja}")

    def aktualizuj_slowo(self, slowo, nowa_definicja):
        """Aktualizuje definicję istniejącego słowa."""
        if slowo in self.slowka:
            self.slowka[slowo] = nowa_definicja
            print(f"Definicja słowa '{slowo}' została zaktualizowana.")
        else:
            print(f"Słowo '{slowo}' nie istnieje w słowniku.")

    def wyczysc_slownik(self):
        """Czyści wszystkie słowa w słowniku."""
        self.slowka.clear()
        print("Słownik został wyczyszczony.")

    def zapisz_do_pliku(self, nazwa_pliku):
        """Zapisuje słownik do pliku."""
        with open(nazwa_pliku, 'w') as plik:
            for slowo, definicja in self.slowka.items():
                plik.write(f"{slowo}:{definicja}\n")
        print(f"Słownik został zapisany do pliku '{nazwa_pliku}'.")

    def zaladuj_z_pliku(self, nazwa_pliku):
        """Ładuje słownik z pliku."""
        try:
            with open(nazwa_pliku, 'r') as plik:
                for linia in plik:
                    slowo, definicja = linia.strip().split(':', 1)
                    self.slowka[slowo] = definicja
            print(f"Słownik został załadowany z pliku '{nazwa_pliku}'.")
        except FileNotFoundError:
            print(f"Plik '{nazwa_pliku}' nie został znaleziony.")
        except Exception as e:
            print(f"Wystąpił błąd podczas ładowania pliku: {e}")

    def szukaj_po_prefiksie(self, prefiks):
        """Zwraca słowa, które zaczynają się od danego prefiksu."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if slowo.startswith(prefiks)}
        return wyniki if wyniki else "Brak słów zaczynających się od tego prefiksu."

    def szukaj_po_sufiksie(self, sufiks):
        """Zwraca słowa, które kończą się na dany sufiks."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if slowo.endswith(sufiks)}
        return wyniki if wyniki else "Brak słów kończących się na ten sufiks."

    def szukaj_po_definicji(self, termin):
        """Zwraca słowa, które zawierają dany termin w definicji."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if termin in definicja}
        return wyniki if wyniki else "Brak słów zawierających ten termin w definicji."

    def liczba_slow(self):
        """Zwraca liczbę słów w słowniku."""
        return len(self.slowka)

    def jest_pusty(self):
        """Sprawdza, czy słownik jest pusty."""
        return len(self.slowka) == 0

    def pobierz_wszystkie_slowka(self):
        """Zwraca listę wszystkich słów w słowniku."""
        return list(self.slowka.keys())

    def pobierz_definicje(self):
        """Zwraca listę wszystkich definicji w słowniku."""
        return list(self.slowka.values())

    def pobierz_definicje_slowka(self, slowo):
        """Zwraca definicję danego słowa lub informację, że słowo nie istnieje."""
        return self.slowka.get(slowo, "Słowo nie istnieje w słowniku.")

    def pobierz_slowka_zaczynajace_sie_na(self, litera):
        """Zwraca słowa zaczynające się na daną literę."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if slowo.startswith(litera)}
        return wyniki if wyniki else "Brak słów zaczynających się na tę literę."

    def pobierz_slowka_konczace_sie_na(self, litera):
        """Zwraca słowa kończące się na daną literę."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if slowo.endswith(litera)}
        return wyniki if wyniki else "Brak słów kończących się na tę literę."

    def pobierz_liczbe_slow(self):
        """Zwraca liczbę słów w słowniku."""
        return len(self.slowka)

    def pobierz_definicje_zawierajace(self, termin):
        """Zwraca definicje, które zawierają dany termin."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if termin in definicja}
        return wyniki if wyniki else "Brak definicji zawierających ten termin."

    def pobierz_wszystkie_wpisy(self):
        """Zwraca wszystkie wpisy w słowniku jako listę krotek."""
        return list(self.slowka.items())

    def pobierz_posortowane_slowka(self):
        """Zwraca posortowaną listę słów w słowniku."""
        return sorted(self.slowka.keys())

    def pobierz_posortowane_definicje(self):
        """Zwraca posortowaną listę definicji w słowniku."""
        return sorted(self.slowka.values())

    def pobierz_najdluzsze_slowo(self):
        """Zwraca najdłuższe słowo w słowniku."""
        if not self.slowka:
            return "Słownik jest pusty."
        najdluzsze_slowo = max(self.slowka.keys(), key=len)
        return najdluzsze_slowo, self.slowka[najdluzsze_slowo]

    def pobierz_najkrotsze_slowo(self):
        """Zwraca najkrótsze słowo w słowniku."""
        if not self.slowka:
            return "Słownik jest pusty."
        najkrotsze_slowo = min(self.slowka.keys(), key=len)
        return najkrotsze_slowo, self.slowka[najkrotsze_slowo]

    def pobierz_dlugosc_slowka(self, slowo):
        """Zwraca długość danego słowa."""
        return len(slowo) if slowo in self.slowka else "Słowo nie istnieje w słowniku."

    def pobierz_dlugosc_definicji(self, slowo):
        """Zwraca długość definicji danego słowa."""
        return len(self.slowka[slowo]) if slowo in self.slowka else "Słowo nie istnieje w słowniku."

    def pobierz_slowka_o_dlugosci(self, dlugosc):
        """Zwraca słowa o określonej długości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) == dlugosc}
        return wyniki if wyniki else "Brak słów o tej długości."

    def pobierz_definicje_o_dlugosci(self, dlugosc):
        """Zwraca definicje o określonej długości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) == dlugosc}
        return wyniki if wyniki else "Brak definicji o tej długości."

    def pobierz_slowka_o_min_dlugosci(self, min_dlugosc):
        """Zwraca słowa o długości większej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) >= min_dlugosc}
        return wyniki if wyniki else "Brak słów o długości większej lub równej tej wartości."

    def pobierz_definicje_o_min_dlugosci(self, min_dlugosc):
        """Zwraca definicje o długości większej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) >= min_dlugosc}
        return wyniki if wyniki else "Brak definicji o długości większej lub równej tej wartości."

    def pobierz_slowka_o_max_dlugosci(self, max_dlugosc):
        """Zwraca słowa o długości mniejszej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów o długości mniejszej lub równej tej wartości."

    def pobierz_definicje_o_max_dlugosci(self, max_dlugosc):
        """Zwraca definicje o długości mniejszej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji o długości mniejszej lub równej tej wartości."

    def pobierz_slowka_zaczynajace_sie_na_samogoske(self):
        """Zwraca słowa zaczynające się na samogłoskę."""
        samogoski = ('a', 'e', 'i', 'o', 'u', 'y')
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if slowo.startswith(samogoski)}
        return wyniki if wyniki else "Brak słów zaczynających się na samogłoskę."

    def pobierz_slowka_konczace_sie_na_samogoske(self):
        """Zwraca słowa kończące się na samogłoskę."""
        samogoski = ('a', 'e', 'i', 'o', 'u', 'y')
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if slowo.endswith(samogoski)}
        return wyniki if wyniki else "Brak słów kończących się na samogłoskę."

    def pobierz_slowka_z_powtarzajacymi_sie_literami(self):
        """Zwraca słowa z powtarzającymi się literami."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(set(slowo)) < len(slowo)}
        return wyniki if wyniki else "Brak słów z powtarzającymi się literami."

    def pobierz_slowka_z_unikalnymi_literami(self):
        """Zwraca słowa z unikalnymi literami."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(set(slowo)) == len(slowo)}
        return wyniki if wyniki else "Brak słów z unikalnymi literami."

    def pobierz_slowka_z_okreslonym_znakiem(self, znak):
        """Zwraca słowa zawierające określony znak."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if znak in slowo}
        return wyniki if wyniki else f"Brak słów zawierających znak '{znak}'."

    def pobierz_definicje_z_okreslonym_znakiem(self, znak):
        """Zwraca definicje zawierające określony znak."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if znak in definicja}
        return wyniki if wyniki else f"Brak definicji zawierających znak '{znak}'."

    def pobierz_slowka_o_dlugosci_zakres(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_zakres(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_wiekszej_niz(self, dlugosc):
        """Zwraca słowa o długości większej niż podana wartość."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) > dlugosc}
        return wyniki if wyniki else "Brak słów o długości większej niż ta wartość."

    def pobierz_definicje_o_dlugosci_wiekszej_niz(self, dlugosc):
        """Zwraca definicje o długości większej niż podana wartość."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) > dlugosc}
        return wyniki if wyniki else "Brak definicji o długości większej niż ta wartość."

    def pobierz_slowka_o_dlugosci_mniejszej_niz(self, dlugosc):
        """Zwraca słowa o długości mniejszej niż podana wartość."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) < dlugosc}
        return wyniki if wyniki else "Brak słów o długości mniejszej niż ta wartość."

    def pobierz_definicje_o_dlugosci_mniejszej_niz(self, dlugosc):
        """Zwraca definicje o długości mniejszej niż podana wartość."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) < dlugosc}
        return wyniki if wyniki else "Brak definicji o długości mniejszej niż ta wartość."

    def pobierz_slowka_o_dlugosci_rownej(self, dlugosc):
        """Zwraca słowa o długości równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) == dlugosc}
        return wyniki if wyniki else "Brak słów o długości równej tej wartości."

    def pobierz_definicje_o_dlugosci_rownej(self, dlugosc):
        """Zwraca definicje o długości równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) == dlugosc}
        return wyniki if wyniki else "Brak definicji o długości równej tej wartości."

    def pobierz_slowka_o_dlugosci_wielokrotnosci(self, wielokrotnosc):
        """Zwraca słowa o długości będącej wielokrotnością podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) % wielokrotnosc == 0}
        return wyniki if wyniki else "Brak słów o długości będącej wielokrotnością tej wartości."

    def pobierz_definicje_o_dlugosci_wielokrotnosci(self, wielokrotnosc):
        """Zwraca definicje o długości będącej wielokrotnością podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) % wielokrotnosc == 0}
        return wyniki if wyniki else "Brak definicji o długości będącej wielokrotnością tej wartości."

    def pobierz_slowka_o_dlugosci_nie_rownej(self, dlugosc):
        """Zwraca słowa o długości różnej od podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) != dlugosc}
        return wyniki if wyniki else "Brak słów o długości różnej od tej wartości."

    def pobierz_definicje_o_dlugosci_nie_rownej(self, dlugosc):
        """Zwraca definicje o długości różnej od podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) != dlugosc}
        return wyniki if wyniki else "Brak definicji o długości różnej od tej wartości."

    def pobierz_slowka_o_dlugosci_w_liscie(self, dlugosci):
        """Zwraca słowa o długości znajdującej się w podanej liście."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) in dlugosci}
        return wyniki if wyniki else "Brak słów o długości w podanej liście."

    def pobierz_definicje_o_dlugosci_w_liscie(self, dlugosci):
        """Zwraca definicje o długości znajdującej się w podanej liście."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) in dlugosci}
        return wyniki if wyniki else "Brak definicji o długości w podanej liście."

    def pobierz_slowka_o_dlugosci_wiekszej_lub_rownej(self, dlugosc):
        """Zwraca słowa o długości większej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) >= dlugosc}
        return wyniki if wyniki else "Brak słów o długości większej lub równej tej wartości."

    def pobierz_definicje_o_dlugosci_wiekszej_lub_rownej(self, dlugosc):
        """Zwraca definicje o długości większej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) >= dlugosc}
        return wyniki if wyniki else "Brak definicji o długości większej lub równej tej wartości."

    def pobierz_slowka_o_dlugosci_mniejszej_lub_rownej(self, dlugosc):
        """Zwraca słowa o długości mniejszej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(slowo) <= dlugosc}
        return wyniki if wyniki else "Brak słów o długości mniejszej lub równej tej wartości."

    def pobierz_definicje_o_dlugosci_mniejszej_lub_rownej(self, dlugosc):
        """Zwraca definicje o długości mniejszej lub równej podanej wartości."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if len(definicja) <= dlugosc}
        return wyniki if wyniki else "Brak definicji o długości mniejszej lub równej tej wartości."

    def pobierz_slowka_o_dlugosci_w_zakresie_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(slowo) < max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(definicja) < max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_inclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (włącznie)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_inclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (włącznie)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_exclusive_inclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min i włącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_exclusive_inclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min i włącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_inclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min i wyłącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(slowo) < max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_inclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min i wyłącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(definicja) < max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_exclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla obu)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(slowo) < max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_exclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla obu)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(definicja) < max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_inclusive_inclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla obu)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_inclusive_inclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla obu)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_exclusive_inclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_exclusive_inclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i wyłącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_inclusive_exclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(slowo) < max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_inclusive_exclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (włącznie dla min, wyłącznie dla max i wyłącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc <= len(definicja) < max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."

    def pobierz_slowka_o_dlugosci_w_zakresie_exclusive_inclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca słowa o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(slowo) <= max_dlugosc}
        return wyniki if wyniki else "Brak słów w tym zakresie długości."

    def pobierz_definicje_o_dlugosci_w_zakresie_exclusive_inclusive_exclusive(self, min_dlugosc, max_dlugosc):
        """Zwraca definicje o długości w określonym zakresie (wyłącznie dla min, włącznie dla max i włącznie dla max)."""
        wyniki = {slowo: definicja for slowo, definicja in self.slowka.items() if min_dlugosc < len(definicja) <= max_dlugosc}
        return wyniki if wyniki else "Brak definicji w tym zakresie długości."
