# Generated by Django 3.0.4 on 2020-10-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0007_document_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Временный тип файлов'),
        ),
    ]
