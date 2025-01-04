from django.contrib import admin
from elearning.models import Year, Course, Lecture,UserExpiry,PdfFiles
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(  Session)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('name',"pk")  # Displays the name field in the admin list view
    search_fields = ('name',)  # Adds a search bar for the name field
    ordering = ('name',)  # Orders the list by name


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'year',"pk")  # Displays name and associated year
    list_filter = ('year',)  # Adds a filter for year
    search_fields = ('name',)  # Adds a search bar for course name
    ordering = ('name',)


@admin.register(PdfFiles)
class PdfFilesAdmin(admin.ModelAdmin):
    list_display = ('name', 'file',"pk")  # Displays the file name and path
    search_fields = ('name',)  # Adds a search bar for file name
    ordering = ('name',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'number',"pk")  # Displays title, course, and number
    list_filter = ('course',)  # Adds a filter for course
    search_fields = ('title', 'description')  # Adds a search bar for title and description
    ordering = ('number',)  # Orders lectures by their number
    filter_horizontal = ('files',)  # Enhances the ManyToManyField UI for files


@admin.register(UserExpiry)
class UserExpiryAdmin(admin.ModelAdmin):
    list_display = ('user', 'form', 'to', 'is_subscription_active')  # Displays user, subscription dates, and status
    list_filter = ('form', 'to')  # Adds filters for subscription start and end dates
    search_fields = ('user__username', 'user__email')  # Allows search by username and email
    ordering = ('user',)
    filter_horizontal = ('courses',)  # Enhances the ManyToManyField UI for courses
