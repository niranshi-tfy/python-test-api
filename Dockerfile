# ==== BACKEND ====
FROM --platform=linux/amd64 python:3.9-slim

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY / ./

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]
