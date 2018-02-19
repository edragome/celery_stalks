from celery import Celery

import requests

URLS = {
    "headers": "http://headers.jsontest.com/",
    "time": "http://time.jsontest.com/",
}

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def requestor(obj):
    if "term" not in obj:
        pass
    term = obj["term"]
    if term not in URLS:
        pass
    response = requests.get(URLS[term])
    if response.status_code != 200:
        pass
    else:
        print(response.content)

if __name__ == "__main__":
    requestor({"term": "time"})
