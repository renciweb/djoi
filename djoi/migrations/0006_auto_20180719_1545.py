# Generated by Django 2.0.7 on 2018-07-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djoi', '0005_publication_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ManyToManyField(null=True, to='djoi.Author'),
        ),
    ]
