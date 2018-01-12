#!/usr/bin/python
# coding:utf-8

import sys
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


# 数据文件路径
def data_path(filename):
    file_path = "{path}/data/{filename}".format(
        path=sys.path[0],
        filename=filename
    )
    return file_path


# 获取数据
def read_data(path):
    data = np.load(path)
    print log_string, path, '数据读取'
    return data


# 绘制
def graph(lon, lat, target, title):
    print log_string, '开始绘制, 参数数据：', 'longitude:', lon.shape, ' latitude:', lat.shape, title, ":", target.shape
    b_map = Basemap(resolution='l', area_thresh=10000, projection='cyl', llcrnrlon=0, urcrnrlon=360, llcrnrlat=-90,
                    urcrnrlat=90)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    lon, lat = np.meshgrid(lon, lat)
    x, y = b_map(lon, lat)
    for i in range(target.shape[0]):
        for j in range(target.shape[1]):
            cs = b_map.contourf(x, y, target[i, j, :, :])
            b_map.colorbar(cs)
            b_map.drawcoastlines(linewidth=0.2)
            plt.title(title, size=20)
            pic_path = sys.path[0] + '/data/' + title + '_pic/'+str(i)+'_'+str(j)+'.png'
            plt.savefig(pic_path)
            print log_string, sys.path[0] + '/data/' + title + '_pic/'+str(i)+'_'+str(j)+'.png  saved'
    plt.close()


if __name__ == '__main__':
    log_string = 'Log draw_data.py : '
    title = 'u'
    longitude = read_data(data_path('longitude.npy'))
    latitude = read_data(data_path('latitude.npy'))
    tar = read_data(data_path(title+'.npy'))
    scale_factor = read_data(data_path(title+'_scale_factor.npy'))
    add_offset = read_data(data_path(title+'_add_offset.npy'))
    new_tar = tar*scale_factor+add_offset  # 偏移计算
    graph(longitude, latitude, new_tar, title)   # 画图