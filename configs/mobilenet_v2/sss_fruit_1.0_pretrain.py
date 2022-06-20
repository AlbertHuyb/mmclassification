_base_ = [
    '../_base_/models/mobilenet_v2_1x.py',
    '../_base_/datasets/sss_fruit_cls.py',
    '../_base_/schedules/imagenet_bs256_epochstep.py',
    '../_base_/default_runtime.py'
]
model = dict(backbone=dict(
    init_cfg=dict(
        type='Pretrained', checkpoint='/home/zhijie/codes/SonyAI/pretrained/mocov2_sss_mobilenetv2_f01_05_ks_mmseg.pth')),
)
