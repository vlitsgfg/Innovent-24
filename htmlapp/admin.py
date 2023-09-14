from django.contrib import admin
from .models import Students,FilesUpload
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Students)
admin.site.register(FilesUpload)
class UserAdmin(ImportExportModelAdmin):
    list_display=('S_id','S_name','S_category','S_totalfee','S_paid','S_due')