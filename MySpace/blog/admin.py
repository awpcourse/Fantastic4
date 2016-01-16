from django.contrib import admin

from blog import models


admin.site.register(models.Post)
admin.site.register(models.UserPostComment)
admin.site.register(models.UserInfo)
admin.site.register(models.Topics)
admin.site.register(models.Likes)
