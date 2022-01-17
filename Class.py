class Student(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def study(self, course_name):
        print('%s is studying%s.' % (self.name, course_name))
def main():
    stu1=Student('zxq', 20)
    stu1.study('Python')

if __name__ == '__main__':
    main()
