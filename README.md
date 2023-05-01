# GPT
Python calls GPT code
# 配置过程
在进行配置之前，需要先完成以下几个步骤
 1. 注册一个Kaggle账号并登录
 2. 注册一个ChatGPT账号，并申请api_key（教程自寻）

在完成以上步骤之后，进入kaggle主界面，create-new notebook 新建一个笔记本
![在这里插入图片描述](https://img-blog.csdnimg.cn/d520a2cc888543c897c9368009b7d783.png)
创建之后，在第一个单元格输入以下代码，安装openai的包（速度很快，5s左右安装完成）
```python
!pip install openai
```
安装完成
![在这里插入图片描述](https://img-blog.csdnimg.cn/54c39e81742042b480982e39f47f2e98.png)
安装之后，在notebook右侧找到上传(upload),上传方式选择Github
![在这里插入图片描述](https://img-blog.csdnimg.cn/b4e8d9832a2d470ca12bb422dc683422.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/a460dbcfe08c4a7fb21497f23982c609.png)
链接如下
`
https://github.com/Kiligmzq6/GPT/blob/37ec7d441a94eeecb90b3fbff76ffc823ce7050d/gpt.py#enroll-beta
`

安装成功后，右侧Data部分显示如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/b101f297783d4e37a553fee36538afb4.png)
之后，在单元格中输入

```python
import openai
import sys
sys.path.insert(1, '/kaggle/input/gpt-code/') 
#添加此语句，告知系统gpt.py在哪个路径中
from gpt import Chat
```
接下来即可调用了

```python
key = "sk-你自己的api_key" 
c1 = Chat(api_key = key)
#创建chat实例
```
调用实例
![在这里插入图片描述](https://img-blog.csdnimg.cn/5f77c19fc9c1494ba87d8b31c67d9e70.png)
运行生成的代码：

```python
import matplotlib.pyplot as plt

# 数据
x = ["apple", "banana", "orange", "kiwi"]
y1 = [20, 35, 25, 30]
y2 = [15, 25, 20, 28]

# 配置
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = [8, 6]

fig, ax = plt.subplots()

# 绘制柱状图
ax.bar(x, y1, color="#ff9933", label="Production", width=0.35)
ax.bar(x, y2, bottom=y1, color="#66cccc", label="Sales", width=0.35)

# 添加标题和坐标轴标签
ax.set_xlabel("Fruit")
ax.set_ylabel("Quantity")
ax.set_title("Fruit Production and Sales")

# 添加图例
ax.legend()

# 显示图形
plt.show()
```
可以正常运行
![在这里插入图片描述](https://img-blog.csdnimg.cn/7e8cabe34dd4474c94f8e37a8a5cb941.png)
# 方法描述

```python
show_conversation()
```
显示历史对话记录
![在这里插入图片描述](https://img-blog.csdnimg.cn/5ed7e010dd6d425fa463dd832a6c6902.png)

```python
ask(self,prompt,use_history = False,history_number = 5)
```
prompt: 提问的问题
use_history:表示是否使用历史问答记录（虽然会结合上下文，但是会比较耗token）
history_number:使用历史几条问答记录
更多功能有待后续完善。

[Github链接](https://github.com/Kiligmzq6/GPT)
