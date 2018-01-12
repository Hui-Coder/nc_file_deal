# nc_file_deal


|--- 处理气象数据（nc文件）


操作说明：
nc 文件命名为：deal_nc.nc,放到data目录下

1、 执行parse_nc.py，解析nc文件，同时在data目录下生成.npy数据文件
2、 执行draw_data.py ，获取.npy数据，并绘制图形
     
     注：1> 、会生成120*3 张图，若只想生成一张，请注视graph函数中的for 循环
         2> 、 默认绘制‘u’数据，获取其他数据绘制，只需要修改title值即可。如：title = 'v'
