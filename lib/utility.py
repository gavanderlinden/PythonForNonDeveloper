import json
from pathlib import Path
from functools import wraps

__dir__ = Path(__file__).absolute().parent


def check_output(expected=None):
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            result = f(*args, **kwargs)
            if result == expected:
                return "CORRECT", result
            else:
                return "WRONG", result
        return wrap
    return decorator


def check_answer(_globals, answers):
    no_errors = True
    locals().update(_globals)
    for answer in answers:
        
        # run eval, catch any exceptions
        try:
            result = eval(answer["eval"])
        except NameError as error:
            no_errors = False
            print(answer.get("name_error", error))
            continue
        except:
            no_errors = False
            print(answer["message"])
            continue
        
        if result is True:
            continue
        elif result is False:
            no_errors = False
            print(answer["message"])
        else:
            no_errors = False
            print("unexpected test output")

    if no_errors:
        print("CORRECT")


class QA(object):

    def __init__(self, file_name):
        self.__file_path = __dir__.parent/"data"/("%s.json" % file_name)
        self.__data = json.load(self.__file_path.open())

    def run(self, _id):
        for question in self.__data[_id]:
            yield self.ask_question(question)
        print("GOOD JOB!")

    def ask_question(self, data):
        question = data["question"]
        answer = data["answer"]
        method = data["method"]
        while True:

            # just execute some code
            if method == "declare":
                print(question)
                return answer

            code = self.standardize_code(input(question + ": "))
            if method == "text":
                result = (answer == code)
                code = ""
            else:
                result = (code == answer)

            if result:
                print("CORRECT")
                return code
            else:
                print("WRONG")

    @staticmethod
    def standardize_code(code):
        return code.replace('"', "'")
