_base_ = [
    '../_base_/models/mobilenet_v2_1x.py',
    '../_base_/datasets/sss_fruit_cls.py',
    '../_base_/schedules/imagenet_bs256_epochstep.py',
    '../_base_/default_runtime.py'
]
