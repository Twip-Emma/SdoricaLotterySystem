'''
Author: 七画一只妖 1157529280@qq.com
Date: 2023-11-10 11:40:23
LastEditors: tanyongqiang 1157529280@qq.com
LastEditTime: 2025-03-08 17:43:54
'''
import uuid
import datetime

from .db import sql_dql, sql_dml

# 初始化背包表
async def init():
    await sql_dml('''
        CREATE TABLE IF NOT EXISTS user_pkg (
            id TEXT PRIMARY KEY,
            drow_id TEXT,
            drow_time TEXT,
            char_name TEXT,
            char_count INT,
            char_rank TEXT,
            user_id TEXT
        )
    ''')


# 查询一个用户的背包并根据char_name去重
async def get_pkg(user_id: str) -> list:
    user_pkg = await sql_dql('''
        SELECT char_name, char_rank, SUM(char_count) as total_count
        FROM user_pkg
        WHERE user_id = ?
        GROUP BY char_name;
    ''', (user_id,))
    print(user_pkg)
    return sorted(user_pkg, key=lambda x: x[1], reverse=True)


# 往背包新增一条数据
async def add_pkg(user_id: str, char_name: str, char_rank: str) -> bool:
    await init()
    char_count = 0
    if char_rank == "0阶角色":
        char_count = 1
    elif char_rank == "1阶角色":
        char_count = 5
    elif char_rank == "2阶角色":
        char_count = 20
    else:
        char_count = 50

    await sql_dml(
        '''
            INSERT INTO user_pkg (id, drow_id, drow_time, char_name, char_count, char_rank, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (str(uuid.uuid1()),
        str(uuid.uuid1()),
        datetime.datetime.now().strftime("%Y-%m-%d"),
        char_name,
        char_count,
        char_rank,
        user_id)
    )


# 获取用户背包总数
async def get_user_pkg_total(user_id: str) -> int:
    user_total = await sql_dql('''
        SELECT user_id, SUM( char_count ) AS total_count FROM user_pkg 
        WHERE user_id = ? 
    ''', (user_id,))
    if user_total[0][0] is None:
        return 0
    return user_total[0][1]


# 获取用户背包角色种类数
async def get_user_pkg_type_count(user_id: str) -> int:
    type_total = await sql_dql('''
        SELECT count(*) from (SELECT
            char_name,
            char_rank,
            SUM( char_count ) AS total_count 
        FROM
            user_pkg 
        WHERE
            user_id = ?
        GROUP BY
            char_name) t
    ''', (user_id,))
    return type_total[0][0]

# 获取用户背包每个角色数量，数量大于250只返回250
async def get_user_roles_by_limit(user_id:str) -> list:
    user_pkg = await sql_dql('''
    SELECT
	char_name,
    CASE
		WHEN SUM( char_count ) > 250 THEN
		250 ELSE SUM( char_count ) END AS total_count 
	FROM
		user_pkg 
	WHERE
		user_id = ?
	GROUP BY
		char_name
    ''', (user_id,))
    return user_pkg


# 获取所有用户练度排名
async def get_all_rank_by_limit() -> list:
    return await sql_dql('''
    SELECT user_id, sum(t.total_count) AS user_total FROM (SELECT
	user_id, char_name,
    CASE
		WHEN SUM( char_count ) > 250 THEN
		250 ELSE SUM( char_count ) END AS total_count 
	FROM
		user_pkg 
	GROUP BY
		user_id, char_name) t GROUP BY user_id ORDER BY user_total DESC
    ''')