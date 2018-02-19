# celery_stalks
Exploring celery running against a dockerize version of sqs (alpine sqs) using docker containers

## getting started

### docker

```
docker-compose up
```
### connecting to the container
```
docker exec -it celerystalks_apps_1
```

### queuing tasks
```
/code# python queuer.py 
usage: queuer.py [-h] {time,headers}
queuer.py: error: the following arguments are required: term
/code# python queuer.py headers
/code# python queuer.py time
```

### celery worker
The celery worker will start automatically from docker-compose with
the `command` configuration in the yaml file.

The command line can be removed from the yaml file and the
line
```
/code# celery -A tasks -Q requesting worker --loglevel=info
```
Can be run in another shell connection to the container

With a populated queue the output will look something like
```
[2018-02-19 03:01:14,044: INFO/MainProcess] Starting new HTTP connection (1): alpinesqs
[2018-02-19 03:01:14,086: INFO/MainProcess] Connected to sqs://ABC:**@alpinesqs:9324//
[2018-02-19 03:01:14,137: INFO/MainProcess] Starting new HTTP connection (1): alpinesqs
[2018-02-19 03:01:14,196: INFO/MainProcess] celery@2fdd752834f7 ready.
[2018-02-19 03:01:16,322: INFO/MainProcess] Received task: tasks.requestor[207cf100-8f01-40c5-acbf-189376d4c767]  
[2018-02-19 03:01:16,637: WARNING/ForkPoolWorker-2] b'{\n   "time": "03:01:13 AM",\n   "milliseconds_since_epoch": 1519009273604,\n   "date": "02-19-2018"\n}\n'
[2018-02-19 03:01:16,640: INFO/ForkPoolWorker-2] Task tasks.requestor[207cf100-8f01-40c5-acbf-189376d4c767] succeeded in 0.29695744698983617s: None
[2018-02-19 03:03:19,662: INFO/MainProcess] Received task: tasks.requestor[4bb0e804-31d0-42e8-baaf-12fa06fdc338]  
[2018-02-19 03:03:19,887: WARNING/ForkPoolWorker-2] b'{\n   "X-Cloud-Trace-Context": "24dd785021d804a3647a4292c9e6906a/10043715951725353939",\n   "Host": "headers.jsontest.com",\n   "User-Agent": "python-requests/2.18.4",\n   "Accept": "*/*"\n}\n'
```

## aws commands

### list queues
```
aws --endpoint-url http://alpinesqs:9324 sqs list-queues --region us-east-1
```

### get the queue attributes and number of items in queue
```
aws sqs get-queue-attributes --endpoint-url http://alpinesqs:9324 --queue-url http://alpinesqs:9324/queue/addes --attribute-names All --region us-east-1
```

### delete queue
```
aws --endpoint-url http://alpinesqs:9324 sqs delete-queue --queue-url http://alpinesqs:9324/queue/celery --region us-east-1
```

