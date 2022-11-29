FROM python:3.10
#FROM python:3.11

RUN apt-get update && apt-get install -y pv

RUN pip install numpy numba
#RUN pip install numpy

WORKDIR app
COPY ultrafb.py ultrafb.py
#COPY launch_and_run.sh launch_and_run.sh

#CMD ["bash", "launch_and_run.sh"]
CMD ["python", "ultrafb.py"]