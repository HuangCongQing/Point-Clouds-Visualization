'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-27 10:10:06
LastEditTime: 2021-04-27 10:10:06
FilePath: /Point-Clouds-Visualization/2open3D/Open3d学习计划/02使用帮助与IO/02IO.py
'''
'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-27 10:10:06
LastEditTime: 2021-04-27 10:10:06
FilePath: /Point-Clouds-Visualization/2open3D/Open3d学习计划/02使用帮助与IO/02IO.py
'''
# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %% [markdown]
# ## 文件IO
# 这一节将会介绍基本几何图形的读取和写入
# 
# 
# %% [markdown]
# ##  点云（pcd txt）

# %%
import open3d as o3d   #导入open3d
print("Testing IO for point cloud ...")
pcd = o3d.io.read_point_cloud("/home/hcq/python/Point-Clouds-Visualization/2open3D/data/merge_with_pedestrian1.pcd") # 读取
print(pcd)
# o3d.io.write_point_cloud("copy_merge_with_pedestrian1.pcd", pcd) # 写入

# %% [markdown]
# ## 网格（Mesh） ply

# %%
import open3d as o3d   #导入open3d

print("Testing IO for meshes ...")
mesh = o3d.io.read_triangle_mesh("/home/hcq/python/Point-Clouds-Visualization/2open3D/data/conferenceRoom_1_GT.ply")
print(mesh)
# o3d.io.write_triangle_mesh("copy_of_conferenceRoom_1_GT.ply",mesh)

# %% [markdown]
# ## 图像（Image）
# 
# 不支持png

# %%
import open3d as o3d   #导入open3d

print("Testing IO for images ...")
img = o3d.io.read_image("/home/hcq/python/Point-Clouds-Visualization/2open3D/data/cat.jpg")
print(img)
o3d.io.write_image("copy.jpg", img)


# %%



