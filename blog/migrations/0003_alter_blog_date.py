# Generated by Django 4.0.4 on 2022-07-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_description_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
    ]
