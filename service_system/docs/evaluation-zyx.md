# 模块名 evaluation
##1、 客户评价提交（修改）接口
#### 请求地址
'''
POST  /evaluation
'''
#### 请求参数
name  |type         |NN |comments
--------|-----------|-----|----------------------
record_id|string|   T  |通话有效记录的id
user_id(type=2) |string|T|客户id   uuid
user_name((type=2)|string|T|客户名字
user_id(type=1)|string|T|客服id    uuid
user_name(type=1)|string|T|客服名字
star_num|int|T|星的等级1-5的整数
word_eva|string|T|文字评价

#### 响应  
##### 201 
## 2、客户获取服务评价接口  
#### 请求地址
'''
GET  /evaluation
'''
#### 请求参数

name  |type         |NN |comments
--------|-----------|-----|-------------------
user_id(type=2) |string|T|客户id   uuid

#### 响应
##### 200

name  |type        |NN|comments
--------|-----------|---|----------------------
record_id|string|   T  |通话有效记录的id
user_id(type=2) |string|T|客户id   uuid
user_name((type=2)|string|T|客户名字
user_id(type=1)|string|T|客服id    uuid
user_name(type=1)|string|T|客服名字
eva_state|string|T|评价状态
star_num|int||星的等级1-5的整数
word_eva|string||文字评价
		
 
## 3、获取数据信息接口
#### 请求地址
'''
GET  /datadisplay
'''
#### 请求参数
name  |type         |NN |comments
--------|-----------|-----|----------------------
month|int            |   T  |值的范围在1-12

#### 响应
##### 200
name                 |type   |comments
-----------------|--- ----|----------------------
star_num         |string| json 里面有五个数据
assessed           |int     |json已评价的数据
not_appraised |int   |json未评价的数据
problem_type|int      |json问题种类


