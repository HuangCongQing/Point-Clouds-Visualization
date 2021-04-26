'''
Description: https://blog.csdn.net/io569417668/article/details/108978225

Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-26 10:41:04
LastEditTime: 2021-04-26 10:52:56
FilePath: /Point-Clouds-Visualization/2open3D/ply/voxel_show_ply.py
'''

import numpy as np
import open3d

def load_ply_point_cloud(filename,voxel_size=0.5):
    print("Load a ply point cloud, print it, and render it")
    mesh= open3d.io.read_triangle_mesh(filename)
    voxel_mesh = open3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh,voxel_size) # Open3d提供了create_from_triangle_mesh函数能够从三角网格中生成体素网格。
    return mesh,voxel_mesh

file = '2open3D/data/conferenceRoom_1_GT.ply'
size = 0.7
mesh,voxel_mesh= load_ply_point_cloud(file,size)
open3d.visualization.draw_geometries([mesh])

# 点云

points_ar = []
for x in voxel_mesh.voxels:
    points_ar.append(x.grid_index)
points = np.array(points_ar)
pcd = open3d.geometry.PointCloud()
pcd.points = open3d.utility.Vector3dVector(points)

# 可视化
open3d.visualization.draw_geometries([pcd])

