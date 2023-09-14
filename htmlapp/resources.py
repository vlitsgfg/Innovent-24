from import_export import resources
from .models import Students
class StudentsResource(resources.ModelResource):
    class meta:
        model=Students