from django.contrib import admin

# Register your models here.
from django.contrib import admin

from sports.models import SportCampo, SportCenter

admin.site.register(SportCampo)
admin.site.register(SportCenter)
