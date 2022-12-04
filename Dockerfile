FROM python:3.7

COPY ./app /app

RUN pip install --no-cache-dir -r app/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]