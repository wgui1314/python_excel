# 从 hub.docker.com 上 pull 最新 python image
FROM python
RUN  pip install fastapi && pip install "uvicorn[standard]" && pip install oss2 && pip install openpyxl
# 容器内的工作目录
WORKDIR /excel-python

# copy 源代码到容器
COPY . /excel-python


CMD ["uvicorn main:app --reload"]
