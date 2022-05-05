import open3d as o3d
import numpy as np
import time
import os
from alfred.fusion.kitti_fusion import load_pc_from_file  # 加载点云
from alfred.fusion.common import compute_3d_box_lidar_coords # 转换bbox使用

# 可视化原始点云
def draw_points():
    print("可视化原始点云\n")

# 可视化原始点云和box
def draw_points_with_boxes():
    print("可视化原始点云和box\n")

    # 初始化窗口
    vis = o3d.visualization.Visualizer()
    # vis.create_window(window_name='pcd', width=800, height=600)
    vis.create_window(window_name='pcd')
    # 可视化参数设置
    opt = vis.get_render_option()
    # 视角拖拽
    ctr = vis.get_view_control()
    ctr.set_lookat(np.array([0.0, 0.0, 55.0]))
    ctr.set_up((0, -1, 0))  # set the positive direction of the x-axis as the up direction
    ctr.set_front((-1, 0, 0))  # set the positive direction of the x-axis toward you

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
    files_path = "/home/hcq/pointcloud/Point-Clouds-Visualization/data_test/bin/livox"
    file_list = os.listdir(files_path)
    file_list.sort()
    for file in file_list:
        v_f = os.path.join(files_path, file)
        pcs = load_pc_from_file(v_f) # 调用库加载点云文件
        geometries = []
        pcs = np.array(pcs[:, :3])
        # 加载点云
        # pcobj.points = o3d.utility.Vector3dVector(pcs)
        # 调整点云颜色
        # pcobj.paint_uniform_color([1, 0, 0])
        # 可视化
        # vis.update_geometry(pcobj)
        # vis.add_geometry(pcobj)
        # 使用下列方法将视角变为自由模式，可以通过拖动和滚轮调整视角。
        if pcobj.is_empty():
            pcobj.points = o3d.utility.Vector3dVector(pcs[:, 0:3])
            vis.add_geometry(pcobj)
        else:
            pcobj.points = o3d.utility.Vector3dVector(pcs[:, 0:3])
            vis.update_geometry(pcobj)

        # 鼠标变换视角
        if to_reset:
            vis.reset_view_point(True)
            to_reset = False
        # 添加box========================================================================
        # 找到box
        txt_path = "/home/hcq/pointcloud/Point-Clouds-Visualization/data_test/predict/livox"
        path = file.split('.')[0]
        txt_file = "%s/%s.txt"%(txt_path, path) #
        with open(txt_file, 'r') as f: #
            lines = f.readlines() # 打开文件
        boxes = [line.strip().split(' ') for line in lines]  # GT内容
        for d in boxes:
            # xyz = np.array([d[1: 4]])
            # hwl = np.array([d[4: 7]])
            xyz = np.array([list(map(float, d[1: 4]))])
            hwl = np.array([list(map(float, d[4: 7]))])
            r_y = [float(d[7])] # 转成数字
            id = [d[0]] # 目前不用
            pts3d = compute_3d_box_lidar_coords(xyz, hwl, angles=r_y, origin=(0.5, 0.5, 0.5), axis=2)
            lines = [[0, 1], [1, 2], [2, 3], [3, 0],
                     [4, 5], [5, 6], [6, 7], [7, 4],
                     [0, 4], [1, 5], [2, 6], [3, 7]]
            colors = [[1, 0, 1] for i in range(len(lines))]
            line_set = o3d.geometry.LineSet()
            # 要画线的话，需要定义Lineset和创造一组点还有一组边。边是一对点的索引。
            # line_set.points = o3d.utility.Vector3dVector(pts3d[0]) # 点
            # line_set.lines = o3d.utility.Vector2iVector(lines)
            # line_set.colors = o3d.utility.Vector3dVector(colors)
            # vis.add_geometry(line_set)
            # 将视角变为自由模式，可以通过拖动和滚轮调整视角。
            if line_set.has_lines():
                line_set.points = o3d.utility.Vector3dVector(pts3d[0]) # 点
                line_set.lines = o3d.utility.Vector2iVector(lines)
                line_set.colors = o3d.utility.Vector3dVector(colors)
                vis.update_geometry(line_set) #
            else:
                line_set.points = o3d.utility.Vector3dVector(pts3d[0]) # 点
                line_set.lines = o3d.utility.Vector2iVector(lines)
                line_set.colors = o3d.utility.Vector3dVector(colors)
                vis.add_geometry(line_set)

        # loop end
        vis.poll_events()
        vis.update_renderer()
        # 设置休眠时间
        time.sleep(0.5)
    print("vis end")
    # vis.destroy_window()


if __name__ == '__main__':
    draw_points_with_boxes()