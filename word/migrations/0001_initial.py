# Generated by Django 4.2.2 on 2023-06-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=50, verbose_name='단어')),
                ('kor', models.CharField(max_length=50, verbose_name='한국어 뜻')),
                ('eng', models.CharField(max_length=100, verbose_name='영어 뜻')),
            ],
        ),
    ]
