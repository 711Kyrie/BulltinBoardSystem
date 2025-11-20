from django.db import models
from lib import BaseModel
# Create your models here.
# 个人站点标配
class Blog(BaseModel):
    site_name = models.CharField(verbose_name="站点名称", help_text="站点名称", max_length=32)
    site_title = models.CharField(verbose_name="站点标题", help_text="站点标题", max_length=32)
    site_theme = models.CharField(verbose_name="站点样式", help_text="站点样式", max_length=64)  # css/js的文件路径