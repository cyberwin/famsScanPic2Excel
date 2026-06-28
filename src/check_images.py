from PIL import Image
import os
import sys

def check_images(image_folder, image_list=None):
    """
    动态检测扫描图片合法性，无固定路径，适配技能参数调用
    :param image_folder: 动态传入的扫描件文件夹路径
    :param image_list: 指定检测图片列表，为空则遍历全部
    :return: 有效图片文件列表
    """
    # 校验文件夹是否存在
    if not os.path.exists(image_folder):
        print(f"[错误] 文件夹不存在: {image_folder}")
        return []

    # 未传入图片列表，自动遍历文件夹所有图片
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
    if not image_list:
        image_list = [f for f in os.listdir(image_folder) 
                      if os.path.splitext(f)[1].lower() in image_extensions]

    valid_images = []
    for img_name in image_list:
        img_path = os.path.join(image_folder, img_name)
        try:
            img = Image.open(img_path)
            print(f"[正常] {img_name}: 尺寸={img.size}, 格式={img.format}, 模式={img.mode}")
            valid_images.append(img_path)
        except Exception as e:
            print(f"[异常] {img_name}: 读取失败 - {e}")

    print(f"\n[检测完成] 有效图片数量: {len(valid_images)}")
    return valid_images

# 技能入口：接收外部动态参数，无固定路径
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python check_images.py 扫描件文件夹路径")
        sys.exit(1)
    target_folder = sys.argv[1]
    check_images(target_folder)
