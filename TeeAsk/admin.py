from django.contrib import admin
from .models import *


class ProfileAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    class Meta:
        model = Profile

class PostAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    class Meta:
        model = Post

class AnswerAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]
    class Meta:
        model = Answer

class LikeAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Like._meta.fields]
    class Meta:
        model = Like



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Answer, AnswerAdmin)