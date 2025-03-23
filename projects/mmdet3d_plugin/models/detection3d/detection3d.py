def forward_train(self, points, img_metas, gt_bboxes_3d, gt_labels_3d, **kwargs):
    # 获取相邻帧之间的自车坐标系变换
    ego_transforms = []
    for i in range(1, len(img_metas)):
        src_info = img_metas[i][0]  # 历史帧
        dst_info = img_metas[0][0]  # 当前帧
        # 使用dataset的方法获取自车坐标系变换
        if hasattr(self.dataset, 'get_ego_to_ego_transform'):
            ego_transform = self.dataset.get_ego_to_ego_transform(src_info, dst_info)
        else:
            # 如果数据集没有提供此方法，使用辅助函数计算
            ego_transform = get_ego_to_ego_transform(src_info, dst_info)
        ego_transforms.append(torch.from_numpy(ego_transform).float().to(points[0].device))
    
    # 使用自车坐标系变换代替全局坐标系变换
    # 将transforms传递给模型中需要用到的组件
    # 其他代码... 