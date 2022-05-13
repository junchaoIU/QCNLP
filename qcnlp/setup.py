from setuptools import setup, find_packages            #这个包没有的可以pip一下


setup(name='qcnlp',
      version='0.0.1',
      keywords = ["pip", "nlp"],			# 关键字
      description='A Preprocessing & Parsing tool for Chinese Natural Language Processing',
      author='wujunchao',
      url = "https://github.com/junchaoIU/QCNLP",
      author_email='wujunchaoIU@outlook.com',
      requires= ['numpy'], # 定义依赖哪些模块
      packages = find_packages(),  # 系统自动从当前目录开始找包
      # 如果有的文件不用打包，则只能指定需要打包的文件
      #packages=['代码1','代码2','__init__']  #指定目录中需要打包的py文件，注意不要.py后缀
      license="apache 2.0"
      )

