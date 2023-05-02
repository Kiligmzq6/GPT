import openai
from PIL import Image
from io import BytesIO
import requests
from IPython.display import display

class Chat:
    def __init__(self, api_key, system_setting=None, language="中文", model="gpt-3.5-turbo") -> None:

        # Apply the API key
        openai.api_key = api_key

        # 初始化对话列表，加入一个key为system的字典，有助于形成更加个性化的回答
        self.system_setting_list = [{'role': 'system', 'content': f"以下的所有问题请用{language}回答"}]
        if system_setting:
            self.system_setting_list.append({'role': 'system', 'content': system_setting})
            # 添加系统设置
        self.conversation_list = []
        # 对话记录
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

    # 清空历史会话
    def clear_conversation(self):
        del self.conversation_list
        self.conversation_list = []

    def generate_prompt(self,prompt, ask_type=None):
        """
        ask_type:问题类型
        """
        # 这部分函数有待更新
        tail_message = "列出你所参考的资料来源,请你一步一步来,并仔细思考你的行为逻辑,核查你输出的信息。"
        prompt = prompt + tail_message
        return prompt

    def translate(self,prompt,aim_language = "英语"):
        """
        :param prompt: 原始语言
        :param aim_language: 要翻译成的语种
        :return: 翻译结果
        """
        trans = f"请把以下语言翻译为{aim_language}。"
        response = self.get_answer(messages=self.system_setting_list + [{'role': 'user', 'content': trans+prompt}])
        return response

    def extract_picture_prompt(self,prompt):
        extract = "以下句子描述了一张图片，请从中提取出对图片的描述，或者想象一下图片的描述，描述请尽量详细。"
        response = self.get_answer(messages=self.system_setting_list + [{'role': 'user', 'content': extract + prompt}])
        return response

    def get_answer(self, messages):
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        answer = response.choices[0].message['content']
        return answer

    def painting(self,prompt,image_size = 512,return_img = False):
        """
        :param prompt: 图像描述
        :param image_size: 图像大小 image_size*image_size
        :param return_img: 是否返回图像，若不返回则直接展示
        :return: 图像
        """
        prompt = self.extract_picture_prompt(prompt)
        prompt = self.translate(prompt)
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=str(image_size)+"x"+str(image_size)
        )
        url = response['data'][0]['url']
        # 获取图片链接的二进制数据
        response = requests.get(url)
        image_data = response.content

        # 将二进制数据转换成图片对象并展示
        image = Image.open(BytesIO(image_data))
        if return_img:
            return response['data'][0]['url']
        display(image)
    # 提示chatgpt
    def ask(self, prompt,reference=True, use_history=False, history_number=5):
        """
        :param prompt:问题描述
        :param reference: 是否列出参考的资料来源
        :param use_history: 是否参考历史对话信息
        :param history_number: 参考历史对话信息的条数
        :return: 此次问题的回复
        """
        if reference:
            prompt = self.generate_pxrompt(prompt)
        self.conversation_list.append({"role": "user", "content": prompt})
        if use_history:
            # 基于历史history_number条提问记录和当前问题进行回答,虽然会结合上下文，但是会比较耗token
            response = self.get_answer(messages=self.system_setting_list + self.conversation_list[-history_number:])
        else:
            # 只基于当前问题进行回答
            response = self.get_answer(messages=self.system_setting_list + [{'role': 'user', 'content': prompt}])
        # 下面这一步是把chatGPT的回答也添加到对话列表中，这样下一次问问题的时候就能形成上下文了
        self.conversation_list.append({"role": "assistant", "content": response})
        return response
