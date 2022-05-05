'''
Description: 先用o3d加载数据，然后matplotlib可视化
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-26 10:58:29
LastEditTime: 2022-05-05 15:14:36
FilePath: /Point-Clouds-Visualization/2open3D/ply/01o3d_load_ply&plt_vis.py
'''
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

print("Load a ply point cloud, print it, and render it")
file_name = "2open3D/data/conferenceRoom_1_GT.ply"
# visualization of point clouds.
pcd = o3d.io.read_point_cloud(file_name)
print(pcd)
print(np.asarray(pcd.points))

# 点云相关信息
pointCloud = np.asarray(pcd.points)
print(pointCloud.shape)

fig = plt.figure(dpi=150)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pointCloud[:, 0],pointCloud[:, 1],pointCloud[:, 2], s=0.01)
plt.show()

# o3d.visualization.draw_geometries([pcd])

''' 
PointCloud with 134536 points.
[[-15.61418152  39.51490784   2.21499991]
 [-15.64233303  39.52183533   2.19350004]
 [-15.60787392  39.50787354   2.19712496]
 ...
 [-15.32199955  39.56200027   0.829     ]
 [-15.33899975  39.56550217   0.4465    ]
 [-15.35999966  39.56999969   0.285     ]]

 '''
