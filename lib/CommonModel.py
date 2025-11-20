# -*- coding: Utf-8 -*-
# Time: 2025/11/20
# author: FuTao
# @File : CommonModel.py
# -*- coding: Utf-8 -*-
# Time: 2025/11/20
# author: FuTao
# @File : CommonModel.py
from django.db import models
class BaseModel(models.Model):
    # 创建时间 -- 第一次新增的时候添加
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间 -- 每一次触发更新会更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        # 当前表是一个抽象表
        # 抽象表不会再数据库中创建出真正的表模型
        abstract = True