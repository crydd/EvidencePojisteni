class Pojistenec:
    """
    Třída reprezentující pojištěnce v evidenci.
    """
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):  # vrací textovou reprezentaci pojištěnce, formátováno pro přehlednější výstup
        return f"{self.jmeno:15s}{self.prijmeni:15s}{self.vek:5s}{self.tel_cislo}"
