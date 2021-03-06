from zhixuewang import login
from zhixuewang import exceptions as zhiExc
import os
import msvcrt


def get_origin(exam):
    while True:
        print("\n是否需要获取原卷？")
        b = input("注意，一段时间以前的考试一般无法获取原卷。\n").strip()
        if b == "Y" or b == "y":
            getget_origin(exam)
            while True:
                b = input("\n是否继续获取原卷？\n").strip()
                if b == "Y" or b == "y":
                    getget_origin(exam)
                if b == "N" or b == "n":
                    break
        if b == "N" or b == "n":
            break


def getget_origin(exam):
    sub = str(input("\n请输入学科名称："))
    url = zxw.get_original(sub, exam)
    test = str(url[1:len(url)-1])
    if test == '':
        print("获取失败。")
    else:
        print(sub+"原卷网页地址:")
        for i in url:
            print(i)
        print("请复制链接在浏览器中打开，然后右键保存。")


def input_noback():
    li = []
    while True:
        ch = msvcrt.getch()
        if ch == b'\r':
            msvcrt.putch(b'\n')
            get_input = '%s' % b''.join(li).decode()
            break
        elif ch == b'\x08':
            if li:
                li.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
        elif ch == b'\x1b':
            break
        else:
            li.append(ch)
            msvcrt.putch(b'*')
    return get_input


os.system("cls")
print("这是一个用于查询智学网上考试分数的程序。")
print("该程序需要你提供账号与密码来登陆账号。")
print("如果发现任何错误，请联系我们。")
print('\n本程序的所有交互通过输入"Y"（是）与"N"（不是）来进行，请牢记。\n')

while True:
    try:
        username = input("你的账号:\n").strip()
        print("\n你的密码:")
        password = input_noback().strip()
        zxw = login(username, password)
        os.system("cls")
        print("登录成功，正在获取考试列表...")
        exams = zxw.get_exams()
        if len(exams) == 0:
            print("你目前没有考试。")
        continued = True
        while continued:
            print("考试列表:")
            for i, exam in enumerate(exams):
                print(f"{i+1}. {exam.name}")
            msg = "请输入要查询的考试编号:"
            while True:
                i = input(msg).strip()
                i = str((int(i)-1))
                if (not i.isdigit()) or int(i) < 0 or int(i) > len(exams) - 1:
                    print("输入有误")
                    msg = "请重新输入:"
                else:
                    break
            print("正在查询成绩...")
            i = int(i)
            exam = exams[i]
            print("成绩为:")
            print(zxw.get_self_mark(exam))
            get_origin(exam)
            while True:
                b = input("\n是否查询其他考试？\n").strip()
                if b == "Y" or b == "y":
                    os.system("cls")
                    break
                if b == "N" or b == "n":
                    continued = False
                    print("\n再见！")
                    exit()
                else:
                    print("输入有误")

    except zhiExc.UserOrPassError:
        print("用户名或密码错误，请重新输入。\n")

    except zhiExc.UserNotFoundError:
        print("用户不存在，请重新输入。\n")

    except zhiExc.LoginError:
        print("登陆错误，请检查你的网络状况或联系我们。\n")
