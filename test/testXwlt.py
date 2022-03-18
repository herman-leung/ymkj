import xlwt

workBook = xlwt.Workbook(encoding = 'utf-8')  # 创建workbook对象
workSheet = workBook.add_sheet('sheet1')  # 创建工作表
# workSheet.write(0,0,"hello")  #写入数据  第一个参数是行号，第二个参数表示列 ，第三个参数是内容
# workBook.save("student.xls")  # 保存数据表


for i in range(1,10):
    for j in range(1,i+1):
        result = "{} * {} = {}".format(j,i,i*j)
        workSheet.write(i-1,j-1,result)
        workBook.save("student.xls")

