from django.contrib import admin

from .models import (
    Services,
    Ministries,
    Problem,
    Region,
)
# Register your models here.

admin.site.register(Services)
admin.site.register(Ministries)
admin.site.register(Problem)
admin.site.register(Region)