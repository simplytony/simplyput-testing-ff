import pytest
import time
from sp import CreateQuestion
from questions import questions

TEST_INTERVAL = 5

# used to put an interval between tests
@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(TEST_INTERVAL)


@pytest.mark.parametrize("question,tests", questions)
def test_question(question, tests):
    q = CreateQuestion(question)
    for t in tests:
        assert t(q)
