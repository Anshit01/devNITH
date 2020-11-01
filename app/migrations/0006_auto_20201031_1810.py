# Generated by Django 2.2.16 on 2020-10-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_account_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshippost',
            name='posted_on',
        ),
        migrations.RemoveField(
            model_name='internshippost',
            name='recruiter',
        ),
        migrations.RemoveField(
            model_name='internshippost',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='opensourcepost',
            name='maintainer',
        ),
        migrations.RemoveField(
            model_name='opensourcepost',
            name='posted_on',
        ),
        migrations.RemoveField(
            model_name='opensourcepost',
            name='tags',
        ),
        migrations.AddField(
            model_name='internshippost',
            name='recruiter_email',
            field=models.EmailField(default='anshit@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internshippost',
            name='recruiter_name',
            field=models.CharField(default='Anshit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internshippost',
            name='recruiter_phone',
            field=models.CharField(default='9876543210', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opensourcepost',
            name='maintainer_email',
            field=models.EmailField(default='anshit@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opensourcepost',
            name='maintainer_name',
            field=models.CharField(default='Anshit01', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opensourcepost',
            name='maintainer_phone',
            field=models.CharField(default='9876543210', max_length=10),
            preserve_default=False,
        ),
    ]