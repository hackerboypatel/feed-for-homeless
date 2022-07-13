# Generated by Django 4.0.6 on 2022-07-12 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='food_pics')),
                ('state', models.CharField(max_length=100, null=b'I01\n')),
                ('city', models.CharField(max_length=100, null=b'I01\n')),
                ('status', models.CharField(default='Available', max_length=100)),
                ('booked', models.CharField(max_length=200, null=b'I01\n')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
