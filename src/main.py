# -*- coding:utf-8 -*-

"""
行情服务

Author: HuangTao
Date:   2018/05/04
"""

import sys

from quant.quant import quant
from quant.config import config
from quant.const import OKEX, OKEX_MARGIN, OKEX_FUTURE, BINANCE, DERIBIT, BITMEX, HUOBI, COINSUPER


def initialize():
    """ 初始化
    """

    for platform in config.platforms:
        if platform == OKEX or platform == OKEX_MARGIN:
            from platforms.okex import OKEx as Market
        elif platform == OKEX_FUTURE:
            from platforms.okex_ftu import OKExFuture as Market
        elif platform == BINANCE:
            from platforms.binance import Binance as Market
        elif platform == DERIBIT:
            from platforms.deribit import Deribit as Market
        elif platform == BITMEX:
            from platforms.bitmex import Bitmex as Market
        elif platform == HUOBI:
            from platforms.huobi import Huobi as Market
        elif platform == COINSUPER:
            from platforms.coinsuper import CoinsuperMarket as Market
        else:
            from quant.utils import logger
            logger.error("platform error! platform:", platform)
            continue
        cc = config.platforms[platform]
        cc["platform"] = platform
        Market(**cc)


def main():
    config_file = sys.argv[1]  # 配置文件 config.json
    quant.initialize(config_file)
    initialize()
    quant.start()


if __name__ == "__main__":
    main()
