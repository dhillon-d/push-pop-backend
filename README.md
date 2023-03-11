**Design**
This app is the backend in memory database accessible by REST API endpoint. There is also a companion frontend application. Both applications have to be running in order to work locally.

**Versions**
Recommended you use pyenv to get the appropriate versions

- python == 3.11
- pip == 22.3.1

**Run app locally**
`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`
`python main.py` or `uvicorn main:app --reload --port 5000`

**Run app in a docker container**
`docker build -t <image_name> .`
`docker run -dp <host_port>:5000 <image_name>`
