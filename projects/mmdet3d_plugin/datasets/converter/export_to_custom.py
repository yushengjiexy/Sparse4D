import json

def convert_to_custom_format(results, data_infos, output_path, use_relative_coordinates=True):
    """导出到自定义格式，支持相对坐标系"""
    
    custom_results = []
    for idx, result in enumerate(results):
        sample_info = data_infos[idx]
        boxes = result['boxes_3d']
        scores = result['scores_3d']
        labels = result['labels_3d']
        
        custom_boxes = []
        for i in range(len(boxes)):
            box_dict = {
                'position': boxes[i, :3].tolist(),
                'dimensions': boxes[i, 3:6].tolist(),
                'yaw': float(boxes[i, 6]),
                'label': int(labels[i]),
                'score': float(scores[i]),
            }
            
            # 处理速度信息
            if boxes.shape[1] > 7:
                # 默认使用相对速度
                velocity = boxes[i, 7:9].tolist()
                
                # 如果需要导出绝对速度
                if not use_relative_coordinates and 'ego_velocity' in sample_info:
                    ego_vel = sample_info['ego_velocity']
                    velocity = [velocity[0] + ego_vel[0], velocity[1] + ego_vel[1]]
                
                box_dict['velocity'] = velocity
                
            custom_boxes.append(box_dict)
            
        frame_result = {
            'token': sample_info['token'],
            'timestamp': sample_info['timestamp'],
            'objects': custom_boxes
        }
        
        custom_results.append(frame_result)
    
    # 如果需要导出全局坐标系下的结果，在这里转换
    if not use_relative_coordinates:
        # 转换到全局坐标系
        # 代码...
    
    # 保存结果
    with open(output_path, 'w') as f:
        json.dump(custom_results, f, indent=2) 