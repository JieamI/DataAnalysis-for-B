# !/usr/bin/env python
# Author: Caijie Fan
# Module name: History_Variation
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Kline
from pyecharts.commons.utils import JsCode
import pyecharts.options as opts
import json

class History_Variation:
    def __init__(self):
        self.url = 'https://www.biliob.com/api/site/history-play?days=365'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        self.x_time = []
        self.k_data = []
        self.getData()
    
    def getData(self):
        content = requests.get(url = self.url, headers = self.headers).content
        soup = BeautifulSoup(content, 'lxml')
        # Convert JSON to DIC and ascend order according to date
        lis = sorted(json.loads(soup.text), key = lambda el: el['date'])
        for each in lis:
            self.x_time.append(each['date'])
            self.k_data.append([each['first'], each['last'], each['min'], each['max']])


    def renderData(self):
        (
            Kline()
            .add_xaxis(xaxis_data = self.x_time)
            .add_yaxis("", self.k_data)
            .set_global_opts(
                yaxis_opts = opts.AxisOpts(is_scale = True),
                xaxis_opts = opts.AxisOpts(is_scale = True),
                title_opts = opts.TitleOpts(title = "B站最大在线观看周线", 
                                            subtitle = 'Author:FCJ', 
                                            pos_left = "center", 
                                            pos_top = "top"),
                tooltip_opts = opts.TooltipOpts(
                    # Customize tooltip content
                    formatter = JsCode(
                        """
                        function (params) {
                            return params.name + '<br>' +
                                    '首天最值:' + params.value[1] + '<br>' +
                                    '末天最值:' + params.value[4] + '<br>' +
                                    '周最大值:' + params.value[2] + '<br>' +
                                    '周最小值:' + params.value[3]
                        }
                        """
                    )
                )
            )
            .render("kline.html")
        )