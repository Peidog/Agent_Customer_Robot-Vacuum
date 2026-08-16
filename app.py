"""
pip install streamlit
streamlit run app.py

我想购买机器人，可以简单给我介绍一下吗
在我城市当前的天气下，机器人该如何保养
帮我生成我的使用报告
"""

import streamlit as st
from agent.react_agent import ReactAgent
import time


# 标题
st.title("扫地机器人智能客服")
# 分隔符
st.divider()

# streamlit需要session_state保存实例 
if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()

# 历史记录保存
if "message" not in st.session_state:
    st.session_state["message"] = []

# 页面输出历史记录
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 用户输入提示词
prompt = st.chat_input()


if prompt:
    # 页面输出用户的提示词
    st.chat_message("user").write(prompt)
    # 记录用户的提问
    st.session_state["message"].append({"role": "user", "content": prompt}) 

    with st.spinner("智能客服思考中..."):
        # 获取迭代器对象
        res_stream = st.session_state["agent"].execute_stream(prompt)

        # 缓存回答
        response_messages = []

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                # yield chunk

                for char in chunk:
                    time.sleep(0.01)
                    yield char

        # 流式输出
        st.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        # 记录Agent回答，去除思考过程
        st.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
        st.rerun()




