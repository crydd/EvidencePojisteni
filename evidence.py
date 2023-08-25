from pojistenec import Pojistenec


class Evidence:

    """
    Třída reprezentující evidenci a její metody
    """
    def __init__(self):
        self.pojistenci = list()  # seznam pojištěnců

    def pridej(self):
        """
        Uloží do seznamu nového pojištěnce.
        """
        jmeno = input("\nZadejte jméno: ")  # vyžádá si vstup
        while not jmeno or not jmeno.isalpha():  # zajistí, aby vstup nezůstal prázdný nebo nesprávně vyplněn
            if not jmeno:
                print("Jméno musí být vyplněno.")
            else:
                print("Jméno může obsahovat pouze písmena.")
            jmeno = input("Zadejte jméno: ")

        prijmeni = input("Zadejte příjmení: ")
        while not prijmeni or not prijmeni.isalpha():
            if not prijmeni:
                print("Příjmení musí být vyplněno.")
            else:
                print("Příjmení může obsahovat pouze písmena.")
            prijmeni = input("Zadejte příjmení: ")

        vek = input("Zadejte věk: ")
        while not vek or not vek.isdigit():
            if not vek:
                print("Věk musí být vyplněn.")
            else:
                print("Věk může obsahovat pouze číslice.")
            vek = input("Zadejte Věk: ")

        tel_cislo = input("Zadejte telefonní číslo: ")
        while not tel_cislo or not tel_cislo.isdigit():
            if not tel_cislo:
                print("Telefonní číslo musí být vyplněno.")
            else:
                print("Telefonní číslo může obsahovat pouze číslice.")
            tel_cislo = input("Zadejte telefonní číslo: ")

        pojistenec = Pojistenec(jmeno.capitalize(), prijmeni.capitalize(), vek.capitalize(), tel_cislo.capitalize())
        self.pojistenci.append(pojistenec)  # přidá nového pojištěnce na konec seznamu

    def vypis(self):
        """
        Vypíše seznam všech zadaných pojištěnců
        """
        print()
        if len(self.pojistenci) == 0:
            print("\nSeznam pojištěnců je prázdný.")
        else:
            for i in self.pojistenci:
                print(i)

    def vyhledej(self):
        """
        Vyhledá v seznamu konkrétního pojištence podle jména a příjmení
        """
        if not self.pojistenci:
            print("Seznam pojištěnců je prázdný je prázdný.")
            return

        hledane_jmeno = input("\nZadejte jméno pojištěného: ")
        while not hledane_jmeno:
            print("Jméno musí být vyplněno.")
            hledane_jmeno = input("Zadejte jméno pojištěného: ")

        hledane_prijmeni = input("Zadejte přijmení: ")
        while not hledane_prijmeni:
            print("Příjmení musí být vyplněno.")
            hledane_prijmeni = input("Zadejte příjmení: ")
        print()

        nalezen = False
        for i in self.pojistenci:  # prohledá seznam a vypíše všechny pojištěnce hledaného jména + příjmení
            if i.jmeno == hledane_jmeno.capitalize() and i.prijmeni == hledane_prijmeni.capitalize():
                print(i)
                nalezen = True
        if not nalezen:
            print("\nPojištěnec nebyl nalezen.")
