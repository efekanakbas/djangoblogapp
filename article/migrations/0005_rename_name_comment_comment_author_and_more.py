# Generated by Django 4.2.1 on 2023-07-15 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="name",
            new_name="comment_author",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="comment",
            new_name="comment_content",
        ),
        migrations.AddField(
            model_name="comment",
            name="comment_date",
            field=models.TimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Oluşturulma Tarihi",
            ),
            preserve_default=False,
        ),
    ]