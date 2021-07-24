FROM python:3.9
ADD main_code.py templates data.csv .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "./main_code.py"]