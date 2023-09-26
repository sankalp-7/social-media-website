FROM python:3.10
ENV PYTHONUNBUFFERED=1

RUN pip3 install mysqlclient


WORKDIR /djinsta

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

RUN pip3 install gunicorn

COPY . .

CMD ["python", "manage.py", "migrate"] && ["gunicorn", "social_media_app.wsgi:application", "-c", "gunicorn_config.py"]