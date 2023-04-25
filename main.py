import json
from translate import translate
from excel import xlsx

default_file = "c:/temp/201011053018055(3).xlsx"
if __name__ == "__main__":
    xlsx_translator = xlsx.Xlsx(default_file)
    xlsx_translator.translate()
