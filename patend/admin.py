from django.contrib import admin

# Register your models here.
from .models import Company, Office, Record, User

admin.site.register(Company)
admin.site.register(Office)
admin.site.register(Record)
admin.site.register(User)
