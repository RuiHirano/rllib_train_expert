FROM rayproject/ray:1.10.0-py39-gpu

RUN pip install tensorflow

CMD [ "bash" ]