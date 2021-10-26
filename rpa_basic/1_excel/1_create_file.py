from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "NadoSheet"
wb.save("sample.xlsx")
wb.close()