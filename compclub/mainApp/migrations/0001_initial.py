# Generated by Django 4.2.5 on 2023-09-17 14:05

from django.db import migrations, models
import mainApp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[mainApp.validators.capitalLetterValidator])),
                ('surname', models.CharField(max_length=50, validators=[mainApp.validators.capitalLetterValidator])),
                ('middlename', models.CharField(max_length=50, validators=[mainApp.validators.capitalLetterValidator])),
                ('email', models.EmailField(max_length=254)),
                ('desired_place', models.CharField(max_length=50)),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField()),
                ('vip', models.BooleanField()),
                ('promo_code', models.CharField(default='', max_length=50)),
                ('commentaries', models.TextField()),
            ],
        ),
    ]
