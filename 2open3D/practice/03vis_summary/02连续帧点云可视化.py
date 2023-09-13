'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-09-13 18:04:52
LastEditTime: 2023-09-13 18:08:27
FilePath: /Point-Clouds-Visualization/2open3D/practice/03vis_summary/02连续帧点云可视化.py
'''
import open3d as o3d
import numpy as np
import time

# 生成示例点云数据和标签数据（这里使用随机数据作为示例）
num_frames = 10
num_points_per_frame = 1000
point_clouds = []
labels = []

for frame_id in range(num_frames):
    # 生成随机点云数据
    points = np.random.rand(num_points_per_frame, 3) * 10  # 随机生成点的坐标
    colors = np.random.rand(num_points_per_frame, 3)  # 随机生成点的颜色

    # 创建Open3D点云对象
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.colors = o3d.utility.Vector3dVector(colors)

    # 添加到点云列表中
    point_clouds.append(point_cloud)

    # 为每帧分配不同的标签（这里示例使用frame_id作为标签）
    labels.append(frame_id)

# 创建Open3D可视化窗口
vis = o3d.visualization.Visualizer()
vis.create_window()

# 设置不同标签对应的颜色
label_colors = {
    0: [1, 0, 0],  # 红色
    1: [0, 1, 0],  # 绿色
    2: [0, 0, 1],  # 蓝色
    3: [1, 1, 0],  # 黄色
    4: [1, 0, 1]   # 洋红色
}

# 可视化每帧点云，并根据标签着色
for frame_id, (point_cloud, label) in enumerate(zip(point_clouds, labels)):
    point_cloud.paint_uniform_color(label_colors[label])
    vis.add_geometry(point_cloud)
    vis.update_geometry(point_cloud)
    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image(f"frame_{frame_id}.png")
    time.sleep(1)

# 关闭可视化窗口
vis.destroy_window()
