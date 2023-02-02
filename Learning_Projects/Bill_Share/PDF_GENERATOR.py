from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """
    Klasa odpowiada za plik pdf w którym znajdują się wszystkie
    informacje.
    """

    def __init__(self, filename):
        self.filename = filename
        
    
    def generatePDF(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Ikonka
        pdf.image("Learning_Projects/Bill_Share/files/house.png", w = 30, h = 30)
        #Tytuł
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Zmiana czcionki
        pdf.set_font(family="Times", size = 14, style = "B")
        #Dane rozliczeniowe - Okres 
        pdf.cell(w = 100, h=60, txt="Period: ", border=0)
        pdf.cell(w = 150, h=60, txt=bill.period, border = 0, ln = 1)

        #Zmiana czcionki
        pdf.set_font(family="Times", size = 12)
        #Ile łącznie do zapłaty
        pdf.cell(w = 100, h = 20, txt = "To pay: ", border=0)
        pdf.cell(w= 150, h = 20, txt = str(round((bill.amount),2)), border=0, ln=1)

        #Dane rozliczeniowe - podział na współlokatorów 
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, border=0, ln=1)
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, border=0, ln=1)
        
        os.chdir("Learning_Projects/Bill_Share/files") #zmiana folderu w którym kod się wykonuje
        pdf_final = pdf.output(self.filename)
        #Automatyczne wyświetlanie wygenerowanego pliku
        webbrowser.open(self.filename)

        # W przypadku Linuxa oraz MacIOS należy wygenerować ściężkę samemu
        # webbrowser.open('file://'+os.path.realpath(self.filename))