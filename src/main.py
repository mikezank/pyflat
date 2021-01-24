import webbrowser
import os

from src.flat import Bill, Flatmate
from src.report import PdfReport

bill_amount = input("Bill amount: ")
bill_period = input("Bill period: ")
bill = Bill(amount=int(bill_amount), period=bill_period)

name1 = input("First flatmate name: ")
days1 = input("Days in house: ")
name2 = input("Second flatmate name: ")
days2 = input("Days in house: ")
john = Flatmate(name=name1, days_in_house=float(days1))
mary = Flatmate(name=name2, days_in_house=float(days2))

pdf = PdfReport(filename='assets/bill.pdf')
pdf.generate(john, mary, bill)
url = f'file://{os.path.realpath("assets/bill.pdf")}'
print(url)
webbrowser.open(url)
