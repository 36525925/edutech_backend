# Generated by Django 3.2.10 on 2024-02-22 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('expensetypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('referenceNO', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=False, verbose_name='Approved')),
                ('datePosted', models.DateField(auto_now_add=True)),
                ('expenseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expensetypes.expensetypes')),
            ],
            options={
                'db_table': 'expenses',
            },
        ),
    ]
