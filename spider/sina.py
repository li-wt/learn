import sys

sys.path.append('.')
import requests  # 导包
from parse.sina import SinaParse
from loguru import logger
from fake_useragent import UserAgent


class SinaSpider:
    def __init__(self):
        self.url = "https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData"
        self.page = 1
        self.page_count = 40
        self.ua = UserAgent()

    def get_headers(self) -> dict:
        """
        这里是获取
        :return: 请求头
        """
        headers = {
            "user-agent": self.ua.random
        }
        return headers

    def get_params(self, node: str, page: int = 1) -> dict:
        """
        获取相应的参数
        :param node: 期货节点
        :param page: 页码
        :return:
        """
        params = {
            "page": page,
            "num": self.page_count,
            "sort": "symbol",
            "asc": 1,
            "node": node,
        }
        return params

    def request(self, page: int = 1, node: str = "hgt_sh"):
        """
        请求获取数据
        :return:
        """
        response = requests.get(url=self.url, headers=self.get_headers(),
                                params=self.get_params(page=page, node=node))
        return response.json()

    def run(self):
        node = "hgt_sh"
        while True:
            data = self.request(page=self.page, node=node)
            logger.info(f'第{self.page}页获取成功')
            SinaParse(data).parse_json()
            logger.info(f'第{self.page}页存储成功')
            if len(data) < self.page_count:
                return
            self.page += 1

    """我要采集那个期货的就要期货的"""


if __name__ == '__main__':
    sina = SinaSpider()
    sina.run()


