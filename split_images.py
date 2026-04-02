#!/usr/bin/env python3
"""
拆分消融实验图表为独立子图
"""

from PIL import Image
import os

# 创建输出目录
output_dir = "images/split"
os.makedirs(output_dir, exist_ok=True)

def split_barlow_metrics():
    """Barlow Twins 指标 - 7个子图 (4+3布局)"""
    img = Image.open("images/ablation_barlow_metrics.png")
    w, h = img.size
    print(f"Barlow metrics: {w}x{h}")
    
    # 计算网格 (第一行4个，第二行3个)
    # 估计每个子图的大小和间距
    # 第一行: 4个图
    # 第二行: 3个图 (居中)
    
    # 估算每个子图区域 (包含padding)
    cell_w = w // 4
    cell_h = h // 2
    
    # 子图名称
    names = [
        "bt_cosine_sim", "bt_effective_rank", "bt_latent_std_mean", "bt_latent_std_min",
        "bt_off_diag", "bt_on_diag", "bt_priv_pred"
    ]
    
    positions = [
        (0, 0), (cell_w, 0), (cell_w*2, 0), (cell_w*3, 0),  # 第一行
        (cell_w//2, cell_h), (cell_w*1 + cell_w//2, cell_h), (cell_w*2 + cell_w//2, cell_h)  # 第二行 (居中)
    ]
    
    for i, (name, (x, y)) in enumerate(zip(names, positions)):
        # 裁剪区域 (稍微缩小以去除边框)
        margin_x = 10
        margin_y = 10
        crop_box = (x + margin_x, y + margin_y, 
                   min(x + cell_w - margin_x, w), 
                   min(y + cell_h - margin_y, h))
        sub_img = img.crop(crop_box)
        sub_img.save(f"{output_dir}/{name}.png")
        print(f"  Saved: {name}.png ({sub_img.size[0]}x{sub_img.size[1]})")

def split_reward_group_1():
    """Reward Group 1 - 3个子图 (水平并排)"""
    img = Image.open("images/ablation_reward_group_1.png")
    w, h = img.size
    print(f"Reward group 1: {w}x{h}")
    
    names = ["rg1_joint_acc_wheel", "rg1_joint_power", "rg1_no_contact"]
    cell_w = w // 3
    
    for i, name in enumerate(names):
        x = i * cell_w
        margin = 5
        crop_box = (x + margin, margin, min(x + cell_w - margin, w), h - margin)
        sub_img = img.crop(crop_box)
        sub_img.save(f"{output_dir}/{name}.png")
        print(f"  Saved: {name}.png ({sub_img.size[0]}x{sub_img.size[1]})")

def split_reward_group_2():
    """Reward Group 2 - 3个子图 (水平并排)"""
    img = Image.open("images/ablation_reward_group_2.png")
    w, h = img.size
    print(f"Reward group 2: {w}x{h}")
    
    names = ["rg2_action_rate", "rg2_ang_vel_xy", "rg2_base_height"]
    cell_w = w // 3
    
    for i, name in enumerate(names):
        x = i * cell_w
        margin = 5
        crop_box = (x + margin, margin, min(x + cell_w - margin, w), h - margin)
        sub_img = img.crop(crop_box)
        sub_img.save(f"{output_dir}/{name}.png")
        print(f"  Saved: {name}.png ({sub_img.size[0]}x{sub_img.size[1]})")

def split_reward_group_3():
    """Reward Group 3 - 5个子图 (上3下2)"""
    img = Image.open("images/ablation_reward_group_3.png")
    w, h = img.size
    print(f"Reward group 3: {w}x{h}")
    
    # 上排3个，下排2个(居中)
    cell_w = w // 3
    cell_h = h // 2
    
    names = [
        "rg3_track_ang_vel_z", "rg3_track_lin_vel_xy", "rg3_undesired_contacts",
        "rg3_wheel_body_speed", "rg3_wheel_vel_penalty"
    ]
    
    positions = [
        (0, 0), (cell_w, 0), (cell_w*2, 0),  # 上排
        (cell_w//2, cell_h), (cell_w + cell_w//2, cell_h)  # 下排 (居中)
    ]
    
    for name, (x, y) in zip(names, positions):
        margin = 5
        crop_box = (x + margin, y + margin, 
                   min(x + cell_w - margin, w), 
                   min(y + cell_h - margin, h))
        sub_img = img.crop(crop_box)
        sub_img.save(f"{output_dir}/{name}.png")
        print(f"  Saved: {name}.png ({sub_img.size[0]}x{sub_img.size[1]})")

def copy_terrain_levels():
    """复制 terrain levels (单图)"""
    img = Image.open("images/ablation_terrain_levels.png")
    img.save(f"{output_dir}/terrain_levels.png")
    print(f"Copied: terrain_levels.png ({img.size[0]}x{img.size[1]})")

if __name__ == "__main__":
    print("="*50)
    print("拆分消融实验图表")
    print("="*50)
    
    copy_terrain_levels()
    split_barlow_metrics()
    split_reward_group_1()
    split_reward_group_2()
    split_reward_group_3()
    
    print("="*50)
    print(f"所有子图已保存到: {output_dir}/")
    print("="*50)
