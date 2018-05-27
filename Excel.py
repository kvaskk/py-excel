import xlrd, xlwt
rb = xlrd.open_workbook('C:/Users/kznva/PycharmProjects/untitled/gotovo.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
name = [sheet.row_values(x)[3] for x in range (sheet.nrows)]
surname = [sheet.row_values(x)[4] for x in range (sheet.nrows)]
otch = [sheet.row_values(x)[5] for x in range (sheet.nrows)]

rb = xlrd.open_workbook('C:/Users/kznva/PycharmProjects/untitled/raz1.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)
orig = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]


for i in range(30083):
    for g in range(5196):
        if orig[i][11] == name[g] and orig[i][12] == surname[g] and orig[i][13] == otch[g]:
            orig[i][11] = 0




wb = xlwt.Workbook()
ws = wb.add_sheet('Test')
for i in range(30083):
    for g in range(21):
        ws.write(i, g, orig[i][g])


wb.save('C:/Users/kznva/PycharmProjects/untitled/new_base.xls')


