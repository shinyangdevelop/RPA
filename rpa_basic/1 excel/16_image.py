from openpyxl.drawing.image import Image
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

img = Image("img.png")

ws.add_image(img, "C3")

wb.save("sample_image.xlsx")
