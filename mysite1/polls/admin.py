from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # 필드 순서 변경
    fieldsets = [                            # 각 필드 분리하여 표시
        ('질문내용', {'fields': ['question_text']}),
        ('작성시간', {'fields': ['pub_date'], 'classes': ['collapse']}), # 필드 접기
    ]
    inlines = [ChoiceInline] # Choice 모델 같이 보기

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
