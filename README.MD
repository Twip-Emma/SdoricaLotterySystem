<!--
 * @Author: 七画一只妖 1157529280@qq.com
 * @Date: 2023-11-10 21:42:48
 * @LastEditors: 七画一只妖 1157529280@qq.com
 * @LastEditTime: 2023-11-10 21:48:08
 * @FilePath: \078万象抽卡3\README.MD
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 万象物语抽卡模拟

### 使用方式
- 1.自己运行main函数里面的两段代码即可，输出结果在payload/cache里面
- 2.参数就一个字符串，用于当作用户的唯一标识


### 已实现功能
>- 万象十连
>- 万象图鉴
>- 每日抽卡限制5次，你可以自行修改get_drow.py内的全局变量PULL_NUM以修改抽卡次数限制


# 扩展
>- 由于该抽卡系统是动态加载机制，所以你可以自己制作类似的图片直接放进payload/char里面即可，如果想新增一类角色，直接新增对应文件夹然后放入角色即可，没有需要修改配置文件的地方