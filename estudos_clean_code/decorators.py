def operations(function):
    def wrapper(*args, **kwargs):
        try:
            print("Numbers:", *args)
            print("Operation:", function.__name__)
            response = function(*args, **kwargs)
            print("Result:", response)
            return response
        except Exception as err:
            raise ValueError(f'{err.__str__()}')

    return wrapper
