# Generated by Django 4.2.1 on 2023-06-03 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Yazar",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(verbose_name="İçerik"),
        ),
        migrations.AlterField(
            model_name="article",
            name="created_time",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Oluşturulma Tarihi"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Başlık"),
        ),
    ]
