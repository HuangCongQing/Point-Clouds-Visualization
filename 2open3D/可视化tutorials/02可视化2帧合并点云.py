'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-09 14:31:50
LastEditTime: 2023-08-09 14:37:56
FilePath: /Point-Clouds-Visualization/2open3D/可视化tutorials/01可视化单帧点云.py
'''
import open3d as o3d
import numpy as np

# 创建第一个点云（红色）
pcd1 = o3d.geometry.PointCloud()
points1 = np.random.rand(1000, 3)
pcd1.points = o3d.utility.Vector3dVector(points1)

# 创建第二个点云（绿色）
pcd2 = o3d.geometry.PointCloud()
points2 = np.random.rand(1000, 3)
pcd2.points = o3d.utility.Vector3dVector(points2)

# 创建一个可视化窗口
vis = o3d.visualization.Visualizer()
vis.create_window()

# 创建一个点云合并容器
merged_pcd = o3d.geometry.PointCloud()
merged_pcd.points = o3d.utility.Vector3dVector(np.vstack((points1, points2)))

# 根据合并后的点云大小设置点的大小
# merged_pcd_colors = np.hstack((np.full(len(points1), 0), np.full(len(points2), 1)))
# merged_pcd_colors = np.expand_dims(merged_pcd_colors, axis=1)
# merged_pcd.colors = o3d.utility.Vector3dVector(merged_pcd_colors)

# # 设置点云的显示大小，即根据不同颜色的点云来设置不同的大小
# sizes = np.array([2.0 if c == 0 else 5.0 for c in merged_pcd_colors])
# sizes = np.expand_dims(sizes, axis=1)
# merged_pcd.point_sizes = o3d.utility.DoubleVector(sizes)

# 将点云添加到窗口中
vis.add_geometry(merged_pcd)

# 显示窗口中的点云
vis.run()
vis.destroy_window()
