import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.logs.logger import log_info


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.restart_process()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            log_info(f"{event.src_path} has been modified")
            self.run_tools()
            self.restart_process()

    def run_tools(self):
        # Run flake8 for linting
        log_info("Running flake8 for linting...")
        flake8_process = subprocess.Popen(
            ["pipenv", "run", "flake8", "src/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        flake8_out, flake8_err = flake8_process.communicate()
        if flake8_out:
            log_info(flake8_out.decode())
        if flake8_err:
            log_info(flake8_err.decode())

        # Run mypy for type checking (optional, if you use mypy)
        log_info("Running mypy for type checking...")
        mypy_process = subprocess.Popen(
            ["pipenv", "run", "mypy", "src/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        mypy_out, mypy_err = mypy_process.communicate()
        if mypy_out:
            log_info(mypy_out.decode())
        if mypy_err:
            log_info(mypy_err.decode())

        # Run autopep8 for automatic code fixing
        log_info("Running autopep8 for auto-fixing...")
        autopep8_process = subprocess.Popen(
            [
                "pipenv",
                "run",
                "autopep8",
                "--in-place",
                "--aggressive",
                "--recursive",
                "src/",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        autopep8_out, autopep8_err = autopep8_process.communicate()
        if autopep8_out:
            log_info(autopep8_out.decode())
        if autopep8_err:
            log_info(autopep8_err.decode())

        # Run black for auto-formatting
        log_info("Running black for auto-formatting...")
        black_process = subprocess.Popen(
            ["pipenv", "run", "black", "src/"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        black_out, black_err = black_process.communicate()
        if black_out:
            log_info(black_out.decode())
        if black_err:
            log_info(black_err.decode())

    def restart_process(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen(self.command, shell=True)
        log_info("Server restarted")


if __name__ == "__main__":
    command = "python src/main.py"
    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path="src/", recursive=True)
    observer.start()
    log_info("Watching for file changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
