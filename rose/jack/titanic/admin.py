from django.contrib import admin
from titanic.models import friends
# Register your models here.
class friendsAdmin(admin.ModelAdmin):
	list_display=['no','name','age','city']
admin.site.register(friends,friendsAdmin)