#!/usr/bin/python
# coding=utf-8

from netCDF4 import Dataset
import numpy as np
import sys


def parse_nc():
    file_path = "{path}/data/{filename}".format(
        path=sys.path[0],
        filename='deal_nc.nc'
    )
    print log_string, '开始解析文件', file_path
    nc = Dataset(file_path)
    for var in nc.variables.keys():
        path = sys.path[0]+'/data/'+var
        np.save(path, nc.variables[var][:])
        print log_string, path + '.npy', '数据写入'
        if var == 'u' or var == 'v' or var == 'z' or var == 't':
            np.save(path+'_scale_factor', nc.variables[var].getncattr('scale_factor'))
            print log_string, path + '_scale_factor.npy', '数据写入'
            np.save(path+'_add_offset', nc.variables[var].getncattr('add_offset'))
            print log_string, path + '_add_offset.npy', '数据写入'
    nc.close()
    print log_string, '数据全部写入完毕 !!！'


log_string = 'Log parse_nc.py :'
parse_nc()
