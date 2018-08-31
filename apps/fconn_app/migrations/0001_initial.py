# Generated by Django 2.1 on 2018-08-29 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed'), ('Not Applicable', 'Not Applicable')], max_length=96)),
                ('test_scores', models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed'), ('Not Applicable', 'Not Applicable')], max_length=96)),
                ('school_transcript', models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed'), ('Not Applicable', 'Not Applicable')], max_length=96)),
                ('reports', models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed'), ('Not Applicable', 'Not Applicable')], max_length=96)),
                ('sec_school_reports', models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed'), ('Not Applicable', 'Not Applicable')], max_length=96)),
                ('recommenadtion', models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed'), ('Not Applicable', 'Not Applicable')], max_length=96)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2)),
                ('application_type', models.CharField(blank=True, choices=[('Early Decision', 'Early Decision'), ('Early Action', 'Early Action'), ('Single Choice Early Action', 'Single Choice Early Action'), ('Regular Decision', 'Regular Decision'), ('Rolling Admission', 'Rolling Admission'), ('FAFSA', 'FAFSA')], max_length=255)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ManyToManyField(related_name='user_colleges', through='fconn_app.Checklist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FAFSADeadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2)),
                ('description', models.CharField(choices=[('Federal', 'Federal'), ('State', 'State')], max_length=96)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('state_abbr', models.CharField(blank=True, max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('resource_url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('schoolState', models.CharField(blank=True, max_length=255, null=True)),
                ('major', models.CharField(blank=True, max_length=255, null=True)),
                ('schoolName', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fconn_app.College'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
