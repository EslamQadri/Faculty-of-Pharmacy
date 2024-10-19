# Generated by Django 5.0.6 on 2024-10-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_userexpiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name': 'PDFs',
                'verbose_name_plural': 'PDFs',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='PDFs', to='elearning.pdffiles'),
        ),
    ]
