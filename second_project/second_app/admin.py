from django.contrib import admin
from second_app.models import Topic,webpage,AccessRecord,user

# Register your models here.
admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(AccessRecord)
admin.site.register(user)