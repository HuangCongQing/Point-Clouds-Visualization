''' 
***point cloud lectern***
=========memo 1=========

       ╰(●’◡’●)╮

to show point cloud for classification task.
take data_whu and data_isprs as examples.
========2019.12.9========
'''
from __future__ import print_function

import os
import sys
import numpy as np
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'mayavi'))

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


class pointcloud_object(object):
    '''Load and parse object data into a usable format.'''
    
    def __init__(self, root_dir):

        self.lidar_dir = root_dir

    def get_lidar(self, idx): 
        # assert(idx<data_num) 
        lidar_filename = os.path.join(self.lidar_dir, '%03d.txt'%(idx))#bin
        return load_velo_scan(lidar_filename)

def load_velo_scan(velo_filename):
    scan = np.loadtxt(velo_filename)
    print('the shape of scan is: ', scan.shape)
    return scan


def draw_lidar(pc, fig=None, bgcolor=(0,0,0), pts_scale=1, pts_mode='point', pts_color=None):
    ''' Draw lidar points
    Args:
        pc: numpy array (n,3) of XYZ
        fig: mayavi figure handler, if None create new one otherwise will use it
    Returns:
        fig: created or used fig
    '''

    if fig is None: fig = mlab.figure(figure=None, bgcolor=bgcolor, fgcolor=None, engine=None, size=(1600, 1000))
#       category  label   r   g   b
#       vegetation  0   0   255 0
#       building    1   255 0   0
#       car         2   0   0   255
#       pedestrian  3   255 255 0
#       lamp        4   255 97  0
#       fence       5   155 74  18
#       others      6   106 90  205
    color_list = [(0, 1, 0),
                  (1, 0, 0),
                  (0, 0, 1),
                  (1, 1, 0), 
                  (1, 97/255, 0),
                  (155/255, 97/255, 18/255),
                  (0, 1, 1),
                  (106/255, 90/255, 205/255)]

    without_semantic_label = True#False#              

    if without_semantic_label:
        mlab.points3d(pc[:,0], pc[:,1], pc[:,2], color=color_list[0], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig)

    else:
        # pc0_mask = pc[:,3]==0
        # pc1_mask = pc[:,3]==1
        # pc2_mask = pc[:,3]==2
        # pc3_mask = pc[:,3]==3
        # pc4_mask = pc[:,3]==4
        # pc5_mask = pc[:,3]==5
        # pc6_mask = pc[:,3]==6
        pc0 = pc[pc[:,3]==0]
        pc1 = pc[pc[:,3]==1]
        pc2 = pc[pc[:,3]==2]
        pc3 = pc[pc[:,3]==3]
        pc4 = pc[pc[:,3]==4]
        pc5 = pc[pc[:,3]==5]
        pc6 = pc[pc[:,3]==6]
        print('136: the size of pc0 is:', len(pc0))
        print('136: the size of pc1 is:', len(pc1))
        print('136: the size of pc2 is:', len(pc2))
        print('136: the size of pc3 is:', len(pc3))
        print('136: the size of pc4 is:', len(pc4))
        print('136: the size of pc5 is:', len(pc5))
        print('136: the size of pc6 is:', len(pc6))

        mlab.points3d(pc0[:,0], pc0[:,1], pc0[:,2],  color=color_list[0], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
        mlab.points3d(pc1[:,0], pc1[:,1], pc1[:,2],  color=color_list[1], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
        mlab.points3d(pc2[:,0], pc2[:,1], pc2[:,2],  color=color_list[2], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
        mlab.points3d(pc3[:,0], pc3[:,1], pc3[:,2],  color=color_list[3], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
        mlab.points3d(pc4[:,0], pc4[:,1], pc4[:,2],  color=color_list[4], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
        mlab.points3d(pc5[:,0], pc5[:,1], pc5[:,2],  color=color_list[5], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
        mlab.points3d(pc6[:,0], pc6[:,1], pc6[:,2],  color=color_list[6], mode=pts_mode, colormap = 'gnuplot', scale_factor=pts_scale, figure=fig) 
    
    
    # mlab.view(azimuth=180, elevation=90, focalpoint=[ 12.0909996 , -1.04700089, -2.03249991], distance=62.0, figure=fig)
    mlab.view(azimuth=270, elevation=0, focalpoint=[ pc[0,0], pc[0,1], pc[0,2]], distance=10.0, figure=fig)
    return fig

def show_lidar(pc_velo, img_fov=False): 
    ''' Show all LiDAR points.
        Draw 3d box in LiDAR point cloud (in velo coord system) '''
    if 'mlab' not in sys.modules: import mayavi.mlab as mlab

    print(('All point num: ', pc_velo.shape[0]))
    fig = mlab.figure(figure=None, bgcolor=(1,1,1),
        fgcolor=None, engine=None, size=(1000, 500))
    
    draw_lidar(pc_velo, fig=fig)

    mlab.show(1)


def dataset_viz():
    dataset = pointcloud_object(os.path.join(ROOT_DIR, 'data-whu'))
    # dataset = pointcloud_object(os.path.join(ROOT_DIR, 'data-isprs'))
    print('143:', dataset)
    data_num = 10

    for data_idx in range(data_num):

        pc_velo = dataset.get_lidar(data_idx)[:,0:4]
        print('the len of dataset is: ', data_num, 'data_idx is: ', data_idx)

        show_lidar(pc_velo, False)
        raw_input()

if __name__=='__main__':
    import mayavi.mlab as mlab
    # from viz_util import draw_lidar_simple, draw_lidar, draw_gt_boxes3d
    dataset_viz()
