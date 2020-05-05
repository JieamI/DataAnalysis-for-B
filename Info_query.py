# !/usr/bin/env python
# Author: Caijie Fan
# Module name: Info_query
import requests
import json
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
import pyecharts.options as opts

# Video information query class
class Av_query:
    def __init__(self, av):
        self.url = 'http://api.bilibili.com/archive_stat/stat?aid=' + av + '&type=jsonp'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        self.x_data = []
        self.y_data = []
        self.getData()

    def getData(self):
        content = requests.get(url = self.url, headers = self.headers).content
        soup = BeautifulSoup(content, 'lxml')
        # Convert JSON to DIC
        dic = json.loads(soup.text)
        if dic['message'] != '0':
            print("请输入正确的AV号！")
            return
        self.x_data = ['点赞', '硬币', '收藏', '分享', '评论']
        self.y_data = [dic['data']['like'], 
                       dic['data']['coin'], 
                       dic['data']['favorite'], 
                       dic['data']['share'], 
                       dic['data']['reply']]
    
    def renderData(self):
        if self.y_data:
            (
                Bar()
                .add_xaxis(xaxis_data = self.x_data)
                .add_yaxis('', yaxis_data = self.y_data)
                .set_global_opts(
                    title_opts = opts.TitleOpts(title = "视频数据分析图", 
                                                subtitle = 'Author:FCJ', 
                                                pos_left = "center", 
                                                pos_top = "top")
                ).render(r'.\Info_query\av_Bar.html')
            )


# UP information query class
class Up_query:
    def __init__(self, uid):
        self.url1 = 'https://api.bilibili.com/x/relation/stat?vmid=' + uid + '&jsonp=jsonp'
        self.url2 = 'https://api.bilibili.com/x/space/upstat?mid=' + uid + '&jsonp=jsonp'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        self.x_data = []
        self.y_data = []
        self.getData()

    def getData(self):
        content1 = requests.get(url = self.url1, headers = self.headers).content
        content2 = requests.get(url = self.url2, headers = self.headers).content
        soup1 = BeautifulSoup(content1, 'lxml')
        soup2 = BeautifulSoup(content2, 'lxml')
        # Convert JSON to DIC
        dic1 = json.loads(soup1.text)
        dic2 = json.loads(soup2.text)
        if dic1['message'] != '0' or dic2['message'] != '0':
            print("请输入正确的UID！")
            return
        self.x_data = ['关注', '粉丝', '获赞', '播放', '阅读']
        self.y_data = [dic1['data']['following'], 
                       dic1['data']['follower'], 
                       dic2['data']['likes'], 
                       dic2['data']['archive']['view'], 
                       dic2['data']['article']['view']]
    
    def renderData(self):
        if self.y_data:
            (
                Bar()
                .add_xaxis(xaxis_data = self.x_data)
                .add_yaxis('', yaxis_data = self.y_data)
                .set_global_opts(
                    title_opts = opts.TitleOpts(title = "UP主数据分析图", 
                                                subtitle = 'Author:FCJ', 
                                                pos_left = "center", 
                                                pos_top = "top")
                ).render(r'.\Info_query\up_Bar.html')
            )