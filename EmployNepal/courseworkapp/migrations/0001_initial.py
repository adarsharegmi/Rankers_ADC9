# Generated by Django 3.0.1 on 2020-01-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_Title', models.CharField(max_length=40)),
                ('job_discription', models.CharField(max_length=100)),
                ('job_Catagory', models.CharField(max_length=40)),
            ],
        ),
    ]
