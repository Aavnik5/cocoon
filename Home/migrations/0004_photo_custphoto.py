# Generated by Django 3.2.6 on 2021-08-14 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Home', '0003_rename_user_category_cust'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='custphoto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.usersignup'),
        ),
    ]
