from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("销量", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("价格", [14, 5, 7, 11, 25, 27, 10])
bar.add_yaxis("库存",[27,155,33,42,42,44,99])
#bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
#bar.render()
bar.render("生成图表.html")

