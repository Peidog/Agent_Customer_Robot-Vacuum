"""
pip install -U langchain langchain-community 
"""

import os
import hashlib
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def get_file_md5_hex(filepath: str): # 获取文件的md5哈希（十六进制字符串）
    if not os.path.exists(filepath):
        logger.error(f"[md5计算] 文件{filepath}不存在")
        return None
    if not os.path.isfile(filepath):
        logger.error(f"[md5计算] {filepath}不是文件")
        return None

    md5_obj = hashlib.md5()

    chunk_size = 4096 # 4KB分片，避免文件过大爆内存
    try:
        with open(filepath, 'rb') as f: # 必须以二进制模式读取文件
            chunk = f.read(chunk_size)
            while chunk:
                md5_obj.update(chunk)
                chunk = f.read(chunk_size)
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"[md5计算] 读取文件{filepath}时发生错误: {str(e)}")
        return None


def listdir_with_allowed_type(path: str, allowed_types: tuple[str]): # 返回文件夹内的文件列表（允许的文件后缀）
    files = []

    if not os.path.isdir(path):
        logger.error(f"[获取允许类型的文件] {path} 不是文件夹")
        return files

    for f in os.listdir(path):
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))

    return tuple(files)


def pdf_loader(filepath: str, passwd = None) -> list[Document]: # 加载pdf文件
    return PyPDFLoader(filepath, passwd).load()


def txt_loader(filepath: str) -> list[Document]: # 加载txt文件
    return TextLoader(filepath, encoding='utf-8').load()

