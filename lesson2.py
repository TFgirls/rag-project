#lesson2.py -- 用 extract_tables() 读课表 表格
import glob
import pdfplumber

pdf_files = glob.glob("pdfs/*.pdf")

with pdfplumber.open(pdf_files[0]) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()   #提取这一页的所有表格
        table = tables[0]

        for row in table:               #外层循环：走每一行
            cleaned = []                #这一行清洗后的结果（空列表当容器）
            for cell in row:            #内层循环：走这一行的每个格子
                if cell is None or cell == "":
                    cleaned.append("")  #空格子 -> 放个空字符串占位
                else:
                    name = "、".join(cell.split("\n"))  #只取第一行 = 课程名
                    cleaned.append(name)
            print(cleaned)