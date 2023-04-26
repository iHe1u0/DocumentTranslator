import time
import tkinter as tk
from tkinter import filedialog
from enum import Enum
from tkinter import ttk

import threading
import queue

from documents.ExcelTranslator import ExcelTranslator
from utils import file_utils


class MainUI:
    __root = tk.Tk()
    __thread = None

    def __init__(self):
        current_row = 0
        root = self.__root
        root.geometry(self.window_size(60, 50))
        is_running = False
        # 创建文件选择器所在的Frame组件，并通过grid()进行布局管理
        file_frame = tk.Frame(root)
        file_frame.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        # 创建标签和按钮，并添加到file_frame中
        open_file_button = ttk.Button(file_frame, text="选择文件",
                                      command=self.open_file_dialog)
        open_file_button.pack(side=tk.LEFT, padx=Padding.START.value)
        file_chooser_entry = ttk.Entry(file_frame, text="请选择一个文件:", width=50)
        file_chooser_entry.pack(
            side=tk.RIGHT, fill=tk.X, expand=True, padx=Padding.END.value)

        # 创建源语言选择
        source_lang_frame = tk.Frame(root)
        source_lang_frame.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        source_lang_label = ttk.Label(source_lang_frame, text="源语言：", width=8)
        source_lang_label.pack(side=tk.LEFT, padx=Padding.START.value)
        source_lang_radio_frame = tk.Frame(source_lang_frame)
        source_lang_radio_frame.pack(side=tk.LEFT)

        source_lang_var = tk.StringVar(value="auto")
        auto_radio_button = ttk.Radiobutton(
            source_lang_radio_frame, text="自动检测", variable=source_lang_var, value="auto")
        zh_radio_button = ttk.Radiobutton(
            source_lang_radio_frame, text="中文", variable=source_lang_var, value="zh")
        en_radio_button = ttk.Radiobutton(
            source_lang_radio_frame, text="英文", variable=source_lang_var, value="en")
        ja_radio_button = ttk.Radiobutton(
            source_lang_radio_frame, text="日文", variable=source_lang_var, value="jp")

        auto_radio_button.pack(side=tk.LEFT)
        zh_radio_button.pack(side=tk.LEFT)
        en_radio_button.pack(side=tk.LEFT)
        ja_radio_button.pack(side=tk.LEFT)

        # 创建目标语言选择
        to_lang_frame = tk.Frame(root)
        to_lang_frame.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        to_lang_label = ttk.Label(to_lang_frame, text="目标语言：", width=8)
        to_lang_label.pack(side=tk.LEFT, padx=Padding.START.value)
        to_lang_radio_frame = tk.Frame(to_lang_frame)
        to_lang_radio_frame.pack(side=tk.LEFT)

        to_lang_var = tk.StringVar(value="zh")
        zh_radio_button = ttk.Radiobutton(
            to_lang_radio_frame, text="中文", variable=to_lang_var, value="zh")
        en_radio_button = ttk.Radiobutton(
            to_lang_radio_frame, text="英文", variable=to_lang_var, value="en")
        ja_radio_button = ttk.Radiobutton(
            to_lang_radio_frame, text="日文", variable=to_lang_var, value="jp")

        auto_radio_button.pack(side=tk.LEFT)
        zh_radio_button.pack(side=tk.LEFT)
        en_radio_button.pack(side=tk.LEFT)
        ja_radio_button.pack(side=tk.LEFT)

        # 开始/停止
        status_frame = tk.Frame(root)
        status_frame.grid(row=current_row, column=0, sticky="w")
        current_row += 1

        self.button_status_text = tk.StringVar(value="开始")
        op_button = ttk.Button(
            status_frame, textvariable=self.button_status_text, command=self.click)
        op_button.pack(side=tk.LEFT, padx=Padding.START.value)

        # for global use
        self.file_chooser_entry = file_chooser_entry
        self.source = source_lang_var
        self.to = to_lang_var
        self.is_running = is_running

        root.mainloop()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select an Excel file",
            filetypes=(("Excel files", "*.xlsx;*.xls"), ("all files", "*.*"))
        )
        self.file_chooser_entry.delete(0, 'end')
        self.file_chooser_entry.insert(0, file_path)

    def window_size(self, width_percent, height_percent):
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        width = int(screen_width * width_percent / 100)
        height = int(screen_height * height_percent / 100)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        return f'{width}x{height}+{x}+{y}'

    def click(self):
        status_text = self.button_status_text
        if self.is_running:
            status_text.set("开始")
            self.is_running = False
        else:
            input_file = self.file_chooser_entry.get()
            source = self.source.get()
            to = self.to.get()
            status_text.set("停止")
            self.is_running = True
            self.__thread = threading.Thread(target=self.translate,
                                             args=(input_file,
                                                   file_utils.make_out_file_path(input_file),
                                                   source,
                                                   to))
            self.__thread.start()
        print(self.__thread.is_alive())
        print(self.__thread.isAlive())

    def translate(self, input_file, output_file, source_lang, to_lang):
        test(input_file, output_file)
        self.button_status_text.set("完成")
        self.is_running = False


def test(source, output):
    test_index = 0
    while test_index < 5:
        test_index += 1
        print(test_index)
        time.sleep(1)
    return 'done'


class Padding(Enum):
    START = 10.0,
    END = 10.0,
    TOP = 0.0,
    BOTTOM = 0.0
