<<<<<<< HEAD
# Generated by Django 4.1.4 on 2022-12-25 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 4.1.4 on 2022-12-22 21:28

from django.db import migrations, models
>>>>>>> 2414e2a0a3fa68856f3e2124f90dd80c65fb834f
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> 2414e2a0a3fa68856f3e2124f90dd80c65fb834f
    ]

    operations = [
        migrations.CreateModel(
            name='GenPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=30)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('passwords', models.CharField(max_length=300)),
<<<<<<< HEAD
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
=======
            ],
            options={
                'verbose_name': 'genpass',
                'verbose_name_plural': 'genpasses',
                'ordering': ['user'],
            },
>>>>>>> 2414e2a0a3fa68856f3e2124f90dd80c65fb834f
        ),
    ]
