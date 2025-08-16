from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class ReportGenerator():
    def __init__(self):
        pass

    def save_report(self,heading,stats):
        c = canvas.Canvas("Report.pdf", pagesize=letter)
        width, height = letter
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 50, heading["title"])
        height = height - 20
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 50, str(heading["date"]))
        c.setFont("Helvetica", 12)
        y = height - 100
        
        for key, value in stats.items():
            c.drawString(100, y, f"{key}")
            data = value
            y -= 20 
            for key,value in data.items():
                c.drawString(100, y, f"{key}: {value}")
                y -= 20 
            y -= 20     
        
        c.save()
        print(f"PDF report saved as Report.pdf")


        

