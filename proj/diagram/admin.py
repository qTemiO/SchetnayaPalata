from django.contrib import admin
from .serializers import ProblemSerializer
from .models import (
    Problem, 
    Ministry, 
    ProblemCluster, 
    Diagram)
    
from loguru import logger

# Register your models here.
class MinistryAdmin(admin.ModelAdmin):
    "Админка министерства"
    list_display = ('name', 'problems_list')

    def problems_list(self, obj):
        seri = ProblemSerializer(obj.problems.all(), many=True)
        return [data['name'] for data in seri.data]


admin.site.register(Problem)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(ProblemCluster)
admin.site.register(Diagram)