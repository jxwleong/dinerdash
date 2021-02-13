import os
import subprocess

import psutil


class Process:
    def __init__(self, process_exec):
        self.process_exec = process_exec
        self.process_name = os.path.basename(self.process_exec)
        self.process_pid = self.set_pid
    
    @property
    def is_running(self):
        # source: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if self.process_name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    @property
    def launch(self):
        proc = subprocess.Popen(self.process_exec)
        self.process_pid = proc.pid

    @property
    def set_pid(self):
        if self.is_running:
            self.process_pid = self.__get_pid()

    def __get_pid(self):
        for proc in psutil.process_iter():
            if proc.name() == self.process_name:
                return proc.pid
