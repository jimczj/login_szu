这是一个给深圳大学提供登录功能的模块
如果你是python开发者，且用django开发web，该模块也行能给你提供到一点帮助

如果你想实现一下深圳大学的校园卡认证登录功能，可以考虑使用我的代码
![这里写图片描述](http://img.blog.csdn.net/20160413011743689)

该模块依赖django，lxml，requests，当你安装该模块时，这些会被自动安装，如果本来就有安装，不会覆盖你原有的版本

安装
--

```
pip install login_szu
```

使用
--
在你django app 的views.py里面这样使用

```
from login_szu.decorator import login_szu

@login_szu(return_url="http://xx.xx.xxx.cn/")
def index(request):
    return render(request, 'index.html')
```
只需要导入装饰器login_szu，在需要登录的函数@login_szu
就能实现登录跳转，return_url参数是必填的，表示你登录后跳转的url，之后你的view函数正常写就好，不会受到其他影响

登录成功后，你的request里面会自动多了两个session的值，在你写的view函数中，这样获取

```
request.session['stu_no']#学号比如2014150122
request.session['stu_ic']#卡号比如130254
#你也可以这样获取
request.session.get('stu_no')
request.session.get('stu_ic')
```

团队
--

 - 码农：阿集 
 - 项目发起人：不兄 
 - 指导者：钟浩贤
