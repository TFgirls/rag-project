#lesson1.py -- 第一个脚本：读课表PDF，把文字抠出来打印
import glob         #用通配符找文件
import pdfplumber   #专门读PDF的库

#第一步:找到 pdfs 文件夹里所有的PDF
pdf_files = glob.glob("pdfs/*.pdf")
print(f"找到 {len(pdf_files)}个PDF:")

for name in pdf_files:
    print(" -", name)

#第二步：打开第一个PDF
with pdfplumber.open(pdf_files[0]) as pdf:
    print(f"\n正在读：{pdf_files[0]}，共 {len(pdf.pages)}页\n")

    #第三步：一页一页把文字抠出来打印
    for i,page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"=========第 {i+1} 页 =========")
        print(text)