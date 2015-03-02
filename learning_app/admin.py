from django.contrib import admin
from learning_app import models


admin.site.register(models.Link)
admin.site.register(models.Hit)