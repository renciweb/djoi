# Generated by Django 2.0.7 on 2018-07-19 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(max_length=63)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djoi.Author')),
            ],
        ),
        migrations.AddField(
            model_name='alias',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djoi.Author'),
        ),
    ]
