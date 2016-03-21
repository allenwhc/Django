from django.contrib import admin
from .models import User, Information

class UserAdmin(admin.ModelAdmin):
	fieldsets=(
		(None, {'fields':['username']}),
		('Date information', {'fields':['user_create_date','user_last_login_date']}),
	)
	list_display=('username','password','user_create_date','user_last_login_date')
	list_filter=['username']
	search_fields=['username']

class InformationAdmin(admin.ModelAdmin):
	fieldsets=(
		('Basic information',{'fields':['first_name','middle_name','last_name', 'birth_date','email_address']}),
	)
	list_display=('first_name','middle_name','last_name', 'birth_date','email_address')


# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Information, InformationAdmin)