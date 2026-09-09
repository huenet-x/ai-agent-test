from langchain.agents import create_agent

from dotenv import load_dotenv
from pathlib import Path

# 从项目根目录的 .env 加载环境变量（与当前工作目录无关）
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

def get_weather(city: str) -> str:
    """Get weather for a given city"""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[get_weather]
)

# for event in agent.stream(
#     {
#         "messages": [
#             { "role": "user", "content": "What's the weather in San Francisco?" }
#         ]
#     },
#     stream_mode="values" # 返回值为字典的值
# ):
#     messages = event["messages"]
#     print(f"历史消息：{len(messages)}条")
#     # for message in messages:
#     #     message.pretty_print()
    
#     messages[-1].pretty_print()

for chunk in agent.stream(
    {
        "messages": [
            { "role": "user", "content": "What's the weather in San Francisco?" }
        ]
    },
    stream_mode="messages" # 返回值为字典的值
):
    # print(chunk)
    # # 输出结果如下：
    # # (AIMessageChunk(
    # #   content="'ll", 
    # #   additional_kwargs={}, 
    # #   response_metadata={'model_provider': 'deepseek'}, 
    # #   id='lc_run--01a085bb-f6dd-7be3-aed8-7fa0841323d0', 
    # #   tool_calls=[], 
    # #   invalid_tool_calls=[], 
    # #   tool_call_chunks=[]
    # # ), 
    # # {'ls_integration': 'langchain_chat_model', 
    # #   'langgraph_step': 1, 
    # #   'langgraph_node': 'model', 
    # #   'langgraph_triggers': ('branch:to:model',), 
    # #   'langgraph_path': ('__pregel_pull', 'model'), 
    # #   'langgraph_checkpoint_ns': 'model:358b9c29-6bdb-d19e-1b09-23ffe67fdbb4', 
    # #   'checkpoint_ns': 'model:358b9c29-6bdb-d19e-1b09-23ffe67fdbb4', 
    # #   'ls_provider': 'deepseek', 
    # #   'ls_model_name': 'deepseek-chat', 
    # #   'ls_model_type': 'chat', 'ls_temperature': None}
    # # )

    print(chunk[0].content, end='')
