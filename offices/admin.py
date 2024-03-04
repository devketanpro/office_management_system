from django.contrib import admin

# Register your models here.
from offices.models import Office, UserOffice, Assignment, UserRequest

admin.site.register(Assignment)
admin.site.register(UserRequest)
admin.site.register(Office)
admin.site.register(UserOffice)
