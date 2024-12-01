FROM python:3.12-slim
RUN apt-get update && apt-get install -y dos2unix
WORKDIR /opt/palavra/
COPY . .
RUN dos2unix /opt/palavra/entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /opt/palavra/entrypoint.sh
EXPOSE 5200
ENTRYPOINT [ "/opt/palavra/entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "--noreload", "0.0.0.0:5200"]
