# Generated by Django 3.2.10 on 2024-02-22 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('systeminfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('datePosted', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('sessionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systeminfo.systeminfo')),
            ],
            options={
                'verbose_name_plural': 'Fee Categories',
                'db_table': 'fee_categories',
            },
        ),
    ]
