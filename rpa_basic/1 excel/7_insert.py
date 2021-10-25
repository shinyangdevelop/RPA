from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8)
# ws.insert_rows(8, 5)

ws.insert_cols(2, 3)

wb.save("sample_insert_cols.xlsx")