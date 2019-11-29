该小项目能体现增删改查的思想以及函数分功能（初步体现高内聚低耦合思想），这里就顺便列一下这个写项目的基本思想，因为也是刚入门，所以还是要写一下的。
1.导类名，写class
2.写类中的函数，首先是初始化函数（init），主要是配置一些基本数据；按功能写函数，增（add-info），删（delete-info），
改（modify-info），查（find-info）。为了使程序有更好的用户体验，最好在配置一个print-menu的函数，这样既美观而且能达到一个调用各函数的功能
3.增：顾名思义就是添加信息，肯定需要input输入，而且要输入到哪里也是一个问题，所以在定义一个空字典，按 “字典名【键名】 = 值”，把值传入字典，
再把该字典传入我们定义的列表中，用append方法
4.删：首先呢，要确定删那条数据，用这个数据来匹配我们系统中的数据，虽是这样说，但实现的过程却是，把我们的数据拿出来，一一和我们要删的数据匹配，
若匹配上，则调用Python现成的函数remove
5.改：改的话也要先找到要改的，找到的话，输入新值，找不到的话，返回提示信息，通过定义flag值，达到分类效果（我感觉类似于switch），
flag作用证明你运行到这个函数了
6.查：；就是直接输入要找的数据，通过循环取值来判断是否找到，同样定义一个flag变量
7.因为运行完以上每个函数后，其实都要展示给用户加保存的，所以这里再定义show—info，save-info，show的意思是把我们目前有的所有信息打出来
而save的话，就（f = open("student.txt","w")f.write(str(self.names))f.close()），打开，操作，关闭
8.最后，在定义一个开始函数，调用定义好的print-menu，打印使用界面，通过分支函数，分开调用各个功能函数




import random

class StudentSys(object):
    def __init__(self):
        # 实例属性
        self.names = []
        self.infos = "1:增加|2:删除|3:修改|4:查找|5:显示|6:退出系统"

    # 打印提示信息(菜单)
    def print_menu(self):
        "打印提示菜单信息"
        print("=" * 25)
        print("\t~学生管理系统版本~")
        print("\t1:添加学生信息")
        print("\t2:删除学生信息")
        print("\t3:修改学生信息")
        print("\t4:查找学生信息")
        print("\t5:显示学生信息")
        print("\t6:退出学生信息系统")
        print("=" * 25)

    def add_info(self):
        "添加信息"
        self.student = {}
        name = input("请添加新同学的姓名:")
        phone = input("请添加新同学的手机号:")
        wechat = input("请输入新同学的微信号:")
        self.student["name"] = name
        self.student["phone"] = phone
        self.student["wechat"] = wechat

        # 把学生信息(字典里面)添加到列表
        self.names.append(self.student)
        self.show_info()
        self.save_info()

    def delete_info(self):
        '删除信息'
        # 根据下标删除和内容删除和末尾删除
        del_name = input("请输入删除的学生的姓名:")
        for name in self.names:
            # name:{"name":"曹操"....}
            if del_name == name.get("name"):
                self.names.remove(name)

        self.show_info()
        self.save_info()

    def modify_info(self):
        """修改信息"""
        # 根据下标修改index是列表的方法
        find_name = input("请输入您需要修改学生的姓名: ")
        flag = 0  # 0,没有找到,1找到了
        for name in self.names:

            if find_name == name["name"]:
                new_name = input("请输入新的名字: ")
                name["name"] = new_name
                flag = 1
                break

        if flag == 0:
            print("该名学生%s不存在" % find_name)

        else:
            self.show_info()
        self.save_info()

    def find_info(self):
        '''查找信息'''
        find_name = input("请输入你要查找的姓名:")
        flag = 0  # 0,没有找到,1找到了
        for name in self.names:
            for value in name.values():
                if find_name == value:
                    flag = 1
                    print("找到了:{}".format(find_name))
                    break

        if flag == 0:
            print("没有找到:{}".format(find_name))

    def show_info(self):
        "表格方式显示所以信息"
        print("\n")
        print("当前学生信息")
        print("~" * 50)
        print("\t姓名\t\t\t电话\t\t\t微信\t")
        for name in self.names:
              msg = "\t" + name.get("name") + "\t\t" + name.get("phone") + "\t\t" + name.get("wechat") + "\t\t"
              print("~" * 50)
              print(msg)
        print("~" * 50)
        print("\n")

    def start(self):
          self.print_menu()
          self.load_info()
          while True:
                print("\n\n")
                print("操作指令")
                print("~" * 50)
                print(self.infos)
                print("~" * 50)
                number = input("请按照提示输入指令：")

                if number.isdight():
                      number = int(number)
                      if number == 1:
                            self.add_info()
                      elif number == 2:
                            self.delete_info()
                      elif number == 3:
                            self.modify_info()
                      elif number == 4:
                            self.find_info()
                      elif number == 5:
                            self.show_info()
                      elif number == 6:
                            break

                else:
                      print("请输入正确的编号！")

    def load_info(self):
          f = open("students.txt","a+")
          f.seek(0,0)
          content = f.read()
          if len(content) > 0:
                self.names = eval(content)

    def save_info(self):
          f = open("student.txt","w")
          f.write(str(self.names))
          f.close()

s = StudentSys()
s.start()
