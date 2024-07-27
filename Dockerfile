# 使用官方Python基础镜像
FROM python:3.9-alpine

# 设置工作目录
WORKDIR /app

# 复制项目的依赖文件到工作目录
COPY requirements.txt .

# 安装项目的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制整个项目到工作目录
COPY . .

# 设置环境变量
ENV PORT=8000

# 暴露服务端口
EXPOSE 8000

# 运行主程序
CMD ["python", "main.py"]
