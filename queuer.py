from tasks import requestor

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='A simple celery sqs queuer')
    parser.add_argument("term", choices=["time", "headers"],
        help='a term to pass to queue')
    args = parser.parse_args()
    requestor.delay({"term": args.term})

