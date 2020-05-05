# !/usr/bin/env python
# Author: Caijie Fan
# Module name: Online_Variation
import requests
import json
from pyecharts.charts import Line
import pyecharts.options as opts
from bs4 import BeautifulSoup

class Online_Variation:
    def __init__(self):
        self.url = 'https://www.biliob.com/api/site/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        self.x_time = []
        self.y_wonline = []
        self.y_ponline = []
        self.getData()

    def getData(self):
        content = requests.get(url = self.url, headers = self.headers).content
        soup = BeautifulSoup(content, 'lxml')
        # Convert JSON to DIC and ascend order according to datetime
        lis = sorted(json.loads(soup.text), key = lambda el: el['datetime'])
        for each in lis:
            self.x_time.append(each['datetime'].replace('-', '/').replace(' ', '-')) 
            self.y_ponline.append(each['playOnline'])
            self.y_wonline.append(each['webOnline'])
        
    def renderData(self):
        (
            Line()
            .set_global_opts(
                title_opts = opts.TitleOpts(title = '24小时内B站在线数据折线图', 
                                            subtitle = 'Author:FCJ', 
                                            pos_left="center", 
                                            pos_top="top"),
                tooltip_opts = opts.TooltipOpts(trigger = "axis", axis_pointer_type = "line"),
                legend_opts = opts.LegendOpts(pos_left="left"),
                xaxis_opts = opts.AxisOpts(type_ = "category", boundary_gap = False),
                yaxis_opts = opts.AxisOpts(
                    type_ = "value",
                    axistick_opts = opts.AxisTickOpts(is_show = True),
                    # splitline_opts = opts.SplitLineOpts(is_show = True),
                ),
            )
            .add_xaxis(xaxis_data = self.x_time)
            .add_yaxis(
                series_name = "在线观看",
                y_axis = self.y_ponline,
                symbol = "emptyCircle",
                is_symbol_show = True,
                label_opts = opts.LabelOpts(is_show=False),
            )
            .add_yaxis(
                series_name = "在线人数",
                y_axis = self.y_wonline,
                symbol = "emptyCircle",
                is_symbol_show = True,
                label_opts = opts.LabelOpts(is_show = False),
            )
            .render("line.html")
        )
