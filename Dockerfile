FROM python:3.12
RUN apt-get update && apt-get install -y dos2unix
WORKDIR /opt/palavra/
COPY . .
RUN dos2unix /opt/palavra/entrypoint.sh
RUN pip install --no-cache-dir django coverage termcolor unidecode python-decouple dj-database-url psycopg2-binary Pillow
RUN chmod +x /opt/palavra/entrypoint.sh
EXPOSE 5200
ENTRYPOINT [ "/opt/palavra/entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "--noreload", "0.0.0.0:5200"]