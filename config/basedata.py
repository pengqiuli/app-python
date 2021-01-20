import xlrd

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'E:\app-python\config\xiugaipassword.xlsx')
    # 打开表格
    table = workbook.sheet_by_name("修改登录密码")
    row = table.nrows
    for i in range(1,row):
        rowdata = table.row_values(i)
        print(rowdata,row)

