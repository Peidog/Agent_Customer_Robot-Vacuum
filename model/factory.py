"""
编辑用户环境变量，新建
OPENAI_API_KEY = "..."
DASHSCOPE_API_KEY = "..."
"""

from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain_community.chat_models.tongyi import BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from utils.config_handler import rag_conf


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings | BaseChatModel]: # 定义抽象方法：生成器，返回嵌入模型或聊天模型
        pass # 抽象类，只定义函数名


class ChatModelFactory(BaseModelFactory): # 聊天模型工厂类，继承BaseModelFactory
    def generator(self) -> Optional[Embeddings | BaseChatModel]: # 生成聊天模型
        return ChatTongyi(model=rag_conf["chat_model_name"])


class EmbeddingsFactory(BaseModelFactory): # 嵌入模型工厂类，继承BaseModelFactory
    def generator(self) -> Optional[Embeddings | BaseChatModel]: # 生成嵌入模型
        return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])


chat_model = ChatModelFactory().generator() # 创建聊天模型实例
embed_model = EmbeddingsFactory().generator() # 创建嵌入模型实例
