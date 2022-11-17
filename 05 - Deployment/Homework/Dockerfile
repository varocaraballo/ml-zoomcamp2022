FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "question4.py", "./"]

RUN pipenv install --system --deploy

EXPOSE 8496

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8496", "question4:app"]