#include <ros/ros.h>
#include <pcl/io/pcd_io.h>
#include <pcl/io/ply_io.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>
#include <sensor_msgs/PointCloud2.h>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <visualization_msgs/Marker.h> // 文字信息
#include <string>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "pcd_visualization");
    // 参数设置
    std::string frame_id = "livox_frame";
    std::string lidar_topic = "/livox/lidar";

    // 
    ros::NodeHandle nh;

    // PCD/PLY 文件夹路径
    std::string pc_dir = "/home/hcq/project/board检测/ws_board/src/board_detection/testdata"; // 替换为您的PCD或PLY文件目录的路径

    // PointCloud2 消息的发布者

    // 创建用于PointCloud2消息的ROS发布器
    ros::Publisher cloud_pub = nh.advertise<sensor_msgs::PointCloud2>(lidar_topic, 1);

    // 创建用于Marker消息的ROS发布器
    ros::Publisher marker_pub = nh.advertise<visualization_msgs::Marker>("marker", 1);

    ros::Rate loop_rate(1);

    while (ros::ok())
    {
        // 遍历PCD/PLY文件夹中的所有文件
        for (const auto& file : boost::filesystem::directory_iterator(pc_dir))
        {
            // 获取文件的后缀名
            std::string file_extension = boost::filesystem::extension(file.path());

            // 根据后缀名判断文件类型并加载
            pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);
            if (boost::iequals(file_extension, ".pcd"))
            {
                if (pcl::io::loadPCDFile<pcl::PointXYZ>(file.path().string(), *cloud) == -1)
                {
                    ROS_ERROR_STREAM("无法加载PCD文件: " << file.path().string());
                    continue;
                }
            }
            else if (boost::iequals(file_extension, ".ply"))
            {
                if (pcl::io::loadPLYFile<pcl::PointXYZ>(file.path().string(), *cloud) == -1)
                {
                    ROS_ERROR_STREAM("无法加载PLY文件: " << file.path().string());
                    continue;
                }
            }
            else
            {
                ROS_WARN_STREAM("跳过不支持的文件类型: " << file.path().string());
                continue;
            }

            // 发布点云信息=====================================================
            // 将PCL点云转换为ROS PointCloud2消息
            sensor_msgs::PointCloud2 msg;
            pcl::toROSMsg(*cloud, msg);
            msg.header.frame_id = frame_id; // 设置在RViz中可视化时的坐标系

            // 发布PointCloud2消息
            cloud_pub.publish(msg);

            // 发布文字信息=====================================================
            // 创建一个Marker消息，在RViz中显示文件名
            visualization_msgs::Marker marker;
            marker.header.frame_id = frame_id;
            marker.header.stamp = ros::Time::now();
            marker.ns = "pcd_files";
            marker.id = 0; // 显示多个文字需要不同
            marker.type = visualization_msgs::Marker::TEXT_VIEW_FACING;
            marker.action = visualization_msgs::Marker::ADD;
            marker.pose.orientation.w = 1.0;
            marker.scale.x = 1.0;
            marker.scale.y = 1.0;
            marker.scale.z = 1.0;
            marker.color.a = 1.0;
            marker.color.r = 1.0;
            marker.color.g = 0.0;
            marker.color.b = 0.0;
            marker.pose.position.x = 0.0;
            marker.pose.position.y = 0.0;
            marker.pose.position.z = 5.0;
            marker.lifetime = ros::Duration();
            // 从完整路径中提取文件名
            std::string file_name = file.path().string().substr(file.path().string().find_last_of("/") + 1);
            marker.text = file_name; //<<<<<<<<<<<<<<<<<<<<<<
            // 发布Marker消息
            marker_pub.publish(marker);

            // 等待一小段时间
            ros::Duration(1.0).sleep();
        }

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
