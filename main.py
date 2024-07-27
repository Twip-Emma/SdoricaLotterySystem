'''
Author: tanyongqiang 1157529280@qq.com
Date: 2024-07-27 23:04:05
LastEditors: tanyongqiang 1157529280@qq.com
LastEditTime: 2024-07-28 00:55:52
FilePath: \078万象抽卡3\web.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fastapi import FastAPI, Query
from payload import get_drow, user_ill

app = FastAPI()

@app.get("/getDraw")
async def generate_image(userId: str = Query(..., min_length=1, max_length=30, regex="^[0-9]+$", description="用户QQ号")):
    try:
        image_path = await get_drow.drow(userId)
        return {"code": 200, "data": image_path, "message": "抽卡成功"}
    except Exception as e:
        return {"code": 500, "data": None, "message": str(e)}
    
# 用户的图鉴
@app.get("/getUserIll")
async def get_user_ill(userId: str = Query(..., min_length=1, max_length=30, regex="^[0-9]+$", description="用户QQ号")):
    try:
        image_path = await user_ill.get_user_ill(userId)
        return {"code": 200, "data": image_path, "message": "获取成功"}
    except Exception as e:
        return {"code": 500, "data": None, "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
