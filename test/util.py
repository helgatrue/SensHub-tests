from datetime import datetime


def get_dated_name(name, extension):
    return name + str(datetime.now()) + extension
