# Generated by Django 3.0.6 on 2020-06-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangoweb', '0007_auto_20200623_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercompetitionboard',
            name='point',
        ),
        migrations.AddField(
            model_name='usercompetitionboard',
            name='answercount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usercompetitionboard',
            name='correctcount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usercompetitionboard',
            name='questioncount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]