FROM python:3 AS INSTALL
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3 AS BUILD
WORKDIR /usr/src/app
COPY --from=INSTALL /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages
COPY fib.py .

#Entrypoint permite que podamos especificar luego el parámetro para ese comando
ENTRYPOINT ["python", "fib.py"]

#Por defecto lo ejectua con -h
CMD ["-h"]