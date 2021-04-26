'''
Description: open3D显示点云 https://blog.csdn.net/weixin_41281151/article/details/107119326
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-06 17:46:00
LastEditTime: 2021-03-06 20:32:12
FilePath: /Point-Clouds/2open3D/01open3d中显示原点云图.py
'''

import open3d as o3d 
import os
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from pyntcloud import PyntCloud

# 读取txt文件
# point_cloud_raw = np.genfromtxt(r"/home/hcq/data/modelnet40/modelnet40_normal_resampled/plant/plant_0001.txt", delimiter=",")  #为 xyz的 N*3矩阵
# point_cloud_raw = DataFrame(point_cloud_raw[:, 0:3])  # 选取每一列 的 第0个元素到第二个元素   [0,3)
# point_cloud_raw.columns = ['x', 'y', 'z']  # 给选取到的数据 附上标题
# point_cloud_pynt = PyntCloud(point_cloud_raw)  # 将points的数据 存到结构体中

# point_cloud_o3d = point_cloud_pynt.to_instance("open3d", mesh=False)  # 实例化

# o3d.visualization.draw_geometries([point_cloud_o3d]) # 显示原始点云


# 读取ply文件
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("s3dis-best-result/conferenceRoom_1_GT.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd], zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])


    