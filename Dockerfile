from python:3.8

RUN pip install click 

ADD main.py /

CMD [ "python", "main.py"]