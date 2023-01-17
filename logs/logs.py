import functools
import logging
import time
from datetime import datetime

from test.util import get_dated_name


def log_config(_func=None):
    def log_decorator_info(func):
        @functools.wraps(func)
        def log_decorator_wrapper():
            logging.basicConfig(
                style='{',
                filemode="w",
                filename=get_dated_name('logs/', '.log'),
                level=logging.DEBUG,
                format="{asctime} {levelname:<8} {message}",
            )
            logger = logging.getLogger()
            test_name = str(func)
            print("Running test function: ", test_name)
            try:
                start = time.time()
                func()
                finish = time.time()
                print("Test: ", test_name, "completed. Execution time: ", finish - start, " s.")
            except Exception as ex:
                logger.error("Error when running test: " + test_name + " with exception: " + str(ex))
                print(ex)

        return log_decorator_wrapper

    if _func is None:
        return log_decorator_info
    else:
        return log_decorator_info(_func)