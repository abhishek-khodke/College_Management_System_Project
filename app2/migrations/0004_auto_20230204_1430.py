# Generated by Django 3.2 on 2023-02-04 09:00

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_auto_20230127_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adr', models.CharField(max_length=500)),
                ('est_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dept_str', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.college')),
            ],
            options={
                'db_table': 'dept',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('age', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.department')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('activep', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_practical', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.department')),
                ('student', models.ManyToManyField(related_name='subjs', to='app2.Student')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.FloatField()),
                ('qual', models.CharField(max_length=50)),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app2.college')),
            ],
            options={
                'db_table': 'principal',
            },
        ),
    ]
