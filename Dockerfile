FROM python:3.8

WORKDIR /coding_challenge

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV TZ=America/Lima
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezoneCOPY . .

COPY ./wiki_insight ./wiki_insight
COPY ./docs ./docs



CMD ["python", "-m", "wiki_insight" ]