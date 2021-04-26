'''
Description: open3D显示点云 https://blog.csdn.net/weixin_41281151/article/details/107119326
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-06 17:46:00
LastEditTime: 2021-04-26 09:51:51
FilePath: /Point-Clouds-Visualization/2open3D/01open3d_show_poinds.py
'''

import open3d as o3d 
import numpy as np

def main():
    np_pc = np.random.random((1000,3))
    pc_view = o3d.geometry.PointCloud()
    pc_view.points = o3d.utility.Vector3dVector(np_pc)
    o3d.visualization.draw_geometries([pc_view])

if __name__ == "__main__":
    main()
