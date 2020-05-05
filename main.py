# !/usr/bin/env python
# Author: Caijie Fan
# Module name: Main
# !/usr/bin/env python
# Author: Caijie Fan
# Module name: main
from Popular_KeyWord import Popular_KeyWord
from Online_Variation import Online_Variation
from History_Variation import History_Variation

def renderWordCloud():
    Popular_KeyWord().renderData()

def renderLine():
    Online_Variation().renderData()

def renderKline():
    History_Variation().renderData()

if __name__ == '__main__':
    renderWordCloud()
    renderLine()
    renderKline()
