'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-11-10 10:21:50
LastEditors: tanyongqiang 1157529280@qq.com
LastEditTime: 2024-07-29 11:30:53
'''
from payload import get_drow, user_ill

import asyncio
loop = asyncio.get_event_loop()


# 用户进行十连
print(loop.run_until_complete(get_drow.drow("123")))

# 用户的图鉴
# print(loop.run_until_complete(user_ill.get_user_ill("123")))

# 查看完整图鉴
# print(loop.run_until_complete(user_ill.get_pool_ill()))