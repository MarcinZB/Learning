###########################################
# Aplikacja oblicza podział rachunku za   #
# mieszkanie dla osób razem mieszkających #
# dodatkowo generowany jest raport        #
# w którym umieszczony zostaje wynik      #
# zwrócony przez program                  #
###########################################
from Bill_Flatmate import Bill, Flatmate
from PDF_GENERATOR import PdfReport, FileSharer

user_pay = float(input("Hello, enter the bill value: "))
user_period = input("What is the period of the bill ?: ")
user_name_1 = input("What is your name ?: ")
user_name_2 = input("What is the name of yours flatmate ?: ")
stay_user_1 = int(input(f"How long did you stay in the house during {user_period}: "))
stay_user_2 = int(input(f"How long did {user_name_2} stay in the house during {user_period}: "))
the_bill = Bill(amount=user_pay, period=user_period)
user_1 = Flatmate(name=user_name_1, days_in_house=stay_user_1)
user_2 = Flatmate(name=user_name_2, days_in_house=stay_user_2)

print(f"{user_name_1} pays: {round(user_1.pays(the_bill, user_2),2)}")
print(f"{user_name_2} pays: {round(user_2.pays(the_bill, user_1),2)}")

pdf_report = PdfReport(filename=f"{user_period}.pdf")
pdf_report.generatePDF(flatmate1=user_1, flatmate2=user_2, bill=the_bill)

# Wygenerowania adresu URL
file_sharer = FileSharer(pdf_report.filename)
linkURL = file_sharer.share()
print(f"Link to pdf bill: {linkURL}")