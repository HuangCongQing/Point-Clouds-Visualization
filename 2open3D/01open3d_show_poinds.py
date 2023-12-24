'''
Description: open3D显示点云 https://blog.csdn.net/weixin_41281151/article/details/107119326
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-06 17:46:00
LastEditTime: 2023-12-25 00:11:08
FilePath: /Point-Clouds-Visualization/2open3D/01open3d_show_poinds.py
'''

import open3d as o3d 
import numpy as np


# 参考https://blog.csdn.net/weixin_53610475/article/details/128188372
def vis_with_mesh_file(path_obj):
    #模型路径，支持后缀：stl/ply/obj/off/gltf/glb
    # path_obj = 'Rmk3.obj'
    #读入网格模型
    mesh = o3d.io.read_triangle_mesh(path_obj)
    #计算网格顶点
    mesh.compute_vertex_normals()
    #可视化网格模型
    o3d.visualization.draw_geometries([mesh])


def vis_points(path):
    np_pc = np.random.random((1000,3)) # 生成随机点np.random.random((1000,3))

    pc_view = o3d.geometry.PointCloud()
    pc_view.points = o3d.utility.Vector3dVector(np_pc) # 转类型？
    
    o3d.visualization.draw_geometries([pc_view]) # 可视化


def main():
    path_obj = "/home/hcq/pointcloud/Point-Clouds-Visualization/2open3D/data/obj/FinalBaseMesh.obj"
    vis_with_mesh_file(path_obj)


if __name__ == "__main__":
    main()
