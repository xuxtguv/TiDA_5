"""

"""

import random

def rzuc_kosci (liczba_kostek):
    return [random.randint(1,6) for _ in range(liczba_kostek)]

def licz_punkty (wynik_rzutu):
    punkty = 0
    for liczba in set(wynik_rzutu):
        if wynik_rzutu.count(liczba) > 1:
            punkty += liczba * wynik_rzutu.count(liczba)
    return punkty

def gra_w_kosci():
    while True:
        while True:
            try:
                liczba_kostek = int(input("Ile kostek chcesz rzucić?(3 - 10)"))
                if 3 <= liczba_kostek <= 10:
                    break
                else:
                    print("Niepoprawna liczba kostek. Podaj liczbę z przedziału 3-10.")
            except ValueError:
                print("Niepoprwana wartość. Wprowadź liczbę całkowitą.")
                
        wynik_rzutu = rzuc_kosci(liczba_kostek)
        
        for i, liczba in enumerate(wynik_rzutu, start=1):
            print(f"Kostka {i}: {liczba}")
            
        punkty = licz_punkty(wynik_rzutu)
        print(f"Liczba uzyskanych punktów: {punkty}")
        
        while True:
            jeszcze_raz = input("Jeszcze raz? (t/n): ").lower()
            if jeszcze_raz in ['t', 'n']:
                break
            else:
                print("Niepoprawna odpowiedż. Wpisz 't' lub 'n'.")
                
        if jeszcze_raz == 'n':
            print("Dziękujemy za grę!")
            break
        
if __name__ == '__main__':
    gra_w_kosci()
