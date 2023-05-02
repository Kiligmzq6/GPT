# 安装
安装方法
```python
!pip install GptCode
```
适用于notebook中调用。如Jupyter NoteBook、Jupyter Lab、Kaggle、Colab等平台。（Kaggle使用不需要科学上网，其余平台需要）
# 代码示例

```python
import openai
from GptCode.gpt import Chat
#导入包
key = "sk-你自己的秘钥" 
c1 = Chat(api_key = key)
#设置秘钥并创建一个对话实例
```
## Chat

```python
ans = c1.ask("请用Python绘制一份饼图，配色设置好看一些，标签和图例使用英文")
print(ans)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2736a17512984fdca6fd216a3a1e63b7.png)
代码运行结果:
![在这里插入图片描述](https://img-blog.csdnimg.cn/c652fb344b544b78ba791e6654698d9d.png)



参数解释:

        :param prompt:问题描述
        :param reference: 是否列出参考的资料来源,默认为True
        :param use_history: 是否参考历史对话信息,默认为False
        :param history_number: 参考历史对话信息的条数,默认为5
        :return: 此次问题的回复
## 聊天记录

```python
c1.show_conversation()
#列出所有聊天记录
c1.clear_conversation()
#清楚聊天记录
```
## 图像生成

```python
c1.painting(prompt,image_size = 512,return_img = False)
"""
        :param prompt: 图像描述
        :param image_size: 图像大小 image_size*image_size
        :param return_img: 是否返回图像，若不返回则直接展示
        :return: 图像
"""
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/cfa64a723d14482f9d636155d4e800c1.png)
更多功能有待后续更新。

[GitHub链接](https://github.com/Kiligmzq6/GPT/blob/main/gpt.py)



