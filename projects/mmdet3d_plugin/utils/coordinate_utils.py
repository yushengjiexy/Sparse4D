def get_ego_to_ego_transform(src_info, dst_info):
    """计算两帧之间自车坐标系的变换矩阵"""
    # 从 src 自车坐标系到全局坐标系的变换
    src_l2e_r = src_info["lidar2ego_rotation"]
    src_l2e_t = src_info["lidar2ego_translation"]
    src_e2g_r = src_info["ego2global_rotation"]
    src_e2g_t = src_info["ego2global_translation"]
    
    # 从 dst 自车坐标系到全局坐标系的变换
    dst_l2e_r = dst_info["lidar2ego_rotation"]
    dst_l2e_t = dst_info["lidar2ego_translation"]
    dst_e2g_r = dst_info["ego2global_rotation"]
    dst_e2g_t = dst_info["ego2global_translation"]
    
    # 计算全局坐标系到 dst 自车坐标系的变换
    dst_g2e_r = pyquaternion.Quaternion(dst_e2g_r).inverse
    dst_g2e_t = -np.array(dst_e2g_t)
    dst_g2e_t = dst_g2e_r.rotation_matrix @ dst_g2e_t
    
    # 省略部分中间计算...
    
    # src自车坐标系 -> 全局坐标系 -> dst自车坐标系
    src2dst = dst_g2e @ src_e2g
    
    return src2dst 