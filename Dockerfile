FROM python:3.13-slim

WORKDIR /app

# install dependencies first so this layer is cached between code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the whole repo so /app/src, /app/templates and /app/static all exist
COPY . .

EXPOSE 5000

CMD ["python", "src/run.py"]
