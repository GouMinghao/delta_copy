import shutil
import os
from .logging import Logger
from tqdm import tqdm

logger = Logger('delta_cp')

class DeltaCopier():
    def __init__(self, compare_log_name):
        self.compare_log_name = compare_log_name
        self.delta_file_list = []
        self._parse_log()

    def _parse_log(self):
        compare_log = open(self.compare_log_name)
        compare_raw_logs = compare_log.readlines()
        for compare_raw_log in compare_raw_logs:
            if compare_raw_log.startswith("#"):
                continue
            else:
                try:
                    src, dst = compare_raw_log.strip().split(',')
                    self.delta_file_list.append((src.strip(), dst.strip()))
                except:
                    logger.logwarning("Cannot parse raw log:{}".format(compare_log))
    
    def print_parsed_log(self):
        print("Parsed delta compare log\n=============")
        for delta_file in self.delta_file_list:
            print("src:{} | dst:{}".format(delta_file[0], delta_file[1]))
        print("=============")

    def print_and_exec_delta_copy(self):
        self.print_parsed_log()
        continue_flag = False
        while True:
            input_char = input('continue? (y/n):').strip().lower()
            if input_char == 'y':
                continue_flag = True
                break
            elif input_char == 'n':
                break
        if not continue_flag:
            raise ValueError('User aborts the task')
        self._exec_delta_copy()

    def _exec_delta_copy(self):
        for delta_file in tqdm(self.delta_file_list, "Executing delta copy"):
            src, dst = delta_file
            if os.path.isdir(os.path.abspath(src)):
                shutil.copytree(
                    os.path.abspath(src),
                    os.path.abspath(dst)
                )
            else:
                shutil.copy2(
                    os.path.abspath(src),
                    os.path.abspath(dst)
                )