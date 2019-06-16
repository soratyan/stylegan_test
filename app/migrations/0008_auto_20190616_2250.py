# Generated by Django 2.2.2 on 2019-06-16 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190616_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touroku',
            name='asleeptime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='touroku',
            name='awaketime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='touroku',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='touroku',
            name='kenkobody',
            field=models.CharField(choices=[('大変悪い', '大変悪い'), ('悪い', '悪い'), ('普通', '普通'), ('良い', '良い'), ('大変良い', '大変良い')], max_length=30),
        ),
        migrations.AlterField(
            model_name='touroku',
            name='name',
            field=models.CharField(choices=[('妻', '妻'), ('ひろゆき', 'ひろゆき')], max_length=30),
        ),
        migrations.AlterField(
            model_name='touroku',
            name='workcond',
            field=models.CharField(choices=[('大変悪い', '大変悪い'), ('悪い', '悪い'), ('普通', '普通'), ('良い', '良い'), ('大変良い', '大変良い')], max_length=30),
        ),
    ]