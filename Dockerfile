FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["/bin/bash", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

# CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["alembic", "upgrade", "head", "&&", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]