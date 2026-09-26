# regex_json.py —— D6 补课：正则表达式 + json

import re
import json
# ========== 第一部分：regex 正则 ==========

text = "我20岁，身高180"

print(re.findall(r"\d+", text))          # ['20', '180']  找所有数字
print(re.sub(r"\d+", "X", text))         # 我X岁，身高X    替换
print(re.search(r"\d+", text).group())   # 20            找第一个
# ========== 第二部分：json ==========
# 字符串 → Python 对象（API 返回后你要做的第一步）
s = '{"name": "Jack", "age": 18}'
data = json.loads(s)
print(data["name"])                      # Jack

# Python 对象 → 字符串（发给别人 / 存文件）
d = {"name": "Jack", "age": 18}
print(json.dumps(d))                     # {"name": "Jack", "age": 18}


# ● 今天 D9 了，正课是 venv +
#   requirements.txt（昨天我提前讲过一半，被岔开了）。现在就做这个。
#
#   D9：给 rag-project 建虚拟环境
#
#   在 PyCharm 底部的 Terminal 里，cd 到项目目录后，依次敲：
#
#   # 1. 建环境（会多出一个 venv 文件夹）
#   python -m venv venv
#
#   # 2. 激活（Windows）——命令行前面会出现 (venv)
#   venv\Scripts\activate
#
#   # 3. 装依赖
#   pip install pdfplumber openpyxl requests python-dotenv pymupdf
#
#   # 4. 导出清单
#   pip freeze > requirements.txt
#
#   然后 .gitignore 里加一行 venv/（跟 .env 一样，别传 GitHub）。
#
#   做完的标志：命令行前面出现 (venv)，且多出 requirements.txt
#   文件（里面列了一堆库）。
#
#   卡在哪一步就贴给我。
# （LeetCode 那 2 道、batch_summary 跑通，还是欠着的，不催你，有空再补。）

