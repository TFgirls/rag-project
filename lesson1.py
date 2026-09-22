import glob
import pdfplumber

# 1. 找 PDF
pdf_files = glob.glob("pdfs/*.pdf")

# 2. 读第一个 PDF,把所有页文字拼到一个大字符串里
all_text = ""
with pdfplumber.open(pdf_files[0]) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        all_text += text + "\n\n"  # += 把每页文字「追加」到 all_text后面

# 3. 把拼好的文字写进一个 txt 文件
with open("课表文字.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("写好了!文字已存到 课表文字.txt")