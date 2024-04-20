# Generated by Django 3.2 on 2023-02-04 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_auto_20230204_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depts', to='app2.college'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='college',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='princi', to='app2.college'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studs', to='app2.department'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjs', to='app2.department'),
        ),
    ]