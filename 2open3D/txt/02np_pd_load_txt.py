'''
Description: open3D显示点云 https://blog.csdn.net/weixin_41281151/article/details/107119326
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-06 17:46:00
LastEditTime: 2021-04-26 10:26:41
FilePath: /Point-Clouds-Visualization/2open3D/02open3d_show_txt.py
'''

import open3d as o3d  # 点云可视化
import os
import numpy as np # 读取txt文件
# import matplotlib.pyplot as plt # 没用到
from pandas import DataFrame #  DataFrame(point_cloud_raw[:, 0:3]) 选取点云前三列
from pyntcloud import PyntCloud # pyntcloud是用于处理 3D 点云的python 库 

# 读取txt文件
point_cloud_raw = np.genfromtxt(r"2open3D/data/plant_0001.txt", delimiter=",")  #为 xyz的 N*3矩阵
point_cloud_raw = DataFrame(point_cloud_raw[:, 0:3])  # 选取每一列 的 第0个元素到第二个元素   [0,3)
point_cloud_raw.columns = ['x', 'y', 'z']  # 给选取到的数据 附上标题

point_cloud_pynt = PyntCloud(point_cloud_raw)  # 将points的数据 存到结构体中
point_cloud_o3d = point_cloud_pynt.to_instance("open3d", mesh=False)  # 实例化
# 可视化
o3d.visualization.draw_geometries([point_cloud_o3d]) # 显示原始点云


    