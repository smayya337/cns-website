FROM python:3.13

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python ./manage.py migrate
RUN yes yes | python ./manage.py collectstatic

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "acm_website.wsgi" ]
