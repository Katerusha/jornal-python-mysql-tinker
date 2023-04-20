# безопасный ввод пародя без повторений
from getpass import getpass
# для подключения к бд MySQL
import mysql.connector
from mysql.connector import connect, Error
# импортируем библиотеку tkinter всю сразу
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
# библиотека для изменения идображений
import PIL
from PIL import Image
from PIL import *
#
import Vhode_s_BD 


surname=(Vhode_s_BD.surname)
name=(Vhode_s_BD.name)
patronymic=(Vhode_s_BD.patronymic)
# print(n_surname)

class Main(tk.Frame):
    def __init__(self, root1):
        super().__init__(root1)
        self.init_main()
        self.db = db
        self.view_records()

    def view_records(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.db.get_all_records():
            self.tree.insert('', 'end', values=row)

# Главное окно
    def init_main(self):
        toolbar = tk.Frame(bg='beige', bd=2)
        toolbar.pack(side=tk.LEFT, fill=tk.Y)
        self.add_img = tk.PhotoImage(file='Иконки/dobav.png').subsample(3, 3)
        btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='beige',
                                    bd=0, compound=tk.LEFT, image=self.add_img)
        btn_open_dialog.pack(side=tk.TOP)
        
        self.delete_img = tk.PhotoImage(file='Иконки/tresh.png').subsample(3, 3)
        btn_delete_dialog = tk.Button(toolbar, text='Удалить', bg='beige', bd=0, image=self.delete_img,
                                      compound=tk.LEFT, command=self.delete_records)
        btn_delete_dialog.pack(side=tk.TOP)
        
        self.update_img = tk.PhotoImage(file='Иконки/redakt.png').subsample(3, 3)
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='beige', bd=0, image=self.update_img,
                                    compound=tk.LEFT, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.TOP)

        self.search_img = tk.PhotoImage(file='Иконки/poisk.png').subsample(3, 3)
        btn_search = tk.Button(toolbar, text='Поиск', bg='beige', bd=0, image=self.search_img,
                               compound=tk.LEFT, command=self.open_search_dialog)

        btn_search.pack(side=tk.TOP)

        self.refresh_img = tk.PhotoImage(file='Иконки/obnov.png').subsample(3, 3)
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='beige', bd=0, image=self.refresh_img,
                                compound=tk.LEFT, command=self.view_records)
        btn_refresh.pack(side=tk.TOP)

        # self.history_img = tk.PhotoImage(file='Иконки/history.png')
        # btn_open_history = tk.Button(toolbar, text='История', command=self.open_history, bg='beige',
        #                             bd=0, compound=tk.TOP, image=self.add_img)
        # im = self.add_img.resize((self.add_img.width // 4, self.add_img.height // 4))
        # btn_open_dialog.pack(side=tk.LEFT)



        self.tree = ttk.Treeview(self, columns=('ID', 'date','time', 'category', 'section','lot'), height=50, show='headings')

        self.tree.column("#0", width=0, stretch=tk.YES)
        self.tree.column('ID', width=200, anchor=tk.CENTER)
        self.tree.column('date', width=200, anchor=tk.CENTER)
        self.tree.column('time', width=200, anchor=tk.CENTER)
        self.tree.column('category', width=300, anchor=tk.CENTER)
        self.tree.column('section', width=300, anchor=tk.CENTER)
        self.tree.column('lot', width=300, anchor=tk.CENTER)

        self.tree.heading('ID', text='Номер ПП')
        self.tree.heading('date', text='Дата')
        self.tree.heading('time', text='Время')
        self.tree.heading('category', text='Код отхода')
        self.tree.heading('section', text='Отдел')
        self.tree.heading('lot', text='Образовалось т.(шт)')

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)
        # имя пользователя
        
        name_block = tk.Label(root1, text=f'Фамилия: {surname}\nИмя: {name}\nОтчество: {patronymic}')
        name_block.pack()

# История


# Добавление данных
    def records(self,id_r, date, time, category, section, lot):
        self.db.insert_data(self,id_r, date, time, category, section, lot)
        self.view_records()

# Обновление данных
        def update_record(self,id_r, date, time, category, section, lot):
            self.c.execute('''
            UPDATE register
            SET date=%s, time=%s, category=%s, section=%s, lot=%s
            WHERE id=%s
        ''', (date, time, category, section, lot, id_r))
        self.conn.commit()
        self.view_records()

# Вывод данных
    def view_records(self):
        self.db.c.execute('''SELECT * FROM register''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

# Удаление данных
    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM register WHERE id_r=? ''', (self.tree.set(selection_item, '#1'),))
            self.db.conn.commit()
            self.view_records()

# Поиск данных
    def search_records(self, id_r):
        id_r = ('%' + id_r + '%',)
        self.db.c.execute('''SELECT * FROM register WHERE id_r LIKE ?''', id_r)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

# Открытие дочернего окна
    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

# Дочернее окно
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root1)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('400x240+400+300')
        self.resizable(True, True)

        label_date = tk.Label(self, text='Дата')
        label_date.place(x=50, y=20)

        label_time = tk.Label(self, text='Время')
        label_time.place(x=50, y=50)

        label_select = tk.Label(self, text='Код отхода')
        label_select.place(x=50, y=80)
        
        label_section = tk.Label(self, text='Отдел')
        label_section.place(x=50, y=110)

        label_lot = tk.Label(self, text='Образовалось т.')
        label_lot.place(x=50, y=140)

        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=200, y=20)

        self.entry_time = ttk.Entry(self)
        self.entry_time.place(x=200, y=50)

        self.entry_category = ttk.Entry(self)
        self.entry_category.place(x=200, y=80)

        self.entry_section = ttk.Entry(self)
        self.entry_section.place(x=200, y=110)

        self.entry_lot = ttk.Entry(self)
        self.entry_lot.place(x=200, y=140)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_date.get(),
                                                                 self.entry_time.get(),
                                                                 self.entry_category.get(),
                                                                 self.entry_section.get(),
                                                                 self.entry_lot.get()))

        self.grab_set()
        self.focus_set()


# Класс обновления унаследованный от дочернего окна
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()


    def init_edit(self):
        self.title('Редактировать ')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_register_record(self.entry_date.get(),
                                                                          self.entry_time.get(),
                                                                          self.entry_category.get(),
                                                                          self.entry_section.get(),
                                                                          self.entry_lot.get()))
        self.btn_ok.destroy()


    def default_data(self):
        self.db.c.execute('''SELECT * FROM register WHERE id_r=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchone()
        self.entry_date.insert(0, row[1])
        self.entry_time.insert(0, row[2])
        if row[3] != 1:
            self.entry_category.current(1)
        self.entry_section.insert(0, row[4])
        self.entry_lot.insert(0, row[5])


# Поиск по наименованию
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

 # Создание базы данных
class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="00000",
            database="jornal"
        )
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS register (
                            id_r INT(5) UNSIGNED ZEROFILL PRIMARY KEY AUTO_INCREMENT,
                            date DATE NOT NULL,
                            time TIME NOT NULL,
                            category INT(7) UNSIGNED ZEROFILL NOT NULL,
                            section VARCHAR(100) NOT NULL,
                            lot DECIMAL(50,0) NOT NULL
                        );'''
        )
        self.conn.commit()
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS staff (
                            id_s INT(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            surname VARCHAR(50),
                            name VARCHAR(50),
                            patronymic VARCHAR(50),
                            job VARCHAR(100),
                            phone VARCHAR(15),
                            login VARCHAR(50),
                            password VARCHAR(50),
                            tip ENUM('admin', 'polzovatel')
                        );'''
        )
        self.conn.commit()
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS wastes (
                id_w INT(5) UNSIGNED ZEROFILL PRIMARY KEY AUTO_INCREMENT,
                category INT(7) UNSIGNED ZEROFILL NOT NULL,
                name_w VARCHAR(50) NOT NULL,
                lot DECIMAL(50,0) NOT NULL);'''
        )
        self.conn.commit()



    def insert_data(self, date, time, category, section, lot):
        sql = """INSERT INTO register (date, time, category, section, lot) VALUES (%s, %s, %s, %s, %s)"""
        values = (date, time, category, section, lot)
        self.c.execute(sql, values)
        self.conn.commit()
        
# Основной код для запуска
if __name__ == "__main__":
    root1 = tk.Tk()
    db = DB()
    app = Main(root1)
    app.pack()
    root1.title("Журнал учета отходов первого класса")
    root1.geometry("1800x1000+300+200")
    root1.resizable(True, True)
    root1.mainloop()
