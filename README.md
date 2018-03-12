# FakeV2EX
Django 2.0 写的仿V2EX社区  纯技术交流 联系方式: QQ 435968679

## Demo地址
[http://fv2ex.izhihu.me](http://fv2ex.izhihu.me)
* 仅供测试。。求大佬别DDos

## 完成功能
* Topic 展示
* 登录，注册，退出
* Tab 展示，Node 信息展示，node 背景色，图标 根据node节点过滤Topic
* 最热，点击量最多的
* member 用户信息查看
* 查看所有 需登录后才能查看
* 分页展示
* 新建Topic Markdown 格式，支持预览
* 支持直接从node 页面新建，自动选择此节点创建Topic
* 我关注的用户数量及用户的信息，帖子展示
* 我关注的节点 数量，所属节点Topic数量
* 我关注的Topic
* 我顶了那个Topic，踩了哪个Topic
* Topic的总点击量 总的顶的数量， 总的踩的数量
* 收藏Topic
* 感谢Topic的作者
* 当前用户的IP显示
* 统计在线用户
* 检测当前用户是否在线
* 评论

## 用户统计功能
* 使用了redis 缓存
* 使用自定义中间件 当用户浏览页面时，把session 加入缓存库中，通过统计缓存库的session 实现在线用户统计
* session 自动过期，如果用户不刷新或者不浏览新页面，session 自动过期，同缓存里的key也自动过期
* 顺便在中间件中加入了获取当前用户ip的逻辑，可以在前端显示当前用户的真实IP地址

## 待完成
* 注册邮箱验证
* @我的或者回复我的实时消息
* 活跃度
* 用户详细信息及设置， 隐私、屏蔽、头像上传等。。。
* 用户财富值，每日领取 发帖，回帖 感谢等对应的财富值变化
* 当前页面加载时间 （目前想到的是用前端js实现）
* 记事本功能
* 用户草稿功能，写了一半没写完的保存到服务端
* ... 目前能想到的暂时就这些吧

## 如何部署
* install python3.6
* git clone https://github.com/lgphone/FakeV2EX
* cd FakeV2EX && pip install -r re.txt
* 修改数据库，Redis连接地址
* python manage.py makemigrations &&  python manage.py migrate
* python manage.py createsuperuser
* 测试直接 python manager.py runserver
* 正式请使用 uwsgi 部署
* 头部的Tab 以及二级导航 需要先在admin中录入数据

## 图片展示 --- old

* 主页
![主页](doc/pic/index.png)

* 登录
![登录](doc/pic/signin.png)

* 注册
![注册](doc/pic/signup.png)

* 退出
![退出](doc/pic/signout.png)

* Tab
![Tab](doc/pic/tab.png)

* Topic
![Topic](doc/pic/topic.png)

* Node
![Node](doc/pic/node.png)

* Member
![Member](doc/pic/member.png)

* Hot
![Hot](doc/pic/hot.png)

* New
![New](doc/pic/new.png)

* New from Node
![New from Node](doc/pic/new_from_node.png)

* 预览
![预览](doc/pic/private.png)

* Recent
![Recent](doc/pic/recent_p.png)

* 登录后主页
![登录后主页](doc/pic/login_index.png)

* 登录后Node
![登录后Node](doc/pic/login_node_p.png)

* 登录后Member
![登录后Member](doc/pic/login_member.png)

* 登录后Topic
![登录后Topic](doc/pic/login_topic.png)

* 我关注的用户
![我关注的用户](doc/pic/my_following.png)

* 我关注的Node
![我关注的Node](doc/pic/my_nodes.png)

* 我关注的Topic
![我关注的Topic](doc/pic/my_topics.png)
