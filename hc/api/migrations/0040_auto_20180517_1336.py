# Generated by Django 2.0.4 on 2018-05-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("api", "0039_remove_check_last_ping_body")]

    operations = [
        migrations.AddField(
            model_name="check",
            name="last_ping_was_fail",
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ping", name="fail", field=models.NullBooleanField(default=False)
        ),
    ]
