from distutils.core import setup

setup(
    name='GptCode',  # 对外模块的名字
    version='1.0.2',  # 版本号
    description='测试本地发布模块',  # 描述
    requires=['openai'], # 定义依赖哪些模块
    author='mazhiqiang',  # 作者
    author_email='mazhiqiang2023@163.com',
    py_modules=['GptCode.gpt'],  # 要发布的模块
)
