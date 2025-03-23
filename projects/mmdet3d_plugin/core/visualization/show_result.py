def draw_velocity_vector(img, bbox, velocity, color=(0, 255, 0), arrow_length_scale=1.0):
    """绘制速度向量
    
    Args:
        img: 图像
        bbox: 2D边界框 [x1, y1, x2, y2]
        velocity: 速度向量 [vx, vy]
        color: 箭头颜色
        arrow_length_scale: 箭头长度缩放系数
    """
    # 计算边界框中心
    center_x = int((bbox[0] + bbox[2]) / 2)
    center_y = int((bbox[1] + bbox[3]) / 2)
    
    # 计算箭头终点 (注意：这是相对速度，直接使用)
    velocity_magnitude = np.sqrt(velocity[0]**2 + velocity[1]**2)
    if velocity_magnitude > 0.5:  # 只绘制足够大的速度
        # 方向是速度方向
        end_x = int(center_x + velocity[0] * arrow_length_scale)
        end_y = int(center_y + velocity[1] * arrow_length_scale)
        
        # 绘制箭头
        cv2.arrowedLine(img, (center_x, center_y), (end_x, end_y), color, 2, tipLength=0.3)
    
    return img 