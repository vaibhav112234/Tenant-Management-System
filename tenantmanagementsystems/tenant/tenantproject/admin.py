from django.contrib import admin

# Register your models here.


from .models import tenant,main,sub,tanker,register
# admin.site.register(student)
admin.site.register(tenant)
admin.site.register(main)
admin.site.register(sub)
admin.site.register(tanker)
admin.site.register(register)