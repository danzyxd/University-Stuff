import tkinter as tk
import sys
from tkinter import messagebox


class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.geometry("500x400")
        self.minsize(300, 200)

        self._build_menu()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.editor = tk.Text(wrap="none")
        self.editor.grid(column=0, row=0, sticky=tk.NSEW)

        self.scrollbar_y = tk.Scrollbar(orient="vertical", command=self.editor.yview)
        self.scrollbar_y.grid(column=1, row=0, sticky=tk.NS)
        self.scrollbar_x = tk.Scrollbar(orient="horizontal", command=self.editor.xview)
        self.scrollbar_x.grid(column=0, row=1, sticky=tk.EW)
        self.editor["yscrollcommand"] = self.scrollbar_y.set
        self.editor["xscrollcommand"] = self.scrollbar_x.set

    def _build_menu(self):
        main_menu_list = [
            ["Файл", self.file_menu, {"Новый              Ctrl+N": self.btn_new, "Открыть           Ctrl+O": self.btn_open, "Сохранить        Ctrl+S": self.btn_save, "Сохранить как... ": self.btn_save_as, "Выход               Ctrl+Q": self.btn_exit}],
            ["Правка", self.edit_menu, {"Копировать": self.btn_copy, "Вставить": self.btn_paste, "Параметры": self.btn_settings}],
            ["Справка", self.info_menu, {"Содержание": self.btn_info, "О программе...": self.btn_about}]
        ]

        main_menu = tk.Menu()
        for elem in main_menu_list:
            elem[1] = tk.Menu(tearoff=0)
            for i, (key, value) in enumerate(elem[2].items()):  # enumerate
                if i == len(elem[2]) - 1:
                    elem[1].add_separator()
                elem[1].add_command(label=key, command=value)
            main_menu.add_cascade(label=elem[0], menu=elem[1])

        self.config(menu=main_menu)

    def btn_new():
        pass

    def btn_open():
        pass

    def btn_save():
        pass

    def btn_save_as():
        pass

    def btn_exit(self):
        sys.exit(0)

    def btn_copy(self):
        try:
            selected_text = self.editor.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.clipboard_append(selected_text)
        except tk.TclError:
            pass

    def btn_paste(self):
        try:
            clipboard_text = self.clipboard_get()
            try:
                selected_text = self.editor.get(tk.SEL_FIRST, tk.SEL_LAST)
                if selected_text != '':
                    self.editor.replace(tk.SEL_FIRST, tk.SEL_LAST, clipboard_text)
                else:
                    self.editor.insert(tk.INSERT, clipboard_text)
            except tk.TclError:
                self.editor.insert(tk.INSERT, clipboard_text)
        except tk.TclError:
            pass

    def btn_settings():
        pass

    def btn_info(self):
        def close_window():
            window.destroy()

        window = tk.Toplevel()
        window.title("Справка")
        window.geometry("300x150")
        label = tk.Label(window, text="Приложение с графический интерфейсом\n'Блокнот TCD' (файл приложения: TCD).\nПозволяет: создавать / открывать / сохранять\nзашифрованный текстовый файл, предусмотрены\nввод и сохранение личного ключа,\nвывод не модальной формы 'Справка',\nвывод модальной формы 'О программе'.")
        label.pack(fill="both", expand=True)

        button = tk.Button(window, text="Закрыть", command=close_window)
        button.pack(pady=10)

    def btn_about(self):
        messagebox.showinfo("О программе", "Программа для 'прозрачного шифрования'\n(c) Kireev A.A., 2025\n\nПользуясь случаем, хочу выразить публичную\nблагодарность своим родителям:\nГильмие Арслановне и Азату Салаватовичу.")

    file_menu, edit_menu, info_menu = None, None, None


window = Notepad()
window.mainloop()
