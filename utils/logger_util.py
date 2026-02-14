import logging
import os.path
import time

class infoFilter(logging.Filter):
    def filter(self, record):
        return  record.levelno==logging.INFO
class errFilter(logging.Filter):
    def filter(self, record):
        return  record.levelno==logging.ERROR
class logger:
    # 获取日志对象--定义类方法@classmethod
    @classmethod
    def getlog(cls):
        # 创建日志对象
        cls.logger=logging.getLogger(__name__)
        cls.logger.setLevel(logging.DEBUG)

        LOG_PATH = "./logs/"
        if not os.path.exists(LOG_PATH):
            # 没有创建，创建一个
            os.mkdir(LOG_PATH)
        # 将日志输出到日志文件中 my.log
        '''
        logs
            ./logs/+2026-2-13.log
            2026-2-13-info.log
            2026-2-13-err.log
        '''
        # 按年月日
        now=time.strftime("%Y-%m-%d")
        log_name=LOG_PATH+now+".log"
        info_log_name=LOG_PATH+now+"-info.log"
        err_log_name =LOG_PATH+now+"-err.log"

        # 保证log文件夹必须创办好了
        # 创建文件管理器
        all_handler=logging.FileHandler(log_name,encoding="utf-8")
        info_handler = logging.FileHandler(info_log_name, encoding="utf-8")
        err_handler = logging.FileHandler(err_log_name, encoding="utf-8")

        # 创建处理器,将日志输出到控制台
        streamHandle=logging.StreamHandler()

        # 创建一个日志格式器对象
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s")
        # 将格式器设置到处理器上
        all_handler.setFormatter(formatter)
        info_handler.setFormatter(formatter)
        err_handler.setFormatter(formatter)
        streamHandle.setFormatter(formatter)
        # 添加过滤器(添加类对象)
        info_handler.addFilter(infoFilter())
        err_handler.addFilter(errFilter())
        # 将这个处理器添加到日志记录器中
        # 这样，日志记录器就会使用这个处理器来处理日志信息
        cls.logger.addHandler(all_handler)
        cls.logger.addHandler(info_handler)
        cls.logger.addHandler(err_handler)
        cls.logger.addHandler(streamHandle)
        return cls.logger


