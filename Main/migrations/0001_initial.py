# Generated by Django 4.1.7 on 2023-06-20 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autoupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='uploads/')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('AscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('LscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SescorePer', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=100)),
                ('description1', models.CharField(blank=True, max_length=255)),
                ('description2', models.CharField(blank=True, max_length=255)),
                ('description3', models.CharField(blank=True, max_length=255)),
                ('description4', models.CharField(blank=True, max_length=255)),
                ('description5', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('users', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('txt_file', models.FileField(upload_to='uploads/')),
                ('xlsx_file', models.FileField(upload_to='uploads/')),
                ('created_at', models.DateTimeField()),
                ('AscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('LscorePer', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SescorePer', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'upload_files',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.question')),
            ],
        ),
    ]