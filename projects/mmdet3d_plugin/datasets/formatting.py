@PIPELINES.register_module()
class FormatRelativeBundle3DTrack(object):
    """将预处理结果转换为模型所需的格式"""
    
    def __init__(
        self,
        with_gt=True,
        with_label=True,
        with_track_id=True,
        with_relative_velocity=True,  # 添加标志
    ):
        self.with_gt = with_gt
        self.with_label = with_label
        self.with_track_id = with_track_id
        self.with_relative_velocity = with_relative_velocity
    
    def __call__(self, results):
        # 处理gt_bboxes_3d
        if self.with_gt and 'gt_bboxes_3d' in results:
            # 确保所有速度是相对速度
            if self.with_relative_velocity and 'ego_velocity' in results:
                ego_vel = results['ego_velocity']
                gt_bboxes_3d = results['gt_bboxes_3d']
                
                # 如果输入中有绝对速度，需要转换为相对速度
                if hasattr(gt_bboxes_3d, 'tensor') and gt_bboxes_3d.tensor.shape[-1] > 7:
                    vel_start_idx = 7
                    # 将绝对速度转换为相对速度
                    gt_bboxes_3d.tensor[:, vel_start_idx:vel_start_idx+2] -= torch.tensor(
                        ego_vel[:2], device=gt_bboxes_3d.tensor.device)
        
        # 现有的格式化代码保持不变...
        return results 