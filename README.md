<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2020-11-16 11:21:14
 * @LastEditTime: 2022-05-06 12:32:05
 * @FilePath: /Point-Clouds-Visualization/README.md
-->

# Point-Clouds-Visualization

点云可视化

@[双愚](https://github.com/HuangCongQing) , 若fork或star请注明来源

## Visualization可视化

- pcl 点云可视化 [`c++`]
- rviz(ROS) topic可视化  [`c++`][`python`]
- open3D [`python`]
- mayavi[`python`]
- matplolib [`python`]

可视化软件：cloudcompare （windows&Ubuntu）

个人笔记：https://www.yuque.com/huangzhongqing/hre6tf/eak3ba

```
# 克隆包含子仓库：https://github.com/chaomath/open3d-kitti-visualization
git clone --recursive https://github.com/HuangCongQing/Point-Clouds-Visualization
```


### mayavi

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

### Open3D

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

## References

* [Semantic-Segmentation-of-Point-Clouds](https://github.com/HuangCongQing/Semantic-Segmentation-of-Point-Clouds)
* [SLAM](https://github.com/HuangCongQing/SLAM)
* [pcl](https://github.com/HuangCongQing/pcl-learning)

## License

Copyright (c) [双愚](https://github.com/HuangCongQing/). All rights reserved.

Licensed under the [MIT](./LICENSE) License.
