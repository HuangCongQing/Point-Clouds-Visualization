'''
Description: 可视化原始点云 https://www.yuque.com/huangzhongqing/ld627o/gulyke
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-09-05 21:39:27
LastEditTime: 2022-09-05 22:09:46
FilePath: /Point-Clouds-Visualization/3ros2_python/01vis_pointcloud.py
'''
# Copyright 2020 Evan Flynn
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
import numpy as np
 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Header
 
 
class PointCloudPublisher(Node):
 
    rate = 30
    moving = True
    width = 100
    height = 100
 
    header = Header()
    header.frame_id = 'map'
 
    dtype = PointField.FLOAT32
    point_step = 16
    fields = [PointField(name='x', offset=0, datatype=dtype, count=1),
              PointField(name='y', offset=4, datatype=dtype, count=1),
              PointField(name='z', offset=8, datatype=dtype, count=1),
              PointField(name='intensity', offset=12, datatype=dtype, count=1)]
    
    # 初始化的时间时候
    def __init__(self):
        super().__init__('pc_publisher')
        self.publisher_ = self.create_publisher(PointCloud2, '/raw_cloud', 10) # 自定义
        timer_period = 1 / self.rate
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0
 
    def timer_callback(self):
        self.header.stamp = self.get_clock().now().to_msg()
        # 1 生成点云
        ## 波浪曲面点云 
        # x, y = np.meshgrid(np.linspace(-2, 2, self.width), np.linspace(-2, 2, self.height))
        # z = 0.5 * np.sin(2*x-self.counter/10.0) * np.sin(2*y)
        # points = np.array([x, y, z, z]).reshape(4, -1).T # 原始点云
        ## 随机生成点云
        # points = np.random.randint(0, 5, size=(10000,4)) # 整数
        # points = np.linspace(0, 5, size=(10000,4)) # 整数
        points = np.random.randn(1000,4)*50 # （0,1）且该数服从标准正太分布


        print(points.shape, points[:5, :]) # (10000, 4)
        # 2得到msg
        pc2_msg = point_cloud2.create_cloud(self.header, self.fields, points) # 生成点云
        # 3 publish发布
        self.publisher_.publish(pc2_msg) # 发布msg
 
        if self.moving:
            self.counter += 1
 
 
def main(args=None):
    rclpy.init(args=args)
    pc_publisher = PointCloudPublisher() # 初始化的时候就执行init（）
    rclpy.spin(pc_publisher)
    pc_publisher.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()