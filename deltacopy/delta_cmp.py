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
    def compare(self):
        if not self.src_flag or not self.dst_flag:
            logger.logerror("src or dst doesn't exist")
            raise ValueError("src or dst doesn't exist")
        