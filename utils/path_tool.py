"""
为整个项目提供统一的绝对路径
"""

import os


def get_project_root() -> str:
    """
    获取项目根目录
    :return: 字符串根目录
    """
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取当前文件夹的绝对路径
    current_dir = os.path.dirname(current_file)
    # 获取项目根目录
    project_root = os.path.dirname(current_dir)

    return project_root


def get_abs_path(relative_path: str) -> str:
    """
    获取相对路径对应的绝对路径
    :param relative_path: 相对路径
    :return: 绝对路径
    """ 
    # 获取项目根目录 
    project_root = get_project_root()
    # 拼接绝对路径
    return os.path.join(project_root, relative_path)


if __name__ == "__main__":
    print(get_abs_path("utils/path_tool.py"))
  