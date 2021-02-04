FROM python:3
EXPOSE 8000

RUN git clone https://github.com/dansobolev/NapoleonIT_project.git
RUN pip install --no-cache-dir -r /NapoleonIT_project/requirements.txt