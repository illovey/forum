# 一、实现功能

1、多用户、多角色（一个管理员、多个普通用户）

2、普通用户可以发布帖子、修改帖子、删除帖子

3、管理员可以拥有和普通用户一样的功能，并且还可以管理用户，例如删除用户

4、置顶帖子

5、管理员一直在线，普通用户可以实时和管理员进行聊天

6、普通用户注册功能（管理员默认存在）

7、下载帖子（把帖子存为txt文件，然后保存在本地）

# 二、API

## 注册

post /api/user/register

| 参数     | 类型   |
| -------- | ------ |
| username | string |
| password | string |

## 登录

/api/user/login

| 参数     | 类型   |
| -------- | ------ |
| username | string |
| password | string |

## 登出

/api/user/logout

| 参数 | 类型 |
| ---- | ---- |
| 无   | 无   |

# 三、数据库

## 库名

forum

## 表名

users(用户表)

| 字段     | 类型        |
| -------- | ----------- |
| username | varchar(50) |
| password | char(32)    |

posts(帖子表)

| 字段        | 类型        |
| ----------- | ----------- |
| id          | int         |
| title       | varchar(50) |
| content     | text        |
| create_time | int         |
| username     | varchar(50)         |
