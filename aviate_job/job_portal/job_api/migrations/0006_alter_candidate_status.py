# Generated by Django 3.2.3 on 2022-08-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_api', '0005_rename_picture_candidate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('Apply', 'APPLY'), ('APPLIED', 'APPLIED'), ('ACCEPT', 'ACCEPT'), ('REJECT', 'REJECT')], default='Apply', max_length=7),
        ),
    ]
