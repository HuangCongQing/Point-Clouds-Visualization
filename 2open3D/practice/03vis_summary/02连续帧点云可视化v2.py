'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-09-13 18:10:38
LastEditTime: 2023-09-13 18:17:33
FilePath: /Point-Clouds-Visualization/2open3D/practice/03vis_summary/02连续帧点云可视化v2.py
'''
import open3d as o3d
import numpy as np
import os

# 设置连续点云的文件夹路径
data_folder = 'path_to_your_npy_files_folder'

# 获取文件夹中的所有npy文件
npy_files = [f for f in os.listdir(data_folder) if f.endswith('.npy')]
npy_files.sort()  # 确保按顺序播放

# 创建Open3D Visualizer
visualizer = o3d.visualization.Visualizer()
visualizer.create_window()

# 用于控制播放的标志
play = True

# 获取文件夹中的所有npy文件
npy_files = [f for f in os.listdir(data_folder) if f.endswith('.npy')]
npy_files.sort()  # 确保按顺序播放

# 创建Open3D Visualizer
visualizer = o3d.visualization.Visualizer()
visualizer.create_window()

# 用于控制播放的标志
play = True

# 创建一个函数来切换播放状态
def toggle_play(vis):
    nonlocal play
    play = not play

# 注册鼠标点击事件
visualizer.register_key_callback(ord(" "), toggle_play)

for npy_file in npy_files:
    # 读取Numpy文件
    point_cloud = np.load(os.path.join(data_folder, npy_file))

    # 创建Open3D点云对象
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud)

    # 添加点云到Visualizer
    visualizer.add_geometry(pcd)

    while play:
        # 清除上一帧数据并添加新的点云
        visualizer.update_geometry(pcd)
        visualizer.poll_events()
        visualizer.update_renderer()

    # 暂停并等待鼠标点击以继续播放
    while not play:
        visualizer.poll_events()

    # 移除上一帧点云
    visualizer.remove_geometry(pcd)

# 关闭Open3D窗口
visualizer.destroy_window()
