这是一个给深圳大学提供登录功能的模块
如果你是python开发者，且用django开发web，该模块也行能给你提供到一点帮助

如果你想实现一下深圳大学的校园卡认证登录功能，可以考虑使用我的代码
![这里写图片描述](http://img.blog.csdn.net/20160413011743689)

该模块依赖django，lxml，requests，当你安装该模块时，这些会被自动安装，如果本来就有安装，不会覆盖你原有的版本

申请认证网址权限
------
要实现深圳大学的校园卡登录认证，首先你要到深圳大学的网络中心 提交申请，具体申请流程忘了，如果有知道的同学或者有链接的同学，求发pull request过来

安装
--

```
pip install login_szu
```

使用
--
在django 的settings.py设置

```
LOGIN_SZU_SECURE_URL=False#或True
LOGIN_SZU_BUCKET_DOMAIN="www.baidu.cn"
```
LOGIN_SZU_SECURE_URL表示是http还是https
LOGIN_SZU_BUCKET_DOMAIN表示你的域名，需要去学校申请权限才可以登录


----------


在你django app 的views.py




里面这样使用

```
from login_szu.decorator import login_szu

@login_szu
def index(request):
    return render(request, 'index.html')
```
只需要导入装饰器login_szu，在需要登录的函数@login_szu
就能实现登录跳转，之后你的view函数正常写就好，不会受到其他影响

登录成功后，你的request里面会自动多了6个session的值，在你写的view函数中，这样获取

```
@login_szu
def index(request):
    print (request.session['szu_no'])#如2014150***
    print (request.session['szu_ic'])#130***
    print (request.session['szu_name'])#陈**
    print (request.session['szu_org_name'])#深圳大学/计算机与软件学院/计算机科学/01
    print (request.session['szu_sex'])#男
    print (request.session['szu_rank_name'])#01
    return render(request, 'index.html')
```

**szu_rank_name对照表**
> //szu_rank_name对照表
//ID	用户类别
//01	本科生
//02	研究生
//03	博士生
//04	留学生
//05	教工
//11	成教学生
//07	教工家属
//08	测试人员
//13	工作人员
//14	离退休教工
//21	博士后
//17	合作银行
//25	校内工作
//30	校外绿色通道
//24	校外人员
//20	外籍教师
//23	校友
//28	交换留学生
//12	自考生
//16	外联办学生
//26	校企人员
//29	消费卡贵宾

## 测试 ##

本地测试的时候因为要用到认证过的网站，在linux可以这样修改host

```
sudo vim /etc/hosts
```
然后在改文件中添加 

```
127.0.0.1  yoursite.com#比如www.baidu.com
```
退出保存，重启网络服务

```
service network restart
```
然后你就可以运行你的django项目了

```
python manage.py runservser www.baidu.com:80
#如果权限不够就执行
sudo su
```

团队
--
学子天地技术部
 - 码农：阿集 
 - 项目发起人：不兄 
 - 指导者：钟浩贤
github地址：https://github.com/jimczj/login_szu
