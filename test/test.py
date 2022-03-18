import openpyxl as op
# 路径 = r'C:\Users\18728\Desktop\pandas官方文档中文版1.0\test.xlsx'
# 工作簿 = op.Workbook(路径);
# 工作簿.save(路径)

path = r'C:\Users\18728\Desktop\pandas官方文档中文版1.0\test.xlsx'

wb = op.load_workbook(path)
workList = wb['Sheet']
print(workList)
print(wb['Sheet2'])
print(wb.active)