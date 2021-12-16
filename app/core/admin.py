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
        ("Agent who created", {"fields": ["author"]}),
        ("General Information", {"fields": ["first_name", "middle_name", "last_name", "date_of_birth", "first_language", "country_of_citizenship", "passport_number", "passport_expry_date", "gender", "marital_status"]}),
        ("Address Details", {"fields": ["address", "city", "zipcode", "country", "state", "email_address", "phone_number"]}),
        ("Education Summary for Grade 12", {"fields": ["school_name_of_grade_12", "country_of_grade_12_school", "grade_12_primary_language_of_instruction", "grade_12_attended_school_from", "grade_12_attended_school_to", "grade_12_degree_name", "grade_12_school_address", "grade_12_school_state", "grade_12_school_city", "grade_12_school_zip_code"]}),
        ("Education Summary for Grade 10", {"fields": ["school_name_of_grade_10", "country_of_grade_10_school", "grade_10_primary_language_of_instruction", "grade_10_attended_school_from", "grade_10_attended_school_to", "grade_10_degree_name", "grade_10_school_address", "grade_10_school_state", "grade_10_school_city", "grade_10_school_zip_code"]}),
        ("Test Score", {"fields": ["english_test_type"]}),
        ("Background Information", {"fields": ["refusal_visa_from", "valid_visa", "more_details"]}),
    ]

admin.site.register(Courses, CoursesAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)