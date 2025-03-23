def _format_bbox(self, results, jsonfile_prefix=None):
    # 现有代码...
    
    for sample_id, det in enumerate(mmcv.track_iter_progress(results)):
        # 获取当前帧的信息
        sample_info = self.data_infos[sample_id]
        
        annos = []
        boxes = output_to_nusc_box(det) 
        sample_token = sample_info["token"]
        
        # 转换回全局速度用于评估 (NuScenes评估需要全局速度)
        if hasattr(self, 'use_relative_velocity') and self.use_relative_velocity:
            # 获取ego速度
            ego_velocity = None
            if 'ego_velocity' in sample_info:
                ego_velocity = sample_info['ego_velocity']
            
            # 将相对速度转换回全局速度
            for box in boxes:
                if ego_velocity is not None:
                    # 从相对速度转换回全局速度
                    rel_velocity = box.velocity
                    box.velocity = [rel_velocity[0] + ego_velocity[0], 
                                    rel_velocity[1] + ego_velocity[1]]
        
        # 转换到全局坐标系
        boxes = lidar_nusc_box_to_global(
            sample_info, boxes, self.CLASSES, self.det3d_eval_configs
        )
        
        # 继续已有评估代码... 