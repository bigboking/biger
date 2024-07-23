# import os
# from PIL import Image
#
#
# def convert_png_to_jpg(directory):
#     # 遍历目录中的所有文件
#     for filename in os.listdir(directory):
#         # 检查文件是否为 PNG 格式
#         if filename.endswith(".png"):
#             # 构造完整文件路径
#             png_file = os.path.join(directory, filename)
#             # 构造 JPG 文件路径
#             jpg_file = os.path.join(directory, filename[:-4] + ".jpg")
#
#             # 打开 PNG 文件并转换为 RGB 模式
#             with Image.open(png_file) as img:
#                 rgb_img = img.convert("RGB")
#                 # 保存为 JPG 文件
#                 rgb_img.save(jpg_file, "JPEG")
#
#             # 打印转换信息
#             print(f"Converted {png_file} to {jpg_file}")
#
#
# # 定义目标目录
# target_directory = r"D:\cx\24.5.15\test-4\pythonProject1\.venv\Scripts\unet-pytorch\VOCdevkit\VOC2007\JPEGImages"
#
# # 调用转换函数
# convert_png_to_jpg(target_directory)
# import os
#
# def delete_png_files(directory):
#     # 遍历目录中的所有文件
#     for filename in os.listdir(directory):
#         # 检查文件是否为 PNG 格式
#         if filename.endswith(".png"):
#             # 构造完整文件路径
#             png_file = os.path.join(directory, filename)
#             # 删除 PNG 文件
#             os.remove(png_file)
#             # 打印删除信息
#             print(f"Deleted {png_file}")
#
# # 定义目标目录
# target_directory = r"D:\cx\24.5.15\test-4\pythonProject1\.venv\Scripts\unet-pytorch\VOCdevkit\VOC2007\JPEGImages"
#
# # 调用删除函数
# delete_png_files(target_directory)
import torch
print(torch.__version__)
print(torch.cuda.is_available())
