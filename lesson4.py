class Course:           #类 = 模板
    def __init__(self, name, teacher):         #造对象时自动跑，收name 和 teacher两个钟
        self.name = name            #存属性1：课程名
        self.teacher = teacher      #存属性2：老师
    def describe(self):
        return f"{self.name} {self.teacher}"    #用 f-string拼出来
    def is_teacher_of(self, teacher_name):
        return self.teacher == teacher_name

c1 = Course("高等数学", "王老师")      #造对象1，两个值按顺序塞进 name，teacher
c2 = Course("大学英语", "李老师")      #造对象2：

print(c1.describe())          #打印

print(c2.describe())

print(c1.is_teacher_of("王老师"))
print(c1.is_teacher_of("李老师"))


class OnlineCourse(Course):
    def __init__(self, name, teacher, platform):
        super().__init__(name, teacher)
        self.platform = platform


o = OnlineCourse("Python", "李老师", "B站")
print(o.describe())  # Python 李老师
print(o.platform)  # B站



