###########################################
# Aplikacja oblicza podział rachunku za   #
# mieszkanie dla osób razem mieszkających #
# dodatkowo generowany jest raport        #
# w którym umieszczony zostaje wynik      #
# zwrócony przez program                  #
###########################################

import fpdf as fp
 
class Bill:
    """
    Objekt reprezentuje dane dotyczące rachunku, takie jak
    cena oraz okres rozliczeniowy
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Klasa reprezentuje obiekt osoby składającej się na rachunek
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def pays(self, bill, flatmate2 ):
        weight = self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        to_pay = bill.amount*weight
        return to_pay


class PdfReport:
    """
    Klasa odpowiada za plik pdf w którym znajdują się wszystkie
    informacje.
    """

    def __init__(self, filename):
        self.filename = filename
    
    def generatePDF(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

