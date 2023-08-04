#include <ros/ros.h>
#include <pcl/io/pcd_io.h>
#include <pcl/io/ply_io.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>
#include <sensor_msgs/PointCloud2.h>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <string>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "pcd_visualization");
    ros::NodeHandle nh;

    // PCD/PLY 文件夹路径
    std::string pc_dir = "/home/hcq/project/board检测/ws_board/src/board_detection/testdata"; // 替换为您的PCD或PLY文件目录的路径

    // PointCloud2 消息的发布者
    ros::Publisher pub = nh.advertise<sensor_msgs::PointCloud2>("pcd", 1);

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

            // 将PCL点云转换为ROS PointCloud2消息
            sensor_msgs::PointCloud2 msg;
            pcl::toROSMsg(*cloud, msg);
            msg.header.frame_id = "map"; // 设置在RViz中可视化时的坐标系

            // 发布PointCloud2消息
            pub.publish(msg);

            // 等待一小段时间
            ros::Duration(0.5).sleep();
        }

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
