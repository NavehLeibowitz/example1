def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped


def if_books(fn):
    def wrapped():
        if books:
            return fn()
    return wrapped


@if_books
def hello():
    return "hello world"


books = input("Insert book names:").split()
print(hello())
