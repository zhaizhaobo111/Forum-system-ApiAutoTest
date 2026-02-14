import requests
from utils.logger_util import logger

host="http://127.0.0.1:58080/"
class  Request:
    log=logger.getlog()
    def get(self,url,**kwargs):
        self.log.info("准备发起get请求，url:"+url)
        self.log.info("接口信息:{}".format(kwargs))
        r=requests.get(url=url,**kwargs)
        self.log.info('接口响应状态码：{}'.format(r.status_code))
        self.log.info('接口响应''内容是：{}'.format(r.json()))

        try:
            self.log.info('接口响应内容是：{}'.format(r.json()))
        except:
            self.log.info('接口响应内容是：{}'.format(r.text))
        return r




    def post(self, url, **kwargs):
         self.log.info("准备发起post请求，url:" + url)
         self.log.info("接口信息:{}".format(kwargs))

         r = requests.post(url=url, **kwargs)

         self.log.info('接口响应状态码：{}'.format(r.status_code))
         try:
             self.log.info('接口响应内容是：{}'.format(r.json()))
         except:
             self.log.info('接口响应内容是：{}'.format(r.text))
         return r