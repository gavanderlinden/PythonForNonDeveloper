from functools import wraps


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


           
