# !/usr/bin/env python
# Author: Caijie Fan
# Module name: Popular_KeyWord
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import WordCloud
import pyecharts.options as opts
import json

class Popular_KeyWord:
    def __init__(self):
        self.url = 'https://www.biliob.com/api/video/popular-keyword'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        self.res_lis = []
        self.getData()
    
    def getData(self):
        content = requests.get(url = self.url, headers = self.headers).content
        soup = BeautifulSoup(content, 'lxml')
        # Convert JSON to DIC
        lis = json.loads(soup.text)
        for each in lis:
            self.res_lis.append((each['_id'], each['value']))
        # Descending order according to 'count'
        # self.res_lis.sort(key = lambda el: el[1], reverse = True) 

    def renderData(self):
        (
            WordCloud()
            .set_global_opts(
                title_opts = opts.TitleOpts(title = 'B站流行词汇词云图', 
                                            subtitle = 'Author:FCJ', 
                                            pos_left = "center", 
                                            pos_top = "top")
            )
            .add('', data_pair = self.res_lis, shape = 'circle')
            .render('wordcloud.html')
        )