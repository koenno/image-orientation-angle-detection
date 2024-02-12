FROM continuumio/miniconda3

WORKDIR /app

COPY . .

RUN conda create --name deep-image-orientation --file requirements.txt -y

SHELL ["conda", "run", "-n", "deep-image-orientation", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "deep-image-orientation", "python", "run.py"]
