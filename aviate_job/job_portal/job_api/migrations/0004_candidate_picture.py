# Generated by Django 3.2.3 on 2022-08-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_api', '0003_alter_candidate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='picture',
            field=models.ImageField(default='profile_pic/default.png', upload_to='profile_pic'),
        ),
    ]