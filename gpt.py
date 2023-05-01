import openai

class Chat:
    def __init__(self,api_key,system_setting = None,language = "中文",model="gpt-3.5-turbo") -> None:        

        # Apply the API key
        openai.api_key = api_key

        # 初始化对话列表，加入一个key为system的字典，有助于形成更加个性化的回答
        self.system_setting_list = [{'role':'system','content': f"以下的所有问题请用{language}回答"}]
        if system_setting:
            self.system_setting_list.append({'role':'system','content': system_setting})
            #添加系统设置
        self.conversation_list = []
        #对话记录
        self.model = model
    
    # 打印对话
    def show_conversation(self):
        for msg in self.conversation_list:
            if msg['role'] == 'user':
                print(f"\U0001F60E: {msg['content']}\n")
            elif msg['role'] == 'assistant':
                print(f"\U0001f47D: {msg['content']}\n")
            else:
                print(f"\U0001f47c: {msg['content']}\n")
    
    #清空历史会话
    def clear_conversation(self):
        del self.conversation_list
        self.conversation_list = []
        
    def generate_prompt(prompt,ask_type):
        """
        ask_type:问题类型
        """
        #这部分函数有待更新
        pass
    
    def get_answer(self,messages):
        response = openai.ChatCompletion.create(model=self.model,messages=messages)
        answer = response.choices[0].message['content']
        return answer
    
    # 提示chatgpt
    def ask(self,prompt,use_history = False,history_number = 5):
        self.conversation_list.append({"role":"user","content":prompt})
        if use_history:
            #基于历史history_number条提问记录和当前问题进行回答,虽然会结合上下文，但是会比较耗token
            response = self.get_answer(messages=self.system_setting_list+self.conversation_list[-history_number:])
        else:
            #只基于当前问题进行回答
            response = self.get_answer(messages=self.system_setting_list+[{'role': 'user', 'content': prompt}])
        # 下面这一步是把chatGPT的回答也添加到对话列表中，这样下一次问问题的时候就能形成上下文了
        self.conversation_list.append({"role":"assistant","content":response})
        return response
