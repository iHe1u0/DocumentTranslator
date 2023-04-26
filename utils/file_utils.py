import os


def make_out_file_path(file_name, default_sep="_translate"):
    dir_path = os.path.abspath(os.path.abspath(file_name))
    new_file_name = os.path.splitext(
        dir_path)[0] + default_sep + os.path.splitext(dir_path)[1]
    return new_file_name


def check_file_exist(file_path):
    """
    检查文件是否存在

    :param file_path: 文件路径（可以是相对路径或绝对路径）
    :return: 如果文件存在返回True，否则返回False
    """
    return os.path.isfile(file_path)
