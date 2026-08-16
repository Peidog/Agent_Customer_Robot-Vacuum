import logging
from utils.path_tool import get_abs_path 
import os
from datetime import datetime


# 日志保存的根目录
LOG_ROOT = get_abs_path("logs")

# 确保日志的目录存在
os.makedirs(LOG_ROOT, exist_ok=True) 

# 配置日志格式
DEFAULT_LOG_FORMAT = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)


def get_logger(
        name: str = "agent", 
        console_level: int = logging.INFO, # 控制台日志级别
        file_level: int = logging.DEBUG, # 文件日志级别
        log_file = None
) -> logging.Logger:
    logger = logging.getLogger(name)  # 获取指定名称的日志记录器
    logger.setLevel(logging.DEBUG)  # 设置日志记录器的级别

    # 避免重复添加Handler
    if logger.handlers:
        return logger

    # 创建控制台Handler
    console_handler = logging.StreamHandler() 
    console_handler.setLevel(console_level) 
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(console_handler)

    # 创建文件Handler
    if not log_file: 
        # 日志文件存放路径
        log_file = os.path.join(LOG_ROOT, f"{name}_{datetime.now().strftime('%Y%m%d')}.log")

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(file_handler)

    return logger


# 快捷获取日志器（from utils.logger_handler import logger） 
logger = get_logger()


if __name__ == "__main__":
    logger.info("This is an info message.")
    logger.error("This is an error message.")
    logger.warning("This is a warning message.")
    logger.debug("This is a debug message.")
    