from fpdf import FPDF


class PdfReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        line_item = lambda fm, fm2 : f"{fm.name}\t\t{round(fm.pays(bill, fm2), 2)}"

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image('assets/house.png', w=30, h=30)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=1, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=0, h=25, txt=line_item(flatmate1, flatmate2), border=1, ln=1)
        pdf.cell(w=0, h=25, txt=line_item(flatmate2, flatmate1), border=1, ln=1)
        pdf.output(self.filename)