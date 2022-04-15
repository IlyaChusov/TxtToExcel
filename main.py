try:
    import xlsxwriter
except ImportError:
    import os
    os.system('pip install xlsxwriter')
    import xlsxwriter

import glob


workbook = xlsxwriter.Workbook('результат.xlsx')

sheet = workbook.add_worksheet()

i = 1
for file in glob.glob("*.txt"):
    newfile = open(file)
    sheet.write('A' + str(i), newfile.read())
    i = i + 1

workbook.close()



