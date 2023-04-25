import os

from documents.ExcelTranslator import ExcelTranslator

app_id = ''
key = ''

default_file = r"C:\Users\iMorning\Downloads\新建文件夹\率土之滨全赛季详解.xlsx"


def make_out_file(file_name):
    dir_path = os.path.abspath(os.path.abspath(file_name))
    new_file_name = os.path.splitext(dir_path)[0] + '_translate' + os.path.splitext(dir_path)[1]
    return new_file_name


if __name__ == "__main__":
    xlsx_translator = ExcelTranslator(default_file, make_out_file(default_file))
    xlsx_translator.translate(des_lang='en')
