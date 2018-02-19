import os

BROKER_URL = 'sqs://{}:{}@alpinesqs:9324'.format(
    os.environ.get("AWS_ACCESS_KEY_ID"),
    os.environ.get("AWS_SECRET_ACCESS_KEY"))

# BROKER_TRANSPORT = 'sqs'
# broker_transport = 'sqs'
# broker_transport_options = {
# #BROKER_TRANSPORT_OPTIONS = {
#     'region': 'us-east-1',
# }
# CELERY_RESULT_SERIALIZER = 'pickle'


#BROKER_TRANSPORT = 'sqs'
BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-east-1',
}
CELERY_RESULT_SERIALIZER = 'json'
#
CELERY_ROUTES = {
    'tasks.requestor': {
        'queue': 'requesting',
#        'routing_key': 'compute.a_result'
    },
}


#CELERY_TASK_ROUTES = {
#    'tasks.add': {
#        'queue': 'addes',
#        'routing_key': 'compute.a_result#'
#    },
#}

