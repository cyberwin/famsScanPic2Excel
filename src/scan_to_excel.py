#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扫描件转Excel工具
famsScanPic2Excel 核心脚本
将扫描的图片文件夹批量识别表格并导出为标准可编辑Excel
适配技能动态传参，无固定路径
"""

import os
import sys
from pathlib import Path

def process_scan_folder(input_folder, output_path):
    """
    处理扫描件文件夹，将图片转换为Excel
    
    Args:
        input_folder: 输入文件夹路径
        output_path: 输出Excel文件路径
    """
    # 检查输入文件夹
    if not os.path.exists(input_folder):
        print(f"错误：输入文件夹不存在 - {input_folder}")
        return False
    
    # 获取所有图片文件
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
    image_files = []
    
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in image_extensions:
                image_files.append(file_path)
    
    if not image_files:
        print(f"警告：输入文件夹中没有找到图片文件")
        return False
    
    print(f"✅ 找到 {len(image_files)} 个有效扫描图片文件")

    # 后续可扩展 OCR 表格识别核心逻辑
    print("\n=== famsScanPic2Excel 转换引擎 ===")
    print(f"📂 输入文件夹: {input_folder}")
    print(f"📤 输出路径: {output_path}")
    print(f"📄 待处理文件列表:")
    for img in image_files:
        print(f"  - {os.path.basename(img)}")

    print("\n💡 提示：OCR表格识别模块待完善，请确保依赖库已安装")
    print("📦 依赖安装命令：pip install pytesseract opencv-python pandas openpyxl Pillow")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python scan_to_excel.py <输入文件夹> <输出Excel路径>")
        print("示例: python scan_to_excel.py ./scan_folder ./output.xlsx")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_path = sys.argv[2]

    process_scan_folder(input_folder, output_path)
