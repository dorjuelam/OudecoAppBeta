# Generated by Django 4.2.1 on 2023-05-31 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_ingeniero_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='ingeniero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.ingeniero'),
        ),
    ]
