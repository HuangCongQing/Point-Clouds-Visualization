'''
Description: draw_geometries
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-27 11:35:02
LastEditTime: 2021-04-27 11:35:02
FilePath: /Point-Clouds-Visualization/2open3D/Open3d学习计划/08可视化/02draw_geometries.py
'''
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("../../TestData/fragment.ply")
o3d.visualization.draw_geometries([pcd], zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])