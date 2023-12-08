# Generated by Django 4.2.7 on 2023-12-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_remove_taskcategorymodel_taskmodel'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(to='category.taskcategorymodel'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_assign_date',
            field=models.DateTimeField(),
        ),
    ]