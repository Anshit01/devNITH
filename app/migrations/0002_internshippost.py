# Generated by Django 2.2.16 on 2020-10-31 06:59

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('posted_on', models.DateField()),
                ('last_date', models.DateField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('description', models.TextField()),
                ('registration_link', models.CharField(max_length=1000)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account')),
            ],
        ),
    ]
