# Generated by Django 2.0.4 on 2018-04-26 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caloriecounter', '0003_auto_20180426_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loghasexercise',
            name='exerciseName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='caloriecounter.Exercises'),
        ),
        migrations.AlterField(
            model_name='loghasfood',
            name='foodName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='caloriecounter.Food'),
        ),
    ]