FROM python:3.13.2

WORKDIR /fav_filmes

COPY . /fav_filmes/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000


CMD ["gunicorn", "-b", "0.0.0.0:8000", "meu_projeto.wsgi:application"]