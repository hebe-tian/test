# test

## chapter.1  
hash:46cff55ce77f43423e703798a4d0b63c5d4d33e6  
最基本的访问PythonAnyWhere，然后切换到各个子页面，并且来验证是否正确访问到了  
pytest中的断言比unittest更符合coder的理解，例如：`assert A == B`,`assert A in B`  
pytest和unittest不同，不一定要在testClass中，case直接放在代码中也可以  
ps. 在使用之前需要先安装selenium（pip install selenium）,pytest(pip install pytest),还需要安装对应浏览器的驱动并且添加到环境变量中  
下一步：把共有的步骤抽取出来，放到setUp方法和tearDown方法中  
setUp，tearDown：在每次执行test方法前后会执行一遍setUp、tearDown  
> chapter1.tips:  
>使用浏览器驱动时无需最新的驱动也能正常使用浏览器的大部分功能，无需实时更新浏览器驱动  

## chapter.2  
hash:83dfa1dcdb2e27474cd512fac539470068613d5c  
setup,teardown  
pytest中的setup函数分为多种  
* setup/setup_method 在test类中，每执行一个类中的case就执行一次  
* setup_class 在test类中，执行类的时候会执行一次  
* setup_function 不在test类中，每执行一个case就会执行一次  
* setup_module 不在test类中，执行类的时候会执行一次  
  
把打开浏览器并访问网址的操作写到setup函数中，把退出浏览器的操作写进teardown函数中，这样就不需要在每个testcase中写大量的重复操作，在case里的代码主要集中在操作-断言  
setup，teardown以及case里面的driver要加self，driver是在setup-case-teardown中共用的  
下一步：把变量抽取出来，不直接放在Class中（暂时还是放在py文件中，后续优化可以放在配置文件或者其他地方）
>chapter2.tips：  
>使用浏览器时可能会出现上一次测试产生的数据干扰了这一次的测试，这个时候我们可以使用浏览器的无痕模式  
>```python3
>options = webdriver.ChromeOptions()
>options.add_argument('--incognito')
>self.driver = webdriver.Chrome(chrome_options=options)
>```

## chapter.3  
hash:6a8c1b7288b2b4361afa40ff625d699c4688b2c6  
这一次的commit里，把代码中的url，xpath都抽出来存放在json文件里，然后在代码中读取json文件里的内容，赋值给url和xpath  
下一步：优化测试报告

## chapter.4  
hash:4ca033e0c4b6790c2cb2b9e426a574516c28e109  
使用pytest执行后输出的测试报告展示在命令行，用.来表示成功，E和Fail代表了失败  
使用pytest-html库可以输出html形式的测试报告  
下一步：添加测试类-登录登出

## charter.5  
hash:  
添加了登录和登出的测试类
