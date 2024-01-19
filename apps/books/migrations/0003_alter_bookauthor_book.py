# Generated by Django 4.2.3 on 2023-12-10 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookreview_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookauthor', to='books.book'),
        ),
    ]
