'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-26 10:58:29
LastEditTime: 2021-04-26 10:58:53
FilePath: /Point-Clouds-Visualization/2open3D/ply/01read_ply.py
'''
import open3d as o3d


file_name = "2open3D/data/conferenceRoom_1_GT.ply"
# visualization of point clouds.
pcd = o3d.io.read_point_cloud(file_name)
o3d.visualization.draw_geometries([pcd])
