from django.contrib import admin
from django.contrib.admin.helpers import Fieldset

from . models import Courses, School, Student

class CoursesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Course Basic Information", {"fields": ["university", "name", "program_level", "program_length", "application_fees", "tution_fees", "cost_of_living", "description"]}),
        ("Course Requirements", {"fields": ["minimum_level_of_education", "minimum_marks", "minimum_TOFEL_score", "minimum_IELTS_score", "minimum_PTE_score", "minimum_Duolingo_score"]}),
        ("Page SEO Optimization", {"fields": ["seo_title", "seo_description", "seo_keyword"]})
    ]

class SchoolAdmin(admin.ModelAdmin):
    fieldsets = [
        ("School Basic Information", {"fields": ["name", "city", "country", "complete_address", "foundation_date", "school_type", "total_students", "international_students", ]}),
        ("School Description", {"fields": ["description"]}),
        ("Page SEO Optimization", {"fields": ["seo_title", "seo_description", "seo_keyword"]})
    ]

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General Information", {"fields": ["first_name", "middle_name", "last_name", "date_of_birth", "first_language", "country_of_citizenship", "passport_number", "passport_expry_date", "gender", "marital_status"]}),
        ("Address Details", {"fields": ["address", "city", "zipcode", "country", "state", "email_address", "phone_number"]})
    ]

admin.site.register(Courses, CoursesAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)