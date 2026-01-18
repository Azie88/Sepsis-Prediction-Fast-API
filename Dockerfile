FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 800

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800"]