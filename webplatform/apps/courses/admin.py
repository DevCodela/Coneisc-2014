#encoding:utf-8
from django.contrib import admin
from .models import Course, Chapter, Article, UserProgress, UserEnrolled


class CourseInline(admin.TabularInline):
    model = Course.enrolled.through
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    inlines = [ CourseInline, ]
    fields = ('title', 'slug', 'summary', 'isfree', 'released',)
    list_display = ('title', 'summary', 'isfree', 'released',)


class ChapterInline(admin.TabularInline):
    model = Chapter.progress.through
    extra = 0


class ChapterAdmin(admin.ModelAdmin):
    inlines = [ ChapterInline, ]
    fields = ('title', 'summary', 'video', 'course', 'released',)
    list_display = ('title', 'course', 'released',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Article)
admin.site.register(UserProgress)
admin.site.register(UserEnrolled)
