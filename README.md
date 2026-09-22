 把 7 个 PDF 课表自动解析成课程名,导出 Excel。

  ## 做了什么
  - lesson1.py:读 PDF 提取文字,存成 txt
  - lesson2.py:用 extract_tables 抽表格、清洗课程名
  - lesson3.py:遍历 7 个 PDF + try-except 兜底 + 写 Excel

  ## 技术栈
  Python / pdfplumber / openpyxl

  ## 怎么跑
  pip install pdfplumber openpyxl
  python lesson3.py