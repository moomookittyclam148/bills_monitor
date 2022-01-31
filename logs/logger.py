import os

script_dir = os.path.dirname(__file__)

class Logger:
    def __init__(self, file=""):
        self.log_start = "[logger]"
        if file != "":
            # open file and prep for log input
            print()

    def info(self, log_message):
        logger_info_start = f"{self.log_start} INFO:"
        print(f"{logger_info_start} {log_message}")

    def error(self, log_message):
        logger_error_start = f"{self.log_start} ERROR:"
        print(f"{logger_error_start} {log_message}")
