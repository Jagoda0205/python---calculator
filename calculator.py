# Kalkulator w Pythonie – projekt do portfolio
# Autor: Jagoda
# Opis: Prosty kalkulator działający w pętli, obsługa +, -, *, /, możliwość zakończenia program wpisując 'exit'

while True:
    # Pobranie pierwszej liczby
    wejscie1 = input("Podaj pierwszą liczbę (albo 'exit'): ")
    if wejscie1.lower() == "exit":
        print("Koniec programu. Do zobaczenia!")
        break
    numer1 = float(wejscie1)  # float pozwala wpisywać liczby dziesiętne

    # Pobranie drugiej liczby
    wejscie2 = input("Podaj drugą liczbę (albo 'exit'): ")
    if wejscie2.lower() == "exit":
        print("Koniec programu. Do zobaczenia!")
        break
    numer2 = float(wejscie2)

    # Wybór działania
    dzialanie = input("Wybierz działanie (+, -, *, /) lub wpisz 'exit': ")
    if dzialanie.lower() == "exit":
        print("Koniec programu. Do zobaczenia!")
        break

    # Wykonanie działania
    if dzialanie == "+":
        wynik = numer1 + numer2
    elif dzialanie == "-":
        wynik = numer1 - numer2
    elif dzialanie == "*":
        wynik = numer1 * numer2
    elif dzialanie == "/":
        if numer2 != 0:
            wynik = numer1 / numer2
        else:
            print("Nie można dzielić przez zero!")
            continue  # wracamy na początek pętli
    else:
        print("Nieprawidłowe działanie! Spróbuj jeszcze raz.")
        continue

    # Wyświetlenie wyniku w czytelnej formie
    print(f"{numer1} {dzialanie} {numer2} = {wynik}\n")
