from django.contrib import admin
from .models import Siuntejas, Vezejas, Siuntiniai, Salys, Miestai
# Register your models here.
admin.site.register([Siuntejas, Vezejas, Siuntiniai, Salys, Miestai])
