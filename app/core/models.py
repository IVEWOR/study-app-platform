from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from tinymce.models import HTMLField
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

class School(models.Model):
    name = models.CharField(max_length=350)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    complete_address = models.CharField(max_length=350)
    description = HTMLField(null=True)
    # Features pending
    # Map Location pending
    
    ####### School Card Information
    # profile pic pending
    foundation_date = models.CharField(max_length=200, null=True)
    SCHOOL_TYPE = (
        ("private", "Private"),
        ("public", "Public")
    )
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPE, null=True)
    total_students = models.CharField(max_length=200, null=True)
    international_students = models.CharField(max_length=200, null=True)

    ####### SEO Details
    seo_title = models.CharField(null=True, max_length=60, help_text="60 max characters")
    seo_description = models.CharField(null=True, max_length=150, help_text="150 max characters")
    seo_keyword = models.CharField(null=True, max_length=200, help_text="Use comma ( , ) to add more than one keyword")

    def __str__(self):
        return self.name

class Courses(models.Model):
    university = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=350)
    program_level = models.CharField(max_length=200)
    program_length = models.CharField(max_length=200)
    application_fees = models.CharField(max_length=200)
    tution_fees = models.CharField(max_length=200)
    cost_of_living = models.CharField(max_length=200)
    description = HTMLField(null=True)

    # requirements
    EDUCATION_LEVELS = (
        ("1", "Grade 1"),
        ("2", "Grade 2"),
        ("3", "Grade 3"),
        ("4", "Grade 4"),
        ("5", "Grade 5"),
        ("6", "Grade 6"),
        ("7", "Grade 7"),
        ("8", "Grade 8"),
        ("9", "Grade 9"),
        ("10", "Grade 10"),
        ("11", "Grade 11"),
        ("12", "Grade 12/High School"),
        ("13", "1-Year Post Secondary Certificate"),
        ("14", "2-Year Undergraduate Diploma"),
        ("15", "3-Year Undergraduate Advanced Diploma"),
        ("16", "3-Year Bachelors Degree"),
        ("17", "4-Year Bachelors Degree"),
        ("18", "Post-Graduate Diploma/Certificate"),
        ("19", "Masters Degree"),
        ("20", "Doctoral Degree (PhD, M.D,..)"),
    )
    minimum_level_of_education = models.CharField(max_length=3, choices=EDUCATION_LEVELS, null=True)
    minimum_marks = models.IntegerField(null=True, default=70, help_text="Marks are in percentage")

    # Language test score
    minimum_TOFEL_score = models.IntegerField(null=True, default=120)
    minimum_IELTS_score = models.FloatField(null=True, default=6.5)
    minimum_PTE_score = models.IntegerField(null=True, default=120)
    minimum_Duolingo_score = models.IntegerField(null=True, default=120)

    ####### SEO Details
    seo_title = models.CharField(null=True, max_length=60, help_text="60 max characters")
    seo_description = models.CharField(null=True, max_length=150, help_text="150 max characters")
    seo_keyword = models.CharField(null=True, max_length=200, help_text="Use comma ( , ) to add more than one keyword")

    def __str__(self):
        return self.name

class Student(models.Model):
    ## General Information
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    first_language = models.CharField(max_length=50, null=True)
    country_of_citizenship = models.CharField(max_length=50, null=True, default="India")
    passport_number = models.CharField(max_length=50, null=True)
    passport_expry_date = models.DateField(null=True)
    GENDER = (
        ("male", "Male"),
        ("female", "Female")
    )
    gender = models.CharField(max_length=50, null=True, choices=GENDER)
    MARITAL_STATUS = (
        ("single", "Single"),
        ("married", "Married")
    )
    marital_status = models.CharField(max_length=50, null=True, choices=MARITAL_STATUS)

    # Address Details
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=100, null=True, default="India")
    state = models.CharField(max_length=100, null=True, default="Delhi")
    email_address = models.EmailField(max_length=200, null=True)
    phone_number = PhoneNumberField(null=True, default="+91")

    

    def __str__(self):
        return self.first_name