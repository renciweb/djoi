# Generated by Django 2.0.7 on 2018-07-19 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djoi', '0008_auto_20180719_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ManyToManyField(blank=True, to='djoi.Author'),
        ),
    ]