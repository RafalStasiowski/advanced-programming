FROM python:3.7

#WORKDIR /opt/app

#COPY app .
COPY ./app /app

RUN pip install --no-cache-dir -r app/requirements.txt

#EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]