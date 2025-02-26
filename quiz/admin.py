from django.contrib import admin
from .models import Question, Answer, Resource


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')  # Display title and text in the admin list view
    search_fields = ('title', 'text')  # Allow searching by title and text

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Resource)