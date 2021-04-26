'''
Description: open3D显示点云 https://blog.csdn.net/weixin_41281151/article/details/107119326
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-06 17:46:00
LastEditTime: 2021-04-26 10:41:51
FilePath: /Point-Clouds-Visualization/2open3D/ply/03open3d_show_ply.py
'''


import open3d as o3d  # 点云可视化
import os
import numpy as np # 读取txt文件
# import matplotlib.pyplot as plt # 没用到
# from pandas import DataFrame #  DataFrame(point_cloud_raw[:, 0:3]) 选取点云前三列
from pyntcloud import PyntCloud # pyntcloud是用于处理 3D 点云的python 库 

# # o3d读取ply文件===================================
# print("Load a ply point cloud, print it, and render it")
# pcd = o3d.io.read_point_cloud("s3dis-best-result/conferenceRoom_1_GT.ply")
# # print(pcd)
# # print(np.asarray(pcd.points))
# o3d.visualization.draw_geometries([pcd], zoom=0.3412,
#                                   front=[0.4257, -0.2125, -0.8795],
#                                   lookat=[2.6172, 2.0475, 1.532],
#                                   up=[-0.0694, -0.9768, 0.2024])

# PyntCloud加载自己的点云文件
file_name = "2open3D/data/conferenceRoom_1_GT.ply"
point_cloud_pynt = PyntCloud.from_file(file_name)

# np加载自己的点云文件
# points = np.genfromtxt("/home/hcq/data/modelnet40/modelnet40_normal_resampled/cup/cup_0006.txt", delimiter=",")
# points = DataFrame(points[:, 0:3]) # 前三列
# points.columns = ['x', 'y', 'z'] # 标题
# point_cloud_pynt = PyntCloud(points) # ================

# 转成open3d能识别的格式
point_cloud_o3d = point_cloud_pynt.to_instance("open3d", mesh=False)
o3d.visualization.draw_geometries([point_cloud_o3d]) # 显示原始点云
    