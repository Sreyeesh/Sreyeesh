FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir markdown

CMD ["python", "export_html.py"]
