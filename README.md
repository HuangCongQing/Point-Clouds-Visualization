<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2020-11-16 11:21:14
 * @LastEditTime: 2023-08-04 23:24:46
 * @FilePath: /Point-Clouds-Visualization/README.md
-->
![image](https://user-images.githubusercontent.com/20675770/188302348-2a278d02-73d5-4e2f-9b82-62f7471eb8ae.png)


# Point-Clouds-Visualization

点云可视化

@[双愚](https://github.com/HuangCongQing) , 若fork或star请注明来源

## Visualization可视化

- open3D [`python`]
- mayavi[`python`]
- matplolib [`python`]
- rviz(ROS) topic可视化  [`c++`][`python`]
- pcl 点云可视化 [`c++`]： [pcl-visualization可视化](https://github.com/HuangCongQing/pcl-learning/tree/master/15visualization%E5%8F%AF%E8%A7%86%E5%8C%96)

可视化软件：cloudcompare （windows&Ubuntu）

个人笔记：https://www.yuque.com/huangzhongqing/hre6tf/eak3ba

```
# 克隆包含子仓库：https://github.com/chaomath/open3d-kitti-visualization
git clone --recursive https://github.com/HuangCongQing/Point-Clouds-Visualization
```


### 1 mayavi

参考自：

* https://www.bilibili.com/video/BV1zJ41167qx?
* https://github.com/liminle/point-cloud-lectern-memos

语义分割任务 classification task

* code： [showpc_memo1](1mayavi/visualizer/showpc_memo1.py)
* data：[1mayavi/data-whu](1mayavi/data-whu)
  * 链接: https://pan.baidu.com/s/11EvyY71Y2qrHz5BXodDi3w 提取码: w9ar

目标检测跟踪任务  detection and tracking task

* code：[showpc_memo2](1mayavi/visualizer/showpc_memo2.py)
* data：[1mayavi/showpc/isprs_frames0/training](1mayavi/showpc/isprs_frames0/training)

### 2 Open3D

https://www.yuque.com/huangzhongqing/hre6tf/xk0gxn

* [2open3D/Open3d学习计划](2open3D/Open3d学习计划)
* [读取txt/ply文件](2open3D)

#### open3d实战项目
* [open3d-kitti-visualization](2open3D/practice/open3d-kitti-visualization)
  * ref:https://github.com/chaomath/open3d-kitti-visualization
* [01kitti_pc](2open3D/practice/01kitti_pc)
* [02kitti_pc&box](2open3D/practice/02kitti_pc&box)
* ...

##### 子仓库代码bug:运行子仓库代码需要修改
* [open3d-kitti-visualization](2open3D/practice/open3d-kitti-visualization)

修改文件：2open3D/practice/open3d-kitti-visualization/open3d_geometry/open3d_arrow.py

```python
	# mesh.transform(T)
	# mesh.rotate([0,beta,0],center=False) # TypeError: rotate(): incompatible function arguments. The following argument types are supported:
	# mesh.rotate([0,0,gamma],center=False)
	# fix:w维度不对 np.expand_dims(np.array([0,beta,0], dtype=np.float64),1).shape
	mesh.rotate(mesh.get_rotation_matrix_from_xyz((0,beta,0)), center=mesh.get_center())
	mesh.rotate(mesh.get_rotation_matrix_from_xyz((0,0,gamma)), center=mesh.get_center())

```



### 4 ros2_python [`python`]


python版本: ubuntu20.04 ，ROS foxy版本

#### vis  points&bbox

*  [3ros2_python/vis_ros2.ipynb](3ros2_python/vis_ros2.ipynb)



### 5 ros1_cpp [`c++`]

> 5ros1_cpp/src/lidar_visualization
#### feat1: 遍历文件夹里的文件（pcd或者ply格式）可视化点云和对应文件名字

```shell
# 编译
catkin_make

# 运行
## 方式1
rosrun lidar_visualization lidars_visualization

## 方式2
roslaunch lidar_visualization test.launch

```


## References

* [Semantic-Segmentation-of-Point-Clouds](https://github.com/HuangCongQing/Semantic-Segmentation-of-Point-Clouds)
* [SLAM](https://github.com/HuangCongQing/SLAM)
* [pcl](https://github.com/HuangCongQing/pcl-learning)

## License

Copyright (c) [双愚](https://github.com/HuangCongQing/). All rights reserved.

Licensed under the [MIT](./LICENSE) License.
