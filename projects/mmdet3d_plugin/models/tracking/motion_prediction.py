def predict_next_position(self, current_boxes, time_delta):
    """使用相对速度预测下一位置"""
    predicted_boxes = current_boxes.clone()
    
    # 使用相对速度预测
    # 注意：不需要考虑ego的运动，因为我们使用的是相对速度
    if current_boxes.shape[-1] > 7:  # 包含速度
        vel_dims = current_boxes.shape[-1] - 7
        velocity = current_boxes[..., 7:7+vel_dims]
        
        # 根据相对速度计算位移
        displacement = velocity * time_delta
        predicted_boxes[..., :2] += displacement[..., :2]  # 只应用x,y方向的位移
    
    return predicted_boxes 