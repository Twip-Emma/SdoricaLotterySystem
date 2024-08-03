<!--
 * @Author: 七画一只妖 1157529280@qq.com
 * @Date: 2023-11-10 21:42:48
 * @LastEditors: tanyongqiang 1157529280@qq.com
 * @LastEditTime: 2024-08-03 23:38:11
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