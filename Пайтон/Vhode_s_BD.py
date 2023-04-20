from tkinter import *
import tkinter.messagebox
import mysql.connector
import subprocess

#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="00000",database="jornal")
cursordb = connectiondb.cursor()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Вход в учетную запись")
    root2.geometry("450x300")
    root2.config(bg="white")

    global login_verification
    global password_verification
    Label(root2, text='Пожалуйста, введите данные своей учетной записи', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="#000000",
    bg="#ffefd2",width=300).pack()
    login_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Логин :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=login_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Пароль :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Войти", bg="#ffefd2", fg='#000000', relief="groove", font=('arial', 12, 'bold'),command=verify_login).pack()
    Label(root2, text="")

  
def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Добро пожаловать")
    logged_message.geometry("500x100")
    Label(logged_message, text="Вход в систему удачен!... Добро пожаловать {} ".format(login_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Вход", bg="#ffefd2", fg='#000000', relief="groove", font=('arial', 12, 'bold'),
            command=logged_destroy).pack()
# command=lambda:[close_full(), logged_destroy() ])

def failed():
    global failed_message
    global failed_destroy
    failed_message = Toplevel(root2)
    failed_message.title("Ошибка")
    failed_message.geometry("500x100")
    Label(failed_message, text="Неверный логин или пароль", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="#ffefd2", fg='#000000', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()


def verify_login():
    global verify_login
    # global surname, name, patronymic # определяем глобальные переменные
    user_verification = login_verification.get()
    pass_verification = password_verification.get()
    sql = "SELECT surname, name, patronymic, login, password FROM staff WHERE login = %s AND password = %s"
    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            surname = i[0]
            name = i[1]
            patronymic = i[2]
            logged()
            break
    else:
        failed()

surname = verify_login()
name = verify_login()
patronymic = verify_login()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Вход в журнал", "Вы действительно хотите выйти?")
    if wayOut > 0:
        root.destroy()
    return

def main_display():
    global root
    root = Tk()
    print("Main window created")
    root.config(bg="white")
    root.title("Вход в журнал")
    root.geometry("450x250")
    Label(root,text='Добро пожаловать в журнал', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="#000000",
    bg="#ffefd2",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Войти', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="#000000",
    bg="#ffefd2",command=login).pack()
    Label(root,text="").pack()
    Button(root,text='Выход', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="#000000",
    bg="#ffefd2",command=Exit).pack()
    Label(root,text="").pack()


# def close_full():
#     root.destroy()

def logged_destroy():
    root2.destroy()  # закрыть окно входа в учетную запись
    root.destroy()  # закрыть окно входа в журнал
    subprocess.run(["python", "./main.py"])  # запустить другой файл
    
main_display()
root.mainloop()
    

