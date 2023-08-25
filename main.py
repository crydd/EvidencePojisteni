from evidence import Evidence

evidence = Evidence()
"""
Uživatelské rozhraní pro práci s evidencí
"""
while True:
    print("----------------------")
    print("Evidence pojištěných")
    print("----------------------")
    print("Vyberte akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    volba = input()

    if volba == "1":
        evidence.pridej()
        print("\nData byla uložena. Pokračujte klávesou Enter...")
        input()

    elif volba == "2":
        evidence.vypis()
        print("\nPokračujte klávesou Enter...")
        input()

    elif volba == "3":
        evidence.vyhledej()
        print("\nPokračujte klávesou Enter...")
        input()

    elif volba == "4":
        print("\nProgram evidence se ukončuje...")
        break

    else:
        print("Neplatná volba, opakujte zadání...")
