# Generated by Django 4.2.1 on 2023-05-20 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_subjectitems_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectitems',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_items', to='main.subject'),
        ),
    ]
