import open3d as o3d
import numpy as np
import time
import os
from alfred.fusion.kitti_fusion import load_pc_from_file  # 加载点云
from alfred.fusion.common import compute_3d_box_lidar_coords

# 可视化原始点云
def draw_points():

    # 初始化窗口
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name='pcd', width=800, height=600)
    # 可视化参数设置
    opt = vis.get_render_option()
    # 设置背景色
    opt.background_color = np.asarray([0, 0, 0])
    # 设置点云大小
    opt.point_size = 1
    opt.show_coordinate_frame = True
    # 创造pcd类型数据(后面调用pcobj.points = ...)
    pcobj = o3d.geometry.PointCloud() # 不要放在for循环里面
    # road_pc = o3d.geometry.PointCloud() # 可以创建多个！！
    # 鼠标变换视角
    to_reset = True

    # 点云加载===============================
    print("可视化原始点云\n")
    files_path = "/home/hcq/pointcloud/Point-Clouds-Visualization/data_test/bin"
    file_list = os.listdir(files_path)
    file_list.sort()
    for file in file_list:
        v_f = os.path.join(files_path, file)
        pcs = load_pc_from_file(v_f) # 调用库加载点云文件
        geometries = []
        pcs = np.array(pcs[:, :3])
        # 加载点云
        pcobj.points = o3d.utility.Vector3dVector(pcs)
        # 调整点云颜色
        # pcobj.paint_uniform_color([1, 0, 0])
        # 可视化
        vis.update_geometry(pcobj)
        vis.add_geometry(pcobj)
        # 鼠标变换视角
        if to_reset:
            vis.reset_view_point(True)
            to_reset = False
        vis.poll_events()
        vis.update_renderer()
        # 设置休眠时间
        time.sleep(0.5)
    print("vis end")
    # vis.destroy_window()

# 可视化原始点云和box
def draw_points_with_boxes():
    print("可视化原始点云和box\n")


if __name__ == '__main__':
    draw_points()