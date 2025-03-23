dataset_type = 'NuScenes3DDetTrackDataset'
# 确保在所有配置中添加
train_pipeline = [
    # 其他参数...
    dict(
        type='FormatRelativeBundle3DTrack',
        with_relative_velocity=True,
    ),
    # 其他参数...
] 