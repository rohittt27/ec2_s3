# Generated by Django 4.2.2 on 2023-06-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255)),
                ('address', models.TextField()),
                ('experience', models.DecimalField(decimal_places=2, max_digits=3)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
