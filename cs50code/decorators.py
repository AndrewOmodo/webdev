def announce(f):
    def wrapper(f):
        print('About to run the funtion...')
        f()
        print('Done running the function!')
        return wrapper

@announce
def hello():
     print('Hello world')

hello()