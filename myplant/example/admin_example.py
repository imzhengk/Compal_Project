'''
from django.contrib import admin
from .models import Course, CourseContent
from myplant.admin import admin_register, admin_register_importexport


register_model = [Course, CourseContent]

# 要显示哪些信息
list_display = {
    'Course'            : ('name', 'department', 'level'),
    'CourseContent'     : ('courseid', 'content', 'summary', 'resource', 'needtime'),
}

# 点击哪些信息可以进入编辑页面
list_display_links = {
    'Course'            : ('name',),
    'CourseContent'     : ('courseid',),
}

# 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
search_fields = {
    'Course'            : ('name',),
}

# 指定列表过滤器，右边将会出现一个快捷的过滤选项
list_filter = {
    'Course'            : ('department', 'level'),
}

# 編輯界面，字段顯示順序
fields = {
}

class Register_Dict:
    list_display = list_display
    list_display_links = list_display_links
    search_fields = search_fields
    list_filter = list_filter
    fields = fields

admin_register(Register_Dict)
'''



'''
# 導入ImportExport模塊
def get_ResourceWorker(plant):
    class Meta:
        model = Worker.get_db(plant)
        fields = ('id', 'name', 'department', 'hiredate')         #要导出的字段
        export_order = ('id', 'name', 'department', 'hiredate')   #导出的字段的排序
    return type(plant+'ResourceWorker', (resources.ModelResource, ), {'Meta': Meta})

admin_register_importexport(Worker, ImportExportModelAdmin, get_ResourceWorker)
'''