<!--
 * @Author: 七画一只妖 1157529280@qq.com
 * @Date: 2023-11-10 21:42:48
 * @LastEditors: tanyongqiang 1157529280@qq.com
 * @LastEditTime: 2025-03-08 18:26:03
 * @FilePath: \078万象抽卡3\README.MD
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 万象物语抽卡模拟SdoricaLotterySystem

### 使用方式
- 1.自己运行main函数里面的两段代码即可，输出结果在payload/cache里面
- 2.参数就一个字符串，用于当作用户的唯一标识


### 已实现功能
#### 1.抽卡
> 进行一次十连抽卡，返回十连抽卡结果图的base64字符串

接口: `http://127.0.0.1:8000/getDraw?userId={user_id:str}`
参数：user_id：用户ID，不超过30位的纯数字字符串
响应：
~~~json
{
    "code": 200,
    "data": "图片的base64字符串",
    "message": "抽卡成功"
}
~~~

#### 2.查看图鉴（查看某位用户的box）
> 查看用户图鉴，返回已解锁和未解锁的角色列表（魂册），且阶数根据抽到的碎片数量进行自动升阶

接口: `http://127.0.0.1:8000/getUserIll?userId={user_id:str}`
参数：user_id：用户ID，不超过30位的纯数字字符串
响应：
~~~json
{
    "code": 200,
    "data": "图片的base64字符串",
    "message": "抽卡成功"
}
~~~

#### 3.查看用户练度（每个角色以250碎片为满练度）
> 查看用户图鉴，返回已解锁和未解锁的角色列表（魂册），且阶数根据抽到的碎片数量进行自动升阶

接口: `http://127.0.0.1:8000/getUserTrain?userId={user_id:str}`
参数：user_id：用户ID，不超过30位的纯数字字符串
响应（括号内文字记得删除/文字仅用作字段说明）：
~~~json
{
    "code": 200,
    "data": {
        "pool_total（卡池角色数量）": 198,
        "user_collect（图鉴收集程度/如果要显示百分比需要*100）": 0.16162,
        "user_train（用户练度/如果要显示百分比需要*100）": 0.0063
    },
    "message": "获取成功"
}
~~~

#### 4.查看所有用户练度排行
> 查看用户图鉴，返回已解锁和未解锁的角色列表（魂册），且阶数根据抽到的碎片数量进行自动升阶

接口: `http://127.0.0.1:8000/getAllRank`
参数：无
响应（括号内文字记得删除/文字仅用作字段说明）：
~~~json
{
    "code": 200,
    "data": [
        {
            "user_id（用户QQ号）": "114514",
            "user_total（用户碎片量/限制了250）": 312,
            "user_train（用户练度/如果要显示百分比需要*100）": 0.0063
        }
    ],
    "message": "获取成功"
}
~~~




### 使用
- 1.本地运行代码
- 2.服务器容器化部署（直接下载提供的镜像文件）
- 3.服务器容器化部署（自行打包成镜像）
注意：后两种方式需要你的服务器中有Docker环境

#### 1.本地运行代码
运行项目根目录下`main.py`即可，如果不想启动服务也可以运行`main-test.py`进行单个接口的测试

#### 2.服务器容器化部署
将下载好的镜像文件`sdorica-service.tar`放入服务器中执行，导入此镜像文件
~~~sh
docker load --input sdorica-service.tar
~~~
随后，执行以下命令将镜像启动为一个容器
~~~sh
docker run -d -p 8000:8000 --name sdorica-service sdorica-service
~~~
最后确保你的服务器防火墙或安全组开放了8000端口，然后就可以请求此服务了

#### 3.服务器容器化部署（自行打包成镜像）
进入项目的根目录，执行以下命令将该项目打包成一个镜像
~~~sh
docker build -t sdorica-service .
~~~
随后，执行以下命令将镜像启动为一个容器
~~~sh
docker run -d -p 8000:8000 --name sdorica-service sdorica-service
~~~
最后确保你的服务器防火墙或安全组开放了8000端口，然后就可以请求此服务了


# 扩展
>- 由于该抽卡系统是动态加载机制，所以你可以自己制作类似的图片直接放进payload/char里面即可，如果想新增一类角色，直接新增对应文件夹然后放入角色即可，没有需要修改配置文件的地方
>- 注意图片比例需要和现有图片保持一致