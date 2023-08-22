import requests
import json
import os


host = "https://rpc.simplyput.ai"

class SPApiError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def CreateQuestion(question: str) -> dict:
    create_endpoint = "/question.v1.QuestionService/CreateQuestion"
    payload = {
        "orgId": os.getenv('ORG_ID'),
        "question": question
    }
    headers = {
        "accept-encoding": "gzip, deflate, br",
        "content-type" : "application/json",
        "x-api-key" : os.getenv('SP_API_KEY'),
        "connect-protocol-version": "1"
    }

    r = requests.post(host+create_endpoint, data=json.dumps(payload), headers=headers)

    if r.status_code != 200:
        raise SPApiError("Error creating question")
    else:
        return r.json()


def hasSql(q: dict) -> bool:
    if "question" in q.keys():
        if "sql" in q['question'].keys():
            return True

    return False

def inSpace(space: str):
    def isInSpace(q: dict) -> bool:
        if "question" in q.keys():
            if "space" in q['question'].keys():
                return q['question']['space']['name'] == space

        return False

    return isInSpace