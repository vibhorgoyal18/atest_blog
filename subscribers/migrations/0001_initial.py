# Generated by Django 2.1.7 on 2019-03-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('mails_sent', models.IntegerField(default=0)),
                ('visit', models.IntegerField(default=1)),
                ('last_mail_sent', models.DateTimeField(auto_now_add=True)),
                ('last_visit', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('date_joined',),
            },
        ),
    ]