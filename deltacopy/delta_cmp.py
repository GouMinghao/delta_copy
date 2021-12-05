from datetime import datetime
import os
from .logging import Logger

logger = Logger('delta_cmp')

class DeltaComparer():
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        if not os.path.exists(src):
            logger.logwarning("src:{} doesn't exist".format(src))
            self.src_flag = False
        else:
            self.src_flag = True
        if not os.path.exists(dst):
            logger.logwarning("dst:{} doesn't exist".format(dst))
            self.dst_flag = False
        else:
            self.dst_flag = True
        self.missing_record_list = []
        self.log_name = "compare_result_{}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        if os.path.exists(self.log_name):
            logger.logwarning("log file {} already exists".format(self.log_name))
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
        self.log_file = open(self.log_name, 'w')
        self.log_file.write("# === delta cmp record === #\n# src:{} #\n# dst:{} #\n# ====== #\n".format(self.src, self.dst))

    def compare(self, write_record = True):
        if not self.src_flag or not self.dst_flag:
            logger.logerror("src or dst doesn't exist")
            raise ValueError("src or dst doesn't exist")
        self._dfs([self.src], [self.dst], write_record = write_record)

    def _dfs(self, cur_src_list, cur_dst_list, write_record = True):
        logger.logdebug("Visiting {}".format(os.path.join(*cur_dst_list)))
        if not os.path.exists(os.path.join(*cur_dst_list)):
            logger.logdebug("{} missing".format(os.path.join(*cur_dst_list)))
            self.missing_record_list.append((
                os.path.join(*cur_src_list),
                os.path.join(*cur_dst_list)
            ))
            if write_record:
                self.log_file.write("{}, {}\n".format(
                    os.path.join(*cur_src_list),
                    os.path.join(*cur_dst_list)
                ))
            
        elif os.path.isdir(os.path.join(*cur_dst_list)):
            try:
                files = os.listdir(os.path.join(*cur_src_list))
                for file in files:
                    cur_src_list.append(file)
                    cur_dst_list.append(file)
                    self._dfs(cur_src_list, cur_dst_list)
                    cur_src_list.pop()
                    cur_dst_list.pop()
            except PermissionError:
                logger.logwarning("Cannot visit {}".format(os.path.join(*cur_src_list)))
