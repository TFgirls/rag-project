# lesson3.py -- 读全部7个PDF的所有表格，汇总课程名
import glob
import pdfplumber
import openpyxl

pdf_files = glob.glob('pdfs/*.pdf')
all_courses = []                #汇总容器

for pdf_file in pdf_files:      #遍历7个文件
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            try:
                tables = page.extract_tables()      #抽这一页所有表
            except Exception as e:      #D2兜底：坏页不崩
                print(f"抽表失败，跳过:{e}")
                continue
            for table in tables:        #遍历每张表
                for row in table:       #遍历每行
                    for cell in row:    #遍历每个格子
                        if cell is None or cell == "":
                            continue
                        name = "、".join(cell.split("\n"))
                        all_courses.append(name)
print(all_courses)
wb = openpyxl.Workbook()            #新建空工作簿（在内存里）
ws = wb.active              #拿第一个工作表
ws.title = "课表名"

ws.append(["课程"])       #第1行写表头
for name in all_courses:
    ws.append([name])       #每个课程名占一行

wb.save("课程汇总.xlsx")        #存成真文件
print("已写入 课程汇总.xlsx")