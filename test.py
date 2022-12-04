import shutil
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import *
import os
import pyperclip
import calendar
import time


def btn_Search(search, listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra):
    tuple_zirzamin = listbox_zirzamin.get(0, listbox_zirzamin.size())
    tuple_tabaghe1 = listbox_tabaghe1.get(0, listbox_tabaghe1.size())
    tuple_tabaghe2 = listbox_tabaghe2.get(0, listbox_tabaghe2.size())
    tuple_tabaghe3 = listbox_tabaghe3.get(0, listbox_tabaghe3.size())
    tuple_tabaghe4 = listbox_tabaghe4.get(0, listbox_tabaghe4.size())
    tuple_Extra = listbox_Extra.get(0, listbox_Extra.size())
    tuple_karevan = listbox_karevan.get(0, listbox_karevan.size())
    print(tuple_zirzamin)
    print(tuple_tabaghe1)
    print(tuple_tabaghe2)
    print(tuple_tabaghe3)
    print(tuple_tabaghe4)
    print(tuple_Extra)
    print(tuple_karevan)
    print("_______")
    flag = False
    for i in tuple_zirzamin:
        if search.get() in i:
            flag = True
            listbox_zirzamin.selection_set(check_index(i, "zirzamin"))
            listbox_zirzamin.see(check_index(i, "zirzamin"))
            listbox_zirzamin.activate(check_index(i, "zirzamin"))
            listbox_zirzamin.selection_anchor(check_index(i, "zirzamin"))
            listbox_zirzamin.selection_anchor(check_index(i, "zirzamin"))
    for i in tuple_tabaghe1:
        if search.get() in i:
            flag = True
            listbox_tabaghe1.selection_set(check_index(i, "tabaghe1"))
            listbox_tabaghe1.see(check_index(i, "tabaghe1"))
            listbox_tabaghe1.activate(check_index(i, "tabaghe1"))
            listbox_tabaghe1.selection_anchor(check_index(i, "tabaghe1"))
            listbox_tabaghe1.selection_anchor(check_index(i, "tabaghe1"))
    for i in tuple_tabaghe2:
        if search.get() in i:
            flag = True
            listbox_tabaghe2.selection_set(check_index(i, "tabaghe2"))
            listbox_tabaghe2.see(check_index(i, "tabaghe2"))
            listbox_tabaghe2.activate(check_index(i, "tabaghe2"))
            listbox_tabaghe2.selection_anchor(check_index(i, "tabaghe2"))
            listbox_tabaghe2.selection_anchor(check_index(i, "tabaghe2"))
    for i in tuple_tabaghe3:
        if search.get() in i:
            flag = True
            listbox_tabaghe3.selection_set(check_index(i, "tabaghe3"))
            listbox_tabaghe3.see(check_index(i, "tabaghe3"))
            listbox_tabaghe3.activate(check_index(i, "tabaghe3"))
            listbox_tabaghe3.selection_anchor(check_index(i, "tabaghe3"))
            listbox_tabaghe3.selection_anchor(check_index(i, "tabaghe3"))
    for i in tuple_tabaghe4:
        if search.get() in i:
            flag = True
            listbox_tabaghe4.selection_set(check_index(i, "tabaghe4"))
            listbox_tabaghe4.see(check_index(i, "tabaghe4"))
            listbox_tabaghe4.activate(check_index(i, "tabaghe4"))
            listbox_tabaghe4.selection_anchor(check_index(i, "tabaghe4"))
            listbox_tabaghe4.selection_anchor(check_index(i, "tabaghe4"))
    for i in tuple_Extra:
        if search.get() in i:
            flag = True
            listbox_Extra.selection_set(check_index(i, "Extra"))
            listbox_Extra.see(check_index(i, "Extra"))
            listbox_Extra.activate(check_index(i, "Extra"))
            listbox_Extra.selection_anchor(check_index(i, "Extra"))
            listbox_Extra.selection_anchor(check_index(i, "Extra"))
    for i in tuple_karevan:
        if search.get() in i:
            flag = True
            listbox_karevan.selection_set(check_index(i, "karevan"))
            listbox_karevan.see(check_index(i, "karevan"))
            listbox_karevan.activate(check_index(i, "karevan"))
            listbox_karevan.selection_anchor(check_index(i, "karevan"))
            listbox_karevan.selection_anchor(check_index(i, "karevan"))

    if not flag:
        messagebox.showinfo( "اخطار" , "فرد مورد نظر یافت نشد")

    search.delete(0 , 'end')


def check_index(element, type):
    if type == "zirzamin":
       try:
           index = listbox_zirzamin.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index
    if type == "tabaghe1":
       try:
           index = listbox_tabaghe1.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index
    if type == "tabaghe2":
       try:
           index = listbox_tabaghe2.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index
    if type == "tabaghe3":
       try:
           index = listbox_tabaghe3.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index
    if type == "tabaghe4":
       try:
           index = listbox_tabaghe4.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index
    if type == "Extra":
       try:
           index = listbox_Extra.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index
    if type == "karevan":
       try:
           index = listbox_karevan.get(0, "end").index(element)
           return index
       except ValueError:
           index = -1
           return index


def btn_add(path, En):
    list1_zirzamin = os.listdir("database/Male/zirzamin")
    list1_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list1_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list1_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list1_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list1_karevan = os.listdir("database/karevan")
    list1_Extra = os.listdir("database/Extra")
    for i in list1_zirzamin:
        if not os.path.isfile("database/Male/zirzamin/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/zirzamin/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/zirzamin/" + i):
                shutil.rmtree("database/Male/zirzamin/" + i)
            else:
                print("no directory !! ")
    for i in list1_tabaghe1:
        if not os.path.isfile("database/Male/tabaghe1/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/tabaghe1/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/tabaghe1/" + i):
                shutil.rmtree("database/Male/tabaghe1/" + i)
            else:
                print("no directory !! ")
    for i in list1_tabaghe2:
        if not os.path.isfile("database/Male/tabaghe2/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/tabaghe2/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/tabaghe2/" + i):
                shutil.rmtree("database/Male/tabaghe2/" + i)
            else:
                print("no directory !! ")
    for i in list1_tabaghe3:
        if not os.path.isfile("database/Female/tabaghe3/" + i + "/info.txt") or not os.path.isfile(
                "database/Female/tabaghe3/" + i + "/img.jpg"):
            if os.path.isdir("database/Female/tabaghe3/" + i):
                shutil.rmtree("database/Female/tabaghe3/" + i)
            else:
                print("no directory !! ")
    for i in list1_tabaghe4:
        if not os.path.isfile("database/Female/tabaghe4/" + i + "/info.txt") or not os.path.isfile(
                "database/Female/tabaghe4/" + i + "/img.jpg"):
            if os.path.isdir("database/Female/tabaghe4/" + i):
                shutil.rmtree("database/Female/tabaghe4/" + i)
            else:
                print("no directory !! ")
    for i in list1_Extra:
        if not os.path.isfile("database/Extra/" + i + "/info.txt") or not os.path.isfile(
                "database/Extra/" + i + "/img.jpg"):
            if os.path.isdir("database/Extra/" + i):
                shutil.rmtree("database/Extra/" + i)
            else:
                print("no directiry !! ")

    list1_zirzamin = os.listdir("database/Male/zirzamin")
    list1_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list1_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list1_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list1_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list1_karevan = os.listdir("database/karevan")
    list1_Extra = os.listdir("database/Extra")
    print("0 -> ", list1_zirzamin)
    print("1 -> ", list1_tabaghe1)
    print("2 -> ", list1_tabaghe2)
    print("3 -> ", list1_tabaghe3)
    print("4 -> ", list1_tabaghe4)
    print("e -> ", list1_Extra)
    print("k -> ", list1_karevan)
    name2_zirzamin = []
    name2_tabaghe1 = []
    name2_tabaghe2 = []
    name2_tabaghe3 = []
    name2_tabaghe4 = []
    name2_Extra = []
    today = int(calendar.timegm(time.gmtime()))

    for i in list1_zirzamin:
        file = open("database/Male/zirzamin/" + i + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name2_zirzamin += [str1[0]]
        else:
            shutil.rmtree("database/Male/zirzamin/" + i)

    for i in list1_tabaghe1:
        file = open("database/Male/tabaghe1/" + i + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name2_tabaghe1 += [str1[0]]
        else:
            shutil.rmtree("database/Male/tabaghe1/" + i)

    for i in list1_tabaghe2:
        file = open("database/Male/tabaghe2/" + i + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name2_tabaghe2 += [str1[0]]
        else:
            shutil.rmtree("database/Male/tabaghe2/" + i)

    for i in list1_tabaghe3:
        file = open("database/Female/tabaghe3/" + i + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name2_tabaghe3 += [str1[0]]
        else:
            shutil.rmtree("database/Female/tabaghe3/" + i)

    for i in list1_tabaghe4:
        file = open("database/Female/tabaghe4/" + i + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name2_tabaghe4 += [str1[0]]
        else:
            shutil.rmtree("database/Female/tabaghe4/" + i)

    for i in list1_Extra:
        file = open("database/Extra/" + i + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name2_Extra += [str1[0]]
        else:
            shutil.rmtree("database/Extra/" + i)

    listbox_zirzamin.delete(0, END)
    listbox_tabaghe1.delete(0, END)
    listbox_tabaghe2.delete(0, END)
    listbox_tabaghe3.delete(0, END)
    listbox_tabaghe4.delete(0, END)
    listbox_karevan.delete(0, END)
    listbox_Extra.delete(0, END)

    listbox_zirzamin.insert(END, *name2_zirzamin)
    listbox_tabaghe1.insert(END, *name2_tabaghe1)
    listbox_tabaghe2.insert(END, *name2_tabaghe2)
    listbox_tabaghe3.insert(END, *name2_tabaghe3)
    listbox_tabaghe4.insert(END, *name2_tabaghe4)
    listbox_karevan.insert(END, *list1_karevan)
    listbox_Extra.insert(END, *name2_Extra)
    if not En.get() == "":
        file_karevan = open(path + "/info.txt", "a")
        file_karevan.write(En.get() + "_")
        file_karevan.close()
    else:
        messagebox.showinfo("خطا", "کد را وارد کنید !!")
    En.delete(0, 'end')


def btn_show(pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2, pathF_tabaghe3, pathF_tabaghe4, pathE, v):
    ScanShow_Window = Toplevel()
    ScanShow_Window.title("نمایش مدارک اسکن شده")
    ScanShow_Window.geometry("350x450")
    ScanShow_Window.resizable(False, False)
    lb = Label(ScanShow_Window, text=" ")
    lb.pack()
    lb = Label(ScanShow_Window, text=" تصویر اسکن شده ", font=("arial", 15, "bold"))
    lb.pack()
    canvas = Canvas(ScanShow_Window, width=300, height=400, bd=5, relief='solid')
    canvas.pack()
    lb = Label(ScanShow_Window, text=" ")
    lb.pack()
    lb = Label(ScanShow_Window, text=" ")
    lb.pack()
    path_asli = ""
    if v.get() == "1":
        if os.path.isdir(pathE):
            path_asli = pathE
        elif os.path.isdir(pathM_zirzamin):
            path_asli = pathM_zirzamin
        elif os.path.isdir(pathM_tabaghe1):
            path_asli = pathM_tabaghe1
        elif os.path.isdir(pathM_tabaghe2):
            path_asli = pathM_tabaghe2
    elif v.get() == "2":
        if os.path.isdir(pathE):
            path_asli = pathE
        elif os.path.isdir(pathF_tabaghe3):
            path_asli = pathF_tabaghe3
        elif os.path.isdir(pathF_tabaghe4):
            path_asli = pathF_tabaghe4
        else:
            messagebox.showinfo("خطا", "مدارک را اسکن نکردید !!")

    if os.path.isfile(path_asli + "/img.jpg"):
        orginal_img = Image.open(path_asli + '/img.jpg')
        resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(resized_img)
        canvas.create_image(0, 0, image=pic, anchor=NW)
    else:
        messagebox.showinfo("خطا", "مدارک را اسکن نکردید")
        ScanShow_Window.destroy()
    ScanShow_Window.mainloop()


def list_del(list, type, temp1, listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra):
    list1_zirzamin = os.listdir("database/Male/zirzamin")
    list1_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list1_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list1_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list1_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list1_Extra = os.listdir("database/Extra")
    if type == "zirzamin":
        directories = list1_zirzamin
        for i in directories:
            file = open("database/Male/zirzamin/" + i + "/info.txt", "r")
            str1 = file.read()
            file.close()
            str1 = str1.split("_")
            if str1[0] == temp1:
                shutil.rmtree("database/Male/zirzamin/" + i)


    elif type == "tabaghe1":
        directories = list1_tabaghe1
        for i in directories:
            file = open("database/Male/tabaghe1/" + i + "/info.txt", "r")
            str1 = file.read()
            file.close()
            str1 = str1.split("_")
            if str1[0] == temp1:
                shutil.rmtree("database/Male/tabaghe1/" + i)

    elif type == "tabaghe2":
        directories = list1_tabaghe2
        for i in directories:
            file = open("database/Male/tabaghe2/" + i + "/info.txt", "r")
            str1 = file.read()
            file.close()
            str1 = str1.split("_")
            if str1[0] == temp1:
                shutil.rmtree("database/Male/tabaghe2/" + i)

    elif type == "tabaghe3":
        directories = list1_tabaghe3
        for i in directories:
            file = open("database/Female/tabaghe3/" + i + "/info.txt", "r")
            str1 = file.read()
            file.close()
            str1 = str1.split("_")
            if str1[0] == temp1:
                shutil.rmtree("database/Female/tabaghe3/" + i)

    elif type == "tabaghe4":
        directories = list1_tabaghe4
        for i in directories:
            file = open("database/Female/tabaghe4/" + i + "/info.txt", "r")
            str1 = file.read()
            file.close()
            str1 = str1.split("_")
            if str1[0] == temp1:
                shutil.rmtree("database/Female/tabaghe4/" + i)

    elif type == "Extra":
        directories = list1_Extra
        for i in directories:
            file = open("database/Extra/" + i + "/info.txt", "r")
            str1 = file.read()
            file.close()
            str1 = str1.split("_")
            if str1[0] == temp1:
                shutil.rmtree("database/Extra/" + i)

    elif type == "karevan":
        list1_zirzamin = os.listdir("database/Male/zirzamin")
        list1_tabaghe1 = os.listdir("database/Male/tabaghe1")
        list1_tabaghe2 = os.listdir("database/Male/tabaghe2")
        list1_tabaghe3 = os.listdir("database/Female/tabaghe3")
        list1_tabaghe4 = os.listdir("database/Female/tabaghe4")
        list1_Extra = os.listdir("database/Extra")
        directories = os.listdir("database/karevan")
        for i in directories:
            if temp1 == i:
                file_k = open("database/karevan/" + temp1 + "/info.txt", "r")
                id_karevan = file_k.read()
                file_k.close()
                ids = id_karevan.split("_")
                for j in ids:
                    if j in list1_zirzamin:
                        shutil.rmtree("database/Male/zirzamin/" + j)
                    elif j in list1_tabaghe1:
                        shutil.rmtree("database/Male/tabaghe1/" + j)
                    elif j in list1_tabaghe2:
                        shutil.rmtree("database/Male/tabaghe2/" + j)
                    elif j in list1_tabaghe3:
                        shutil.rmtree("database/Female/tabaghe3/" + j)
                    elif j in list1_tabaghe4:
                        shutil.rmtree("database/Female/tabaghe4/" + j)
                    elif j in list1_Extra:
                        shutil.rmtree("database/Extra/" + j)
        shutil.rmtree("database/karevan/" + temp1)

    list_zirzamin = os.listdir("database/Male/zirzamin")
    list_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list_Extra = os.listdir("database/Extra")
    list_karevan = os.listdir("database/karevan")
    for i in list_zirzamin:
        if not os.path.isfile("database/Male/zirzamin/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/zirzamin/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/zirzamin/" + i):
                shutil.rmtree("database/Male/zirzamin/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe1:
        if not os.path.isfile("database/Male/tabaghe1/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/tabaghe1/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/tabaghe1/" + i):
                shutil.rmtree("database/Male/tabaghe1/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe2:
        if not os.path.isfile("database/Male/tabaghe2/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/tabaghe2/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/tabaghe2/" + i):
                shutil.rmtree("database/Male/tabaghe2/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe3:
        if not os.path.isfile("database/Female/tabaghe3/" + i + "/info.txt") or not os.path.isfile(
                "database/Female/tabaghe3/" + i + "/img.jpg"):
            if os.path.isdir("database/Female/tabaghe3/" + i):
                shutil.rmtree("database/Female/tabaghe3/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe4:
        if not os.path.isfile("database/Female/tabaghe4/" + i + "/info.txt") or not os.path.isfile(
                "database/Female/tabaghe4/" + i + "/img.jpg"):
            if os.path.isdir("database/Female/tabaghe4/" + i):
                shutil.rmtree("database/Female/tabaghe4/" + i)
            else:
                print("no directory !! ")
    for i in list_Extra:
        if not os.path.isfile("database/Extra/" + i + "/info.txt") or not os.path.isfile(
                "database/Extra/" + i + "/img.jpg"):
            if os.path.isdir("database/Extra/" + i):
                shutil.rmtree("database/Extra/" + i)
            else:
                print("no directiry !! ")

    list_zirzamin = os.listdir("database/Male/zirzamin")
    list_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list_karevan = os.listdir("database/karevan")
    list_Extra = os.listdir("database/Extra")
    name_zirzamin = []
    name_tabaghe1 = []
    name_tabaghe2 = []
    name_tabaghe3 = []
    name_tabaghe4 = []
    name_Extra = []
    today = int(calendar.timegm(time.gmtime()))

    for temp in list_zirzamin:
        file = open("database/Male/zirzamin/" + temp + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_zirzamin += [str1[0]]
        else:
            shutil.rmtree("database/Male/zirzamin/" + temp)

    for temp in list_tabaghe1:
        temp += "/info.txt"
        file = open("database/Male/tabaghe1/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe1 += [str1[0]]
        else:
            shutil.rmtree("database/Male/tabaghe1/" + temp)

    for temp in list_tabaghe2:
        temp += "/info.txt"
        file = open("database/Male/tabaghe2/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe2 += [str1[0]]
        else:
            shutil.rmtree("database/Male/tabaghe2/" + temp)

    for temp in list_tabaghe3:
        temp += "/info.txt"
        file = open("database/Female/tabaghe3/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe3 += [str1[0]]
        else:
            shutil.rmtree("database/Female/tabaghe3/" + temp)

    for temp in list_tabaghe4:
        temp += "/info.txt"
        file = open("database/Female/tabaghe4/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe4 += [str1[0]]
        else:
            shutil.rmtree("database/Female/tabaghe4/" + temp)

    for temp in list_Extra:
        temp += "/info.txt"
        file = open("database/Extra/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_Extra += [str1[0]]
        else:
            shutil.rmtree("database/Extra/" + temp)

    listbox_zirzamin.delete(0, END)
    listbox_tabaghe1.delete(0, END)
    listbox_tabaghe2.delete(0, END)
    listbox_tabaghe3.delete(0, END)
    listbox_tabaghe4.delete(0, END)
    listbox_karevan.delete(0, END)
    listbox_Extra.delete(0, END)

    listbox_zirzamin.insert(END, *name_zirzamin)
    listbox_tabaghe1.insert(END, *name_tabaghe1)
    listbox_tabaghe2.insert(END, *name_tabaghe2)
    listbox_tabaghe3.insert(END, *name_tabaghe3)
    listbox_tabaghe4.insert(END, *name_tabaghe4)
    listbox_karevan.insert(END, *list_karevan)
    listbox_Extra.insert(END, *name_Extra)

    list.delete(ANCHOR)


def btn_scan(w):
    print("Scan")
    pyperclip.copy(w.get(1.0, END))
    spam = pyperclip.paste()


def btn_save(v, pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2, pathF_tabaghe3, pathF_tabaghe4, pathE, txtName, txtTell,
             Scan_window, path_koll, listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra):
    print("Save")
    print(v.get())
    flag = False
    text = ""
    path_asli = ""
    txt_position = ""
    Name = txtName.get()
    Tell = txtTell.get()
    if Name == "" or Tell == "":
        messagebox.showinfo("خطا", "نام یا تلفن را وارد نکردید !! ")
    else:
        if v.get() == "1":
            if os.path.isdir(pathE):
                path_asli = pathE
                txt_position = "ساختمان شماره 2"
            elif os.path.isdir(pathM_zirzamin):
                path_asli = pathM_zirzamin
                txt_position = "زیرزمین"
            elif os.path.isdir(pathM_tabaghe1):
                path_asli = pathM_tabaghe1
                txt_position = "طبقه اول"
            elif os.path.isdir(pathM_tabaghe2):
                path_asli = pathM_tabaghe2
                txt_position = "طبقه دوم"
            if os.path.isfile(path_asli + "/img.jpg"):
                flag = True
                today = calendar.timegm(time.gmtime())
                file = open(path_asli + "/info.txt", "w")
                file.write(Name + "_" + Tell + "_" + str(today))
                file.close()
            else:
                messagebox.showinfo("خطا", "مدارک را اسکن نکردید")
        elif v.get() == "2":
            if os.path.isdir(pathE):
                path_asli = pathE
                txt_position = "ساختمان شماره 2"
            elif os.path.isdir(pathF_tabaghe3):
                path_asli = pathF_tabaghe3
                txt_position = "طبقه سوم"
            elif os.path.isdir(pathF_tabaghe4):
                path_asli = pathF_tabaghe4
                txt_position = "طبقه چهارم"
            if os.path.isfile(path_asli + "/img.jpg"):
                flag = True
                today = calendar.timegm(time.gmtime())
                file = open(path_asli + "/info.txt", "w")
                file.write(Name + "_" + Tell + "_" + str(today))
                file.close()
            else:
                messagebox.showinfo("خطا", "مدارک را اسکن نکردید !!")
        if flag:
            messagebox.showinfo("موقعیت", "موقعیت شما :  " + txt_position)
            Scan_window.destroy()
            list1_zirzamin = os.listdir("database/Male/zirzamin")
            list1_tabaghe1 = os.listdir("database/Male/tabaghe1")
            list1_tabaghe2 = os.listdir("database/Male/tabaghe2")
            list1_tabaghe3 = os.listdir("database/Female/tabaghe3")
            list1_tabaghe4 = os.listdir("database/Female/tabaghe4")
            list1_Extra = os.listdir("database/Extra")
            for i in list1_zirzamin:
                if not os.path.isfile("database/Male/zirzamin/" + i + "/info.txt") or not os.path.isfile(
                        "database/Male/zirzamin/" + i + "/img.jpg"):
                    if os.path.isdir("database/Male/zirzamin/" + i):
                        shutil.rmtree("database/Male/zirzamin/" + i)
                    else:
                        print("no directory !! ")
            for i in list1_tabaghe1:
                if not os.path.isfile("database/Male/tabaghe1/" + i + "/info.txt") or not os.path.isfile(
                        "database/Male/tabaghe1/" + i + "/img.jpg"):
                    if os.path.isdir("database/Male/tabaghe1/" + i):
                        shutil.rmtree("database/Male/tabaghe1/" + i)
                    else:
                        print("no directory !! ")
            for i in list1_tabaghe2:
                if not os.path.isfile("database/Male/tabaghe2/" + i + "/info.txt") or not os.path.isfile(
                        "database/Male/tabaghe2/" + i + "/img.jpg"):
                    if os.path.isdir("database/Male/tabaghe2/" + i):
                        shutil.rmtree("database/Male/tabaghe2/" + i)
                    else:
                        print("no directory !! ")
            for i in list1_tabaghe3:
                if not os.path.isfile("database/Female/tabaghe3/" + i + "/info.txt") or not os.path.isfile(
                        "database/Female/tabaghe3/" + i + "/img.jpg"):
                    if os.path.isdir("database/Female/tabaghe3/" + i):
                        shutil.rmtree("database/Female/tabaghe3/" + i)
                    else:
                        print("no directory !! ")
            for i in list1_tabaghe4:
                if not os.path.isfile("database/Female/tabaghe4/" + i + "/info.txt") or not os.path.isfile(
                        "database/Female/tabaghe4/" + i + "/img.jpg"):
                    if os.path.isdir("database/Female/tabaghe4/" + i):
                        shutil.rmtree("database/Female/tabaghe4/" + i)
                    else:
                        print("no directory !! ")
            for i in list1_Extra:
                if not os.path.isfile("database/Extra/" + i + "/info.txt") or not os.path.isfile(
                        "database/Extra/" + i + "/img.jpg"):
                    if os.path.isdir("database/Extra/" + i):
                        shutil.rmtree("database/Extra/" + i)
                    else:
                        print("no directiry !! ")

            list1_zirzamin = os.listdir("database/Male/zirzamin")
            list1_tabaghe1 = os.listdir("database/Male/tabaghe1")
            list1_tabaghe2 = os.listdir("database/Male/tabaghe2")
            list1_tabaghe3 = os.listdir("database/Female/tabaghe3")
            list1_tabaghe4 = os.listdir("database/Female/tabaghe4")
            list1_karevan = os.listdir("database/karevan")
            list1_Extra = os.listdir("database/Extra")
            print("0 -> ", list1_zirzamin)
            print("1 -> ", list1_tabaghe1)
            print("2 -> ", list1_tabaghe2)
            print("3 -> ", list1_tabaghe3)
            print("4 -> ", list1_tabaghe4)
            print("e -> ", list1_Extra)
            print("k -> ", list1_karevan)
            name2_zirzamin = []
            name2_tabaghe1 = []
            name2_tabaghe2 = []
            name2_tabaghe3 = []
            name2_tabaghe4 = []
            name2_Extra = []
            today = int(calendar.timegm(time.gmtime()))

            for i in list1_zirzamin:
                file = open("database/Male/zirzamin/" + i + "/info.txt", "r")
                str1 = file.read()
                file.close()
                str1 = str1.split("_")
                time_vorod = int(str1[2])
                print((today - time_vorod) / (3600 * 24))
                if (today - time_vorod) / (3600 * 24) < 3:
                    name2_zirzamin += [str1[0]]
                else:
                    shutil.rmtree("database/Male/zirzamin/" + i)

            for i in list1_tabaghe1:
                file = open("database/Male/tabaghe1/" + i + "/info.txt", "r")
                str1 = file.read()
                file.close()
                str1 = str1.split("_")
                time_vorod = int(str1[2])
                print((today - time_vorod) / (3600 * 24))
                if (today - time_vorod) / (3600 * 24) < 3:
                    name2_tabaghe1 += [str1[0]]
                else:
                    shutil.rmtree("database/Male/tabaghe1/" + i)

            for i in list1_tabaghe2:
                file = open("database/Male/tabaghe2/" + i + "/info.txt", "r")
                str1 = file.read()
                file.close()
                str1 = str1.split("_")
                time_vorod = int(str1[2])
                print((today - time_vorod) / (3600 * 24))
                if (today - time_vorod) / (3600 * 24) < 3:
                    name2_tabaghe2 += [str1[0]]
                else:
                    shutil.rmtree("database/Male/tabaghe2/" + i)

            for i in list1_tabaghe3:
                file = open("database/Female/tabaghe3/" + i + "/info.txt", "r")
                str1 = file.read()
                file.close()
                str1 = str1.split("_")
                time_vorod = int(str1[2])
                print((today - time_vorod) / (3600 * 24))
                if (today - time_vorod) / (3600 * 24) < 3:
                    name2_tabaghe3 += [str1[0]]
                else:
                    shutil.rmtree("database/Female/tabaghe3/" + i)

            for i in list1_tabaghe4:
                file = open("database/Female/tabaghe4/" + i + "/info.txt", "r")
                str1 = file.read()
                file.close()
                str1 = str1.split("_")
                time_vorod = int(str1[2])
                print((today - time_vorod) / (3600 * 24))
                if (today - time_vorod) / (3600 * 24) < 3:
                    name2_tabaghe4 += [str1[0]]
                else:
                    shutil.rmtree("database/Female/tabaghe4/" + i)

            for i in list1_Extra:
                file = open("database/Extra/" + i + "/info.txt", "r")
                str1 = file.read()
                file.close()
                str1 = str1.split("_")
                time_vorod = int(str1[2])
                print((today - time_vorod) / (3600 * 24))
                if (today - time_vorod) / (3600 * 24) < 3:
                    name2_Extra += [str1[0]]
                else:
                    shutil.rmtree("database/Extra/" + i)

            listbox_zirzamin.delete(0, END)
            listbox_tabaghe1.delete(0, END)
            listbox_tabaghe2.delete(0, END)
            listbox_tabaghe3.delete(0, END)
            listbox_tabaghe4.delete(0, END)
            listbox_karevan.delete(0, END)
            listbox_Extra.delete(0, END)

            listbox_zirzamin.insert(END, *name2_zirzamin)
            listbox_tabaghe1.insert(END, *name2_tabaghe1)
            listbox_tabaghe2.insert(END, *name2_tabaghe2)
            listbox_tabaghe3.insert(END, *name2_tabaghe3)
            listbox_tabaghe4.insert(END, *name2_tabaghe4)
            listbox_karevan.insert(END, *list1_karevan)
            listbox_Extra.insert(END, *name2_Extra)
            if not os.path.isdir(path_koll):
                shutil.copytree(path_asli,path_koll)



def btn_path(v, w, pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2, pathF_tabaghe3, pathF_tabaghe4, pathE,
             counter_male_zirzamin, counter_male_tabaghe1, counter_male_tabaghe2, counter_female_tabaghe3,
             counter_female_tabaghe4, counter_extra):
    desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")
    print(desktop_path)
    if v.get() == "1" and counter_male_zirzamin < 1000:
        if os.path.isdir(pathF_tabaghe3):
            os.rmdir(pathF_tabaghe3)
        if os.path.isdir(pathF_tabaghe4):
            os.rmdir(pathF_tabaghe4)
        if not os.path.isdir(pathM_zirzamin):
            os.mkdir(pathM_zirzamin)
        w.delete(1.0, END)
        path = pathM_zirzamin.replace("/", "\\")
        w.insert(1.0, "C:" + desktop_path + "\\" + path + "\\img.jpg")

    elif v.get() == "1" and counter_male_tabaghe1 < 1000:
        if os.path.isdir(pathF_tabaghe3):
            os.rmdir(pathF_tabaghe3)
        if os.path.isdir(pathF_tabaghe4):
            os.rmdir(pathF_tabaghe4)
        if not os.path.isdir(pathM_tabaghe1):
            os.mkdir(pathM_tabaghe1)
        w.delete(1.0, END)
        path = pathM_tabaghe1.replace("/", "\\")
        w.insert(1.0, "C:" + desktop_path + "\\" + path + "\\img.jpg")

    elif v.get() == "1" and counter_male_tabaghe2 < 1000:
        if os.path.isdir(pathF_tabaghe3):
            os.rmdir(pathF_tabaghe3)
        if os.path.isdir(pathF_tabaghe4):
            os.rmdir(pathF_tabaghe4)
        if not os.path.isdir(pathM_tabaghe2):
            os.mkdir(pathM_tabaghe2)
        w.delete(1.0, END)
        path = pathM_tabaghe2.replace("/", "\\")
        w.insert(1.0, "C:" + desktop_path + "\\" + path + "\\img.jpg")

    elif v.get() == "2" and counter_female_tabaghe3 < 1000:
        if os.path.isdir(pathM_zirzamin):
            os.rmdir(pathM_zirzamin)
        if os.path.isdir(pathM_tabaghe1):
            os.rmdir(pathM_tabaghe1)
        if os.path.isdir(pathM_tabaghe2):
            os.rmdir(pathM_tabaghe2)
        if not os.path.isdir(pathF_tabaghe3):
            os.mkdir(pathF_tabaghe3)
        w.delete(1.0, END)
        path = pathF_tabaghe3.replace("/", "\\")
        w.insert(1.0, "C:" + desktop_path + "\\" + path + "\\img.jpg")
    elif v.get() == "2" and counter_female_tabaghe4 < 1000:
        if os.path.isdir(pathM_zirzamin):
            os.rmdir(pathM_zirzamin)
        if os.path.isdir(pathM_tabaghe1):
            os.rmdir(pathM_tabaghe1)
        if os.path.isdir(pathM_tabaghe2):
            os.rmdir(pathM_tabaghe2)
        if not os.path.isdir(pathF_tabaghe4):
            os.mkdir(pathF_tabaghe4)
        w.delete(1.0, END)
        path = pathF_tabaghe4.replace("/", "\\")
        w.insert(1.0, "C:" + desktop_path + "\\" + path + "\\img.jpg")
    elif counter_extra < 2000:
        os.mkdir(pathE)
        w.delete(1.0, END)
        path = pathE.replace("/", "\\")
        w.insert(1.0, "C:" + desktop_path + "\\" + path + "\\img.jpg")
    else:
        messagebox.showinfo("اخطار", "فضای خالی وجود ندارد")


    w.configure(state=NORMAL)
    w.configure(inactiveselectbackground=w.cget("selectbackground"))


def btn_popUp(listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra):
    list_zirzamin = os.listdir("database/Male/zirzamin")
    list_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list_Extra= os.listdir("database/Extra")
    list_karevan = os.listdir("database/karevan")
    for i in list_zirzamin:
        if not os.path.isfile("database/Male/zirzamin/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/zirzamin/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/zirzamin/" + i):
                shutil.rmtree("database/Male/zirzamin/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe1:
        if not os.path.isfile("database/Male/tabaghe1/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/tabaghe1/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/tabaghe1/" + i):
                shutil.rmtree("database/Male/tabaghe1/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe2:
        if not os.path.isfile("database/Male/tabaghe2/" + i + "/info.txt") or not os.path.isfile(
                "database/Male/tabaghe2/" + i + "/img.jpg"):
            if os.path.isdir("database/Male/tabaghe2/" + i):
                shutil.rmtree("database/Male/tabaghe2/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe3:
        if not os.path.isfile("database/Female/tabaghe3/" + i + "/info.txt") or not os.path.isfile(
                "database/Female/tabaghe3/" + i + "/img.jpg"):
            if os.path.isdir("database/Female/tabaghe3/" + i):
                shutil.rmtree("database/Female/tabaghe3/" + i)
            else:
                print("no directory !! ")
    for i in list_tabaghe4:
        if not os.path.isfile("database/Female/tabaghe4/" + i + "/info.txt") or not os.path.isfile(
                "database/Female/tabaghe4/" + i + "/img.jpg"):
            if os.path.isdir("database/Female/tabaghe4/" + i):
                shutil.rmtree("database/Female/tabaghe4/" + i)
            else:
                print("no directory !! ")
    for i in list_Extra:
        if not os.path.isfile("database/Extra/" + i + "/info.txt") or not os.path.isfile(
                "database/Extra/" + i + "/img.jpg"):
            if os.path.isdir("database/Extra/" + i):
                shutil.rmtree("database/Extra/" + i)
            else:
                print("no directiry !! ")

    list_zirzamin = os.listdir("database/Male/zirzamin")
    list_tabaghe1 = os.listdir("database/Male/tabaghe1")
    list_tabaghe2 = os.listdir("database/Male/tabaghe2")
    list_tabaghe3 = os.listdir("database/Female/tabaghe3")
    list_tabaghe4 = os.listdir("database/Female/tabaghe4")
    list_karevan = os.listdir("database/karevan")
    list_Extra = os.listdir("database/Extra")
    name_zirzamin = []
    name_tabaghe1 = []
    name_tabaghe2 = []
    name_tabaghe3 = []
    name_tabaghe4 = []
    name_Extra = []
    today = int(calendar.timegm(time.gmtime()))

    for temp in list_zirzamin:
        file = open("database/Male/zirzamin/" + temp + "/info.txt", "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today-time_vorod)/(3600*24))
        if (today-time_vorod)/(3600*24) < 3:
            name_zirzamin += [str1[0]]
        else:
            shutil.rmtree("database/Male/zirzamin/" + temp)


    for temp in list_tabaghe1:
        temp += "/info.txt"
        file = open("database/Male/tabaghe1/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe1 += [str1[0]]
        else:
            shutil.rmtree("database/Male/tabaghe1/" + temp)

    for temp in list_tabaghe2:
        temp += "/info.txt"
        file = open("database/Male/tabaghe2/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe2 += [str1[0]]
        else:
            shutil.rmtree("database/Male/tabaghe2/" + temp)

    for temp in list_tabaghe3:
        temp += "/info.txt"
        file = open("database/Female/tabaghe3/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe3 += [str1[0]]
        else:
            shutil.rmtree("database/Female/tabaghe3/" + temp)

    for temp in list_tabaghe4:
        temp += "/info.txt"
        file = open("database/Female/tabaghe4/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_tabaghe4 += [str1[0]]
        else:
            shutil.rmtree("database/Female/tabaghe4/" + temp)

    for temp in list_Extra:
        temp += "/info.txt"
        file = open("database/Extra/" + temp, "r")
        str1 = file.read()
        file.close()
        str1 = str1.split("_")
        time_vorod = int(str1[2])
        print((today - time_vorod) / (3600 * 24))
        if (today - time_vorod) / (3600 * 24) < 3:
            name_Extra += [str1[0]]
        else:
            shutil.rmtree("database/Extra/" + temp)

    listbox_zirzamin.delete(0, END)
    listbox_tabaghe1.delete(0, END)
    listbox_tabaghe2.delete(0, END)
    listbox_tabaghe3.delete(0, END)
    listbox_tabaghe4.delete(0, END)
    listbox_karevan.delete(0, END)
    listbox_Extra.delete(0, END)

    listbox_zirzamin.insert(END, *name_zirzamin)
    listbox_tabaghe1.insert(END, *name_tabaghe1)
    listbox_tabaghe2.insert(END, *name_tabaghe2)
    listbox_tabaghe3.insert(END, *name_tabaghe3)
    listbox_tabaghe4.insert(END, *name_tabaghe4)
    listbox_karevan.insert(END, *list_karevan)
    listbox_Extra.insert(END, *name_Extra)

    counter_male_zirzamin = len(os.listdir("database/Male/zirzamin"))
    counter_male_tabaghe1 = len(os.listdir("database/Male/tabaghe1"))
    counter_male_tabaghe2 = len(os.listdir("database/Male/tabaghe2"))
    counter_female_tabaghe3 = len(os.listdir("database/Female/tabaghe3"))
    counter_female_tabaghe4 = len(os.listdir("database/Female/tabaghe4"))
    counter_extra = len(os.listdir("database/Extra"))
    code = txtCode.get()
    txtCode.delete(0, END)
    if code.isdigit():
        pathM_zirzamin = "database/Male/zirzamin/" + str(code)
        pathM_tabaghe1 = "database/Male/tabaghe1/" + str(code)
        pathM_tabaghe2 = "database/Male/tabaghe2/" + str(code)
        pathF_tabaghe3 = "database/Female/tabaghe3/" + str(code)
        pathF_tabaghe4 = "database/Female/tabaghe4/" + str(code)
        pathE = "database/Extra/" + str(code)
        path_koll="database/koll/" + str(code)
        if os.path.isdir(pathM_zirzamin):
            print("Male")
            file = open(pathM_zirzamin + "/info.txt", "r")
            str_tabaghe = file.read()
            file.close()
            str_tabaghe = str_tabaghe.split("_")
            # pop up
            Show_window = Toplevel()
            Show_window.resizable(False, False)
            Show_window.geometry("350x580")
            Show_window.title("نمایش اطلاعات")

            Space5 = Label(Show_window, text=" ")
            Space5.pack()
            l_tabaghe = Label(Show_window, text="  موقعیت : " + "زیرزمین",
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="    نام :   " + str_tabaghe[0],
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="  تلفن :  " + str_tabaghe[1],
                              font=("tahoma", 18))
            l_tabaghe.pack()

            canvas = Canvas(Show_window, width=300, height=400, bd=5, relief='solid')
            canvas.pack()
            orginal_img = Image.open(pathM_zirzamin + '/img.jpg')
            resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, image=pic, anchor=NW)

            btn_close = Button(Show_window, text="بستن", command=Show_window.destroy)
            btn_close.pack()
            Show_window.mainloop()

        elif os.path.isdir(pathM_tabaghe1):
            print("Male")
            file = open(pathM_tabaghe1 + "/info.txt", "r")
            str_tabaghe = file.read()
            file.close()
            str_tabaghe = str_tabaghe.split("_")

            # pop up
            Show_window = Toplevel()
            Show_window.resizable(False, False)
            Show_window.geometry("350x580")
            Show_window.title("نمایش اطلاعات")

            Space5 = Label(Show_window, text=" ")
            Space5.pack()
            l_tabaghe = Label(Show_window, text="  موقعیت : " + "طبقه اول",
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="    نام :   " + str_tabaghe[0],
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="  تلفن :  " + str_tabaghe[1],
                              font=("tahoma", 18))
            l_tabaghe.pack()

            canvas = Canvas(Show_window, width=300, height=400, bd=5, relief='solid')
            canvas.pack()
            orginal_img = Image.open(pathM_tabaghe1 + '/img.jpg')
            resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, image=pic, anchor=NW)

            btn_close = Button(Show_window, text="بستن", command=Show_window.destroy)
            btn_close.pack()
            Show_window.mainloop()

        elif os.path.isdir(pathM_tabaghe2):
            print("Male")
            file = open(pathM_tabaghe2 + "/info.txt", "r")
            str_tabaghe = file.read()
            file.close()
            str_tabaghe = str_tabaghe.split("_")
            # pop up
            Show_window = Toplevel()
            Show_window.resizable(False, False)
            Show_window.geometry("350x580")
            Show_window.title("نمایش اطلاعات")

            Space5 = Label(Show_window, text=" ")
            Space5.pack()
            l_tabaghe = Label(Show_window, text="  موقعیت : " + "طبقه دوم",
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="    نام :   " + str_tabaghe[0],
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="  تلفن :  " + str_tabaghe[1],
                              font=("tahoma", 18))
            l_tabaghe.pack()

            canvas = Canvas(Show_window, width=300, height=400, bd=5, relief='solid')
            canvas.pack()
            orginal_img = Image.open(pathM_tabaghe2 + '/img.jpg')
            resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, image=pic, anchor=NW)

            btn_close = Button(Show_window, text="بستن", command=Show_window.destroy)
            btn_close.pack()
            Show_window.mainloop()

        elif os.path.isdir(pathF_tabaghe3):
            print("Female")
            file = open(pathF_tabaghe3 + "/info.txt", "r")
            str_tabaghe = file.read()
            file.close()
            str_tabaghe = str_tabaghe.split("_")
            # pop up
            Show_window = Toplevel()
            Show_window.resizable(False, False)
            Show_window.geometry("350x580")
            Show_window.title("نمایش اطلاعات")

            Space5 = Label(Show_window, text=" ")
            Space5.pack()
            l_tabaghe = Label(Show_window, text="  موقعیت : " + "طبقه سوم",
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="    نام :   " + str_tabaghe[0] ,
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="  تلفن :  " + str_tabaghe[1],
                              font=("tahoma", 18))
            l_tabaghe.pack()
            canvas = Canvas(Show_window, width=300, height=400, bd=5, relief='solid')
            canvas.pack()
            orginal_img = Image.open(pathF_tabaghe3 + '/img.jpg')
            resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, image=pic, anchor=NW)

            btn_close = Button(Show_window, text="بستن", command=Show_window.destroy)
            btn_close.pack()
            Show_window.mainloop()
        elif os.path.isdir(pathF_tabaghe4):
            print("Female")
            file = open(pathF_tabaghe4 + "/info.txt", "r")
            str_tabaghe = file.read()
            file.close()
            str_tabaghe = str_tabaghe.split("_")
            # pop up
            Show_window = Toplevel()
            Show_window.resizable(False, False)
            Show_window.geometry("350x580")
            Show_window.title("نمایش اطلاعات")

            Space5 = Label(Show_window, text=" ")
            Space5.pack()
            l_tabaghe = Label(Show_window, text="  موقعیت : " + "طبقه چهارم",
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="    نام :   " + str_tabaghe[0],
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="  تلفن :  " + str_tabaghe[1],
                              font=("tahoma", 18))
            l_tabaghe.pack()

            canvas = Canvas(Show_window, width=300, height=400, bd=5, relief='solid')
            canvas.pack()
            orginal_img = Image.open(pathF_tabaghe4 + '/img.jpg')
            resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, image=pic, anchor=NW)

            btn_close = Button(Show_window, text="بستن", command=Show_window.destroy)
            btn_close.pack()
            Show_window.mainloop()

        elif os.path.isdir(pathE):
            print("Male-Female")
            file = open(pathE + "/info.txt", "r")
            str_tabaghe = file.read()
            file.close()
            str_tabaghe = str_tabaghe.split("_")
            # pop up
            Show_window = Toplevel()
            Show_window.resizable(False, False)
            Show_window.geometry("350x580")
            Show_window.title("نمایش اطلاعات")

            Space5 = Label(Show_window, text=" ")
            Space5.pack()
            l_tabaghe = Label(Show_window, text="  موقعیت : " + "ساختمان شماره 2",
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="    نام :   " + str_tabaghe[0],
                              font=("tahoma", 18))
            l_tabaghe.pack()
            l_tabaghe = Label(Show_window, text="  تلفن :  " + str_tabaghe[1],
                              font=("tahoma", 18))
            l_tabaghe.pack()

            canvas = Canvas(Show_window, width=300, height=400, bd=5, relief='solid')
            canvas.pack()
            orginal_img = Image.open(pathE + '/img.jpg')
            resized_img = orginal_img.resize((310, 410), Image.ANTIALIAS)
            pic = ImageTk.PhotoImage(resized_img)
            canvas.create_image(0, 0, image=pic, anchor=NW)

            btn_close = Button(Show_window, text="بستن", command=Show_window.destroy)
            btn_close.pack()
            Show_window.mainloop()
        else:
            if os.path.isdir(path_koll):
                result = messagebox.askokcancel("اخطار", "این فرد قبلا از لیست حذف شده است آیا میخواهید ادامه دهید ؟ ")
                if result:
                    Scan_window = Toplevel()
                    Scan_window.resizable(False, False)
                    Scan_window.title("عضوگیری")
                    Space6 = Label(Scan_window, text=" : جنسیت ", font=("arial", 15, "bold"))
                    Space6.grid(row=1, column=0)
                    v = StringVar(Scan_window, "1")
                    style = Style(Scan_window)
                    style.configure("TRadiobutton", background="light green",
                                    foreground="red", font=("arial", 15, "bold"))
                    values = {"  مرد ": "1",
                              "  زن ": "2"}
                    c = 2
                    for (text, value) in values.items():
                        Radiobutton(Scan_window, text=text, variable=v, value=value,
                                    command=lambda: btn_path(v, w, pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2,
                                                             pathF_tabaghe3, pathF_tabaghe4, pathE,
                                                             counter_male_zirzamin,
                                                             counter_male_tabaghe1, counter_male_tabaghe2,
                                                             counter_female_tabaghe3, counter_female_tabaghe4,
                                                             counter_extra)).grid(row=c, column=0, pady=2)
                        c += 1

                    Space6 = Label(Scan_window, text=" : آدرس اسکن مدارک ", font=("arial", 15, "bold"))
                    Space6.grid(row=4, column=0)
                    w = Text(Scan_window, height=1, width=60, borderwidth=0)
                    w.grid(row=5, column=0)
                    l_name = Label(Scan_window, text=": نام ", font=("arial", 15, "bold"))
                    l_name.grid(row=6, column=0)
                    txtName = Entry(Scan_window)
                    txtName.grid(row=7, column=0)
                    l_tell = Label(Scan_window, text=": تلفن ", font=("arial", 15, "bold"))
                    l_tell.grid(row=8, column=0)
                    txtTell = Entry(Scan_window)
                    txtTell.grid(row=9, column=0, pady=3)
                    btn_scanner = Button(Scan_window, text="اسکن مدارک", command=lambda: btn_scan(w))
                    btn_scanner.grid(row=10, column=0)
                    btn_sh = Button(Scan_window, text="نمایش اسکن",
                                    command=lambda: btn_show(pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2,
                                                             pathF_tabaghe3, pathF_tabaghe4, pathE, v))
                    btn_sh.grid(row=11, column=0, pady=3)
                    btn_Save = Button(Scan_window, text="ذخیره",
                                      command=lambda: btn_save(v, pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2,
                                                               pathF_tabaghe3, pathF_tabaghe4, pathE, txtName, txtTell,
                                                               Scan_window, path_koll, listbox_zirzamin,
                                                               listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3,
                                                               listbox_tabaghe4, listbox_karevan, listbox_Extra))
                    btn_Save.grid(row=12, column=0)
                    Scan_window.mainloop()
            else:
                Scan_window = Toplevel()
                Scan_window.resizable(False, False)
                Scan_window.title("عضوگیری")
                Space6 = Label(Scan_window, text=" : جنسیت " , font=("arial", 15, "bold"))
                Space6.grid(row=1, column=0)
                v = StringVar(Scan_window, "1")
                style = Style(Scan_window)
                style.configure("TRadiobutton", background="light green",
                                foreground="red", font=("arial", 15, "bold"))
                values = {"  مرد ": "1",
                          "  زن ": "2"}
                c = 2
                for (text, value) in values.items():
                    Radiobutton(Scan_window, text=text, variable=v, value=value,
                                command=lambda: btn_path(v, w, pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2,
                                                         pathF_tabaghe3, pathF_tabaghe4, pathE, counter_male_zirzamin,
                                                         counter_male_tabaghe1, counter_male_tabaghe2,
                                                         counter_female_tabaghe3, counter_female_tabaghe4,
                                                         counter_extra)).grid(row=c, column=0, pady=2)
                    c += 1

                Space6 = Label(Scan_window, text=" : آدرس اسکن مدارک " , font=("arial", 15, "bold"))
                Space6.grid(row=4, column=0)
                w = Text(Scan_window, height=1,width=60, borderwidth=0)
                w.grid(row=5, column=0)
                l_name = Label(Scan_window, text=": نام ", font=("arial", 15, "bold"))
                l_name.grid(row=6, column=0)
                txtName = Entry(Scan_window)
                txtName.grid(row=7, column=0)
                l_tell = Label(Scan_window, text=": تلفن ", font=("arial", 15, "bold"))
                l_tell.grid(row=8, column=0)
                txtTell = Entry(Scan_window)
                txtTell.grid(row=9, column=0, pady=3)
                btn_scanner = Button(Scan_window, text="اسکن مدارک", command=lambda: btn_scan(w))
                btn_scanner.grid(row=10, column=0)
                btn_sh = Button(Scan_window, text="نمایش اسکن", command=lambda: btn_show(pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2, pathF_tabaghe3, pathF_tabaghe4, pathE,v))
                btn_sh.grid(row=11, column=0, pady=3)
                btn_Save = Button(Scan_window, text="ذخیره",
                                  command=lambda: btn_save(v, pathM_zirzamin, pathM_tabaghe1, pathM_tabaghe2,
                                                           pathF_tabaghe3, pathF_tabaghe4, pathE, txtName, txtTell,
                                                           Scan_window,path_koll, listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
                btn_Save.grid(row=12, column=0)
                Scan_window.mainloop()
    else:
        if not code == "":
            path = "database/karevan/" + code
            os.mkdir(path)
            karevan_window = Toplevel()
            karevan_window.title("اعضا کاروان")
            lb = Label(karevan_window, text="کد را وارد کنید :")
            lb.pack()
            En = Entry(karevan_window)
            En.pack()
            btn = Button(karevan_window, text="اضافه کردن", command=lambda: btn_add(path, En))
            btn.pack()
            karevan_window.mainloop()



MainWindow = Tk()
MainWindow.title("سامانه اسکان اربعین ")
MainWindow.resizable(False, False)
# Spaces
Space3 = Label(MainWindow, text=" ")
Space3.grid(row=0, column=223)

Space3 = Label(MainWindow, text="  عضویت  ", font=("arial", 15, "bold"))
Space3.grid(row=1, column=3, pady=5)
# Label
l_bala = Label(MainWindow, text=" : کد را وارد کنید ")
l_bala.grid(row=2, column=3, pady=0)

# txtCode
txtCode = Entry(MainWindow)
txtCode.grid(row=4, column=3,pady= 8)

# Button
btn_ns = Button(MainWindow, text="نمایش / عضو جدید ",command=lambda: btn_popUp(listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
btn_ns.grid(row=5, column=3)


Space3 = Label(MainWindow, text="  جست و جو  " , font=("arial", 15, "bold"))
Space3.grid(row=1, column=7, pady=5)
# Search
l_bala = Label(MainWindow, text=": نام را وارد کنید  ")
l_bala.grid(row=2, column=7, pady=0)
search = Entry(MainWindow)
search.grid(row=4, column=7, pady=8)
btn_search = Button(MainWindow, text="جست و جو ", command=lambda :btn_Search(search, listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
btn_search.grid(row=5, column=7)

list_zirzamin = os.listdir("database/Male/zirzamin")
list_tabaghe1 = os.listdir("database/Male/tabaghe1")
list_tabaghe2 = os.listdir("database/Male/tabaghe2")
list_tabaghe3 = os.listdir("database/Female/tabaghe3")
list_tabaghe4 = os.listdir("database/Female/tabaghe4")
list_Extra = os.listdir("database/Extra")
list_karevan = os.listdir("database/karevan")

for i in list_zirzamin:
    if not os.path.isfile("database/Male/zirzamin/" + i + "/info.txt") or not os.path.isfile(
            "database/Male/zirzamin/" + i + "/img.jpg"):
        if os.path.isdir("database/Male/zirzamin/" + i):
            shutil.rmtree("database/Male/zirzamin/" + i)
        else:
            print("no directory !! ")
for i in list_tabaghe1:
    if not os.path.isfile("database/Male/tabaghe1/" + i + "/info.txt") or not os.path.isfile(
            "database/Male/tabaghe1/" + i + "/img.jpg"):
        if os.path.isdir("database/Male/tabaghe1/" + i):
            shutil.rmtree("database/Male/tabaghe1/" + i)
        else:
            print("no directory !! ")
for i in list_tabaghe2:
    if not os.path.isfile("database/Male/tabaghe2/" + i + "/info.txt") or not os.path.isfile(
            "database/Male/tabaghe2/" + i + "/img.jpg"):
        if os.path.isdir("database/Male/tabaghe2/" + i):
            shutil.rmtree("database/Male/tabaghe2/" + i)
        else:
            print("no directory !! ")
for i in list_tabaghe3:
    if not os.path.isfile("database/Female/tabaghe3/" + i + "/info.txt") or not os.path.isfile(
            "database/Female/tabaghe3/" + i + "/img.jpg"):
        if os.path.isdir("database/Female/tabaghe3/" + i):
            shutil.rmtree("database/Female/tabaghe3/" + i)
        else:
            print("no directory !! ")
for i in list_tabaghe4:
    if not os.path.isfile("database/Female/tabaghe4/" + i + "/info.txt") or not os.path.isfile(
            "database/Female/tabaghe4/" + i + "/img.jpg"):
        if os.path.isdir("database/Female/tabaghe4/" + i):
            shutil.rmtree("database/Female/tabaghe4/" + i)
        else:
            print("no directory !! ")
for i in list_Extra:
    if not os.path.isfile("database/Extra/" + i + "/info.txt") or not os.path.isfile(
            "database/Extra/" + i + "/img.jpg"):
        if os.path.isdir("database/Extra/" + i):
            shutil.rmtree("database/Extra/" + i)
        else:
            print("no directiry !! ")

list_zirzamin = os.listdir("database/Male/zirzamin")
list_tabaghe1 = os.listdir("database/Male/tabaghe1")
list_tabaghe2 = os.listdir("database/Male/tabaghe2")
list_tabaghe3 = os.listdir("database/Female/tabaghe3")
list_tabaghe4 = os.listdir("database/Female/tabaghe4")
list_karevan = os.listdir("database/karevan")
list_Extra = os.listdir("database/Extra")
name_zirzamin = []
name_tabaghe1 = []
name_tabaghe2 = []
name_tabaghe3 = []
name_tabaghe4 = []
name_Extra = []


for temp in list_zirzamin:
    temp += "/info.txt"
    file = open("database/Male/zirzamin/" + temp, "r")
    str1 = file.read()
    file.close()
    str1 = str1.split("_")
    name_zirzamin += [str1[0]]

for temp in list_tabaghe1:
    temp += "/info.txt"
    file = open("database/Male/tabaghe1/" + temp, "r")
    str1 = file.read()
    file.close()
    str1 = str1.split("_")
    name_tabaghe1 += [str1[0]]

for temp in list_tabaghe2:
    temp += "/info.txt"
    file = open("database/Male/tabaghe2/" + temp, "r")
    str1 = file.read()
    file.close()
    str1 = str1.split("_")
    name_tabaghe2 += [str1[0]]

for temp in list_tabaghe3:
    temp += "/info.txt"
    file = open("database/Female/tabaghe3/" + temp, "r")
    str1 = file.read()
    file.close()
    str1 = str1.split("_")
    name_tabaghe3 += [str1[0]]

for temp in list_tabaghe4:
    temp += "/info.txt"
    file = open("database/Female/tabaghe4/" + temp, "r")
    str1 = file.read()
    file.close()
    str1 = str1.split("_")
    name_tabaghe4 += [str1[0]]

for temp in list_Extra:
    temp += "/info.txt"
    file = open("database/Extra/" + temp, "r")
    str1 = file.read()
    file.close()
    str1 = str1.split("_")
    name_tabaghe4 += [str1[0]]


Space2 = Label(MainWindow, text="     ")
Space2.grid(row=9, column=0)

lb_zirzmin = Label(MainWindow, text=" زیرزمین ")
lb_zirzmin.config(font=("tahoma", 12))
listbox_zirzamin = Listbox(MainWindow, height=15, width=30)
listbox_zirzamin.insert(END, *name_zirzamin)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_zirzamin, "zirzamin",
                                                                        listbox_zirzamin.get(
                                                                          listbox_zirzamin.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))

lb_zirzmin.grid(row=10, column=1)
listbox_zirzamin.grid(row=11, column=1, padx=2)
btn_delete.grid(row=12, column=1, pady=3)

fasele = Label(MainWindow, text="")
fasele.grid(row=10, column=2)

lb_tabaghe1 = Label(MainWindow, text=" طبقه اول ")
lb_tabaghe1.config(font=("tahoma", 12))
listbox_tabaghe1 = Listbox(MainWindow, height=15, width=30)
listbox_tabaghe1.insert(END, *name_tabaghe1)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_tabaghe1, "tabaghe1",
                                                                        listbox_tabaghe1.get(
                                                                            listbox_tabaghe1.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
lb_tabaghe1.grid(row=10, column=3)
listbox_tabaghe1.grid(row=11, column=3, padx=2)
btn_delete.grid(row=12, column=3, pady=3)

fasele = Label(MainWindow, text="")
fasele.grid(row=10, column=4)

lb_tabaghe2 = Label(MainWindow, text=" طبقه دوم ")
lb_tabaghe2.config(font=("tahoma", 12))
listbox_tabaghe2 = Listbox(MainWindow, height=15, width=30)
listbox_tabaghe2.insert(END, *name_tabaghe2)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_tabaghe2, "tabaghe2",
                                                                        listbox_tabaghe2.get(
                                                                            listbox_tabaghe2.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
lb_tabaghe2.grid(row=10, column=5)
listbox_tabaghe2.grid(row=11, column=5, padx=2)
btn_delete.grid(row=12, column=5, pady=3)

fasele = Label(MainWindow, text="")
fasele.grid(row=12, column=6)

lb_tabaghe3 = Label(MainWindow, text=" طبقه سوم ")
lb_tabaghe3.config(font=("tahoma", 12))
listbox_tabaghe3 = Listbox(MainWindow, height=15, width=30)
listbox_tabaghe3.insert(END, *name_tabaghe3)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_tabaghe3, "tabaghe3",
                                                                        listbox_tabaghe3.get(
                                                                            listbox_tabaghe3.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
lb_tabaghe3.grid(row=10, column=7)
listbox_tabaghe3.grid(row=11, column=7, padx=2)
btn_delete.grid(row=12, column=7, pady=3)

fasele = Label(MainWindow, text="")
fasele.grid(row=10, column=8)

lb_tabaghe4 = Label(MainWindow, text=" طبقه چهارم ")
lb_tabaghe4.config(font=("tahoma", 12))
listbox_tabaghe4 = Listbox(MainWindow, height=15, width=30)
listbox_tabaghe4.insert(END, *name_tabaghe4)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_tabaghe4, "tabaghe4",
                                                                        listbox_tabaghe4.get(
                                                                            listbox_tabaghe4.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
lb_tabaghe4.grid(row=10, column=9)
listbox_tabaghe4.grid(row=11, column=9, padx=2)
btn_delete.grid(row=12, column=9, pady=3)

fasele = Label(MainWindow, text="   ")
fasele.grid(row=10, column=10)

fasele = Label(MainWindow, text="  ")
fasele.grid(row=13, column=0)
fasele = Label(MainWindow, text="  ")
fasele.grid(row=14, column=0)

lb_karevan = Label(MainWindow, text=" کاروان ها ")
lb_karevan.config(font=("tahoma", 12))
listbox_karevan = Listbox(MainWindow, height=15, width=30)
listbox_karevan.insert(END, *list_karevan)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_karevan, "karevan",
                                                                        listbox_karevan.get(
                                                                            listbox_karevan.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
lb_karevan.grid(row=14, column=1)
listbox_karevan.grid(row=15, column=1, padx=2)
btn_delete.grid(row=16, column=1, pady=3)

fasele = Label(MainWindow, text="")
fasele.grid(row=14, column=2)

lb_Extra = Label(MainWindow, text=" ساختمان شماره 2 ")
lb_Extra.config(font=("tahoma", 12))
listbox_Extra = Listbox(MainWindow, height=15, width=30)
listbox_Extra.insert(END, *name_Extra)
btn_delete = Button(MainWindow, text="حذف", command=lambda: list_del(listbox_Extra, "Extra",
                                                                        listbox_Extra.get(
                                                                            listbox_Extra.curselection()),listbox_zirzamin, listbox_tabaghe1, listbox_tabaghe2, listbox_tabaghe3, listbox_tabaghe4, listbox_karevan, listbox_Extra))
lb_Extra.grid(row=14, column=3)
listbox_Extra.grid(row=15, column=3, padx=2)
btn_delete.grid(row=16, column=3, pady=3)


fasele = Label(MainWindow, text=" ")
fasele.grid(row=17, column=0)
fasele = Label(MainWindow, text=" ")
fasele.grid(row=18, column=0)

txtCode.focus_set()
MainWindow.columnconfigure(0, weight=1)
mainloop()
