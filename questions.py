from sp import hasSql, inSpace
import os
print(os.getenv("ORG_ID"))
# Here is where you put in the questions you want to test:
questions = [
    ("How many questions were there?", [hasSql, inSpace("Questions")])
]
