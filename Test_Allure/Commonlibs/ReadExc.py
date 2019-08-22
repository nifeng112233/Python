import xlrd

class Read_Ex():
    def read_excel(self):
        book = xlrd.open_workbook("C:/Users/Administrator/PycharmProjects/untitled/Test_Allure/Data/data1.xlsx")
        table = book.sheet_by_name("Sheet2")
        row_Num = table.nrows
        col_Num = table.ncols
        s = []
        key = table.row_values(0)
        if row_Num <=1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d = {}
                values = table.row_values(j)
                for x in range(col_Num):
                    d[key[x]]=values[x]
                j += 1
                s.append(d)
            return s

if __name__ == '__main__':
    r = Read_Ex()
    s = r.read_excel()
    print(s)

