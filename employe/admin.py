from django.contrib import admin

# Register your models here.
from .models import User,Employer

admin.site.register(User)
admin.site.register(Employer)