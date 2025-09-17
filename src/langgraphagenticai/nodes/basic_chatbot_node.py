from src.langgraphagenticai.state.state import State

class BasicChatbotNode():
    """
    Basic Chatbot START -> CHATBOT -> END
    """
    def __init__(self,model):
        self.llm=model

    def process(self, state:State)-> dict:
        print("invoke")
        msg= self.llm.invoke(state['messages'])
        print(f'msg: {msg}')
        return  {"messages":msg}