import pdfplumber
import glob

class ScheduleRender:
    def __init__(self, folder):
        self.folder = folder        #存文件夹路径

    def get_course(self):
        pdf_files = glob.glob(self.folder + '/*.pdf')
        all_courses = []
        for pdf_file in pdf_files:
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    try:
                        tables = page.extract_tables()
                    except Exception as e:
                        print(f"抽表失败，跳过：{e}")
                        continue
                    for table in tables:
                        for row in table:
                            for cell in row:
                                if cell is None or cell == "":
                                    continue
                                name = "、".join(cell.split("\n"))

                                all_courses.append(name)
        return all_courses
reader = ScheduleRender("pdfs")
courses = reader.get_course()
print(len(courses))

