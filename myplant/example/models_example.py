'''
from django.db import models
from myplant.models import NewModel, create_all_db


class Course(NewModel):
    name = models.CharField('名稱', unique=True, max_length=100, default='')

    class Meta:
        abstract = True
        verbose_name = '課程'


class CourseContent(NewModel):
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE, default='')
    content = models.TextField('內容', default='', blank=True)

    class FK:
        courseid = Course

    class Meta:
        abstract = True
        verbose_name = '課程-學習資源'


MODELS = [Course, CourseContent]
create_all_db(MODELS)
'''