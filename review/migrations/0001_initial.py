# Generated by Django 3.2.23 on 2023-12-17 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=45)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
    ]
