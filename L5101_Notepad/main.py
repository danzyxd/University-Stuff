import tkinter as tk
import sys
from tkinter import messagebox, font, filedialog
import cryptography


class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Безымянный - Notepad")
        self.geometry("800x500")
        self.minsize(300, 200)

        # self.iconbitmap(default="./edit.ico")

        self._build_menu()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.my_font = ["Consolas", 24]
        self.editor = tk.Text(wrap="none", font=(self.my_font[0], self.my_font[1]))
        self.editor.grid(column=0, row=0, sticky=tk.NSEW)

        self.scrollbar_y = tk.Scrollbar(orient="vertical", command=self.editor.yview)
        self.scrollbar_y.grid(column=1, row=0, sticky=tk.NS)
        self.scrollbar_x = tk.Scrollbar(orient="horizontal", command=self.editor.xview)
        self.scrollbar_x.grid(column=0, row=1, sticky=tk.EW)
        self.editor["yscrollcommand"] = self.scrollbar_y.set
        self.editor["xscrollcommand"] = self.scrollbar_x.set

        self.editor.bind("<<Modified>>", self.text_change)

        self.editor.focus_set()

        try:
            with open("./AmTCD.ini", "r", encoding="utf-8") as file:
                pass
        except FileNotFoundError:
            with open("./AmTCD.ini", "w", encoding="utf-8") as self.file:
                keyuser = cryptography.generate_new_key()
                self.file.write(f"[main]\nkeyuser = {keyuser}")



    def _build_menu(self):
        main_menu_list = [
            ["Файл", self.file_menu, {"Новый              Ctrl+N": self.btn_new, "Открыть           Ctrl+O": self.btn_open, "Сохранить        Ctrl+S": self.btn_save, "Сохранить как... ": self.btn_save_as, "Выход               Ctrl+Q": self.btn_exit}],
            ["Правка", self.edit_menu, {"Копировать                  Ctrl+C": self.btn_copy, "Вставить                        Crtl+V": self.btn_paste, "Увл. разм. шрифта     Ctrl+": self.btn_scale_up, "Умн. разм. шрифта    Ctrl-": self.btn_scale_down}],
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

    def text_change(self, event=None):
        if self.editor.edit_modified():
            self.is_edited = True
            self.editor.edit_modified(False)
        self.window_title()

    def window_title(self):
        global file_path, is_edited
        if self.file_path:
            title = self.file_path.split('/')[-1]
        else:
            title = "Безымянный"
        if self.is_edited:
            title = f"*{title}"
        self.title(f"{title} - Notepad")

    def btn_new(self):
        global file_path, is_edited
        if self.is_edited:
            self.btn_save()
        self.file_path = None
        self.editor.delete("1.0", "end")
        self.is_edited = False
        self.window_title()

    def btn_open(self):
        global file_path, is_edited
        if self.is_edited:
            self.btn_save()
        self.tmp_file_path = filedialog.askopenfilename(defaultextension=".txtx", filetypes=[("Text files", "*.txtx"), ("All files", "*.*")])
        if not self.tmp_file_path:
            return
        self.file_path = self.tmp_file_path
        with open(self.file_path, "r", encoding="utf-8") as file:
            text = file.read()
        try:
            decrypted_text = cryptography.decrypt(text)
            self.editor.delete("1.0", "end")
            self.editor.insert("1.0", decrypted_text)
            self.is_edited = False
            self.editor.edit_modified(False)
            self.window_title()
        except ValueError:
            messagebox.showerror("Ошибка", "Файл поврежден или имеет неверный формат!")

    def btn_save(self):
        global file_path
        if self.file_path is None:
            self.btn_save_as()
        else:
            self.save_new_file()

    def btn_save_as(self):
        global file_path
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txtx", filetypes=[("Text files", "*.txtx"), ("All files", "*.*")])
        if not self.file_path:
            return
        self.save_new_file()

    def save_new_file(self):
        self.text = self.editor.get("1.0", "end").strip()
        encrypted_text = cryptography.encrypt(self.text)
        with open(self.file_path, "w", encoding="utf-8") as self.file:
            self.file.write(encrypted_text)
        self.is_edited = False
        self.window_title()

    def btn_exit(self):
        sys.exit(0)

    def btn_copy(self):
        self.editor.event_generate("<<Copy>>")

    def btn_paste(self):
        self.editor.event_generate("<<Paste>>")

    def btn_scale_down(self):
        if self.my_font[1] == 12:
            return
        self.my_font[1] -= 8
        self.editor.config(font=(self.my_font[0], self.my_font[1]))

    def btn_scale_up(self):
        if self.my_font[1] == 64:
            return 
        self.my_font[1] += 8
        self.editor.config(font=(self.my_font[0], self.my_font[1]))

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
    file_path, is_edited = None, False

if __name__ == "__main__":
    window = Notepad()
    window.mainloop()
