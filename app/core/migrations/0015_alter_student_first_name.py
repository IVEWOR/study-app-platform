# Generated by Django 4.0.4 on 2022-05-23 23:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_student_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]