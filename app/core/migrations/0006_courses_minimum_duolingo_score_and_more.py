# Generated by Django 4.0 on 2021-12-11 21:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_courses_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='minimum_Duolingo_score',
            field=models.IntegerField(default=120, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='minimum_IELTS_score',
            field=models.FloatField(default=6.5, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='minimum_PTE_score',
            field=models.IntegerField(default=120, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='minimum_TOFEL_score',
            field=models.IntegerField(default=120, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='minimum_marks',
            field=models.IntegerField(default=70, help_text='Marks are in percentage', null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='foundation_date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='international_students',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='school_type',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='total_students',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
