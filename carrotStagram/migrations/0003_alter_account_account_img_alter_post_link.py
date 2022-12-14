# Generated by Django 4.1.3 on 2022-11-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carrotStagram", "0002_remove_account_follow_set_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="account_img",
            field=models.ImageField(blank=True, upload_to="profiles_imgs"),
        ),
        migrations.AlterField(
            model_name="post", name="link", field=models.URLField(blank=True),
        ),
    ]
