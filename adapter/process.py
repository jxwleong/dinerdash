import os
import subprocess

import psutil


class Process:
    def __init__(self, executable_path):
        self.executable_path = executable_path
        self.name = os.path.basename(self.executable_path)
        self.__pid = None
    
    @property
    def is_running(self):
        # source: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if self.name.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def launch(self):
        proc = subprocess.Popen(self.executable_path)
        self.__pid = proc.pid
    
    @property
    def pid(self):
        if self.is_running:
            self.__pid = self.__get_pid()        
        return self.__pid


    def __get_pid(self):
        for proc in psutil.process_iter():
            if proc.name() == self.name:
                return proc.pid
