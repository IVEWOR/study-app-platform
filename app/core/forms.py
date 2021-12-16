from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from . import models


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class CreateStudent(forms.ModelForm):
     class Meta:
         model = models.Student
         fields = ["first_name", "middle_name", "last_name", "date_of_birth", "first_language", "country_of_citizenship", "passport_number", "passport_expry_date", "gender", "marital_status", "address", "city", "zipcode", "country", "state", "email_address", "phone_number", "school_name_of_grade_12", "country_of_grade_12_school", "grade_12_primary_language_of_instruction", "grade_12_attended_school_from", "grade_12_attended_school_to", "grade_12_degree_name", "grade_12_school_address", "grade_12_school_state", "grade_12_school_city", "grade_12_school_zip_code", "school_name_of_grade_10", "country_of_grade_10_school", "grade_10_primary_language_of_instruction", "grade_10_attended_school_from", "grade_10_attended_school_to", "grade_10_degree_name", "grade_10_school_address", "grade_10_school_state", "grade_10_school_city", "grade_10_school_zip_code", "english_test_type", "refusal_visa_from", "valid_visa", "more_details",
    ]