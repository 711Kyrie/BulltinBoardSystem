from django.db import models
from lib import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser, BaseModel):
    # 继承AbstractUser类
    # 继承BaseModel类 
    # 扩展字段 电话
    phone = models.CharField(max_length=11, verbose_name="手机号", null=True, blank=True)
    # 扩展字段 头像
    avatar = models.CharField(max_length=32, verbose_name="用户头像",default="static/avatar/default.png")
    # 逻辑删除
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    # 关联个人站点的外键字段
    blog = models.OneToOneField(verbose_name="一对一关联个人站点",)
    class Meta:
        # 单数形式的模型名称，用于后台显示
        verbase_name = "用户信息表"
        # 复数形式的模型名称，用于后台显示
        verbase_name_plural = "用户信息表"
        db_table = "user"
    def __str__(self):
        return self.username    