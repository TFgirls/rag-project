import os
import fitz
import requests
import openpyxl
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()           # 真正调用它,把 .env读进环境变量
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")        #把key存进变量
def summarize(text):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": "Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user","content": f"请用三句话概括以下内容：{text}"}]
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]

def read_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

folder = Path(r"F:\Desktop\rag-project\pdfs")
results = []
errors = []

for pdf_path in folder.glob("*.pdf"):
    try:
        print(f"正在处理：{pdf_path.name}")
        text = read_pdf(pdf_path)
        summary = summarize(text)
        results.append((pdf_path.name,summary))
        print(f"   完成:{summary[:30]}...")
        time.sleep(1)           #每个请求隔1秒
    except Exception as e:
        errors.append((pdf_path.name, str(e)))
        print(f"   失败:{e}")


wb = openpyxl.Workbook()
ws = wb.active
ws.append(["文件名","摘要"])

for name, summary in results:
    ws.append([name,summary])

wb.save(r"F:\Desktop\rag-project\摘要结果.xlsx")
print(f"\n完成,成功{len(results)}个,失败{len(errors)}")
if errors:
    print("失败列表:",errors)