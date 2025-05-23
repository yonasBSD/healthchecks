# Generated by Django 2.1.7 on 2019-03-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("api", "0057_auto_20190118_1319")]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("email", "Email"),
                    ("webhook", "Webhook"),
                    ("hipchat", "HipChat"),
                    ("slack", "Slack"),
                    ("pd", "PagerDuty"),
                    ("pagertree", "PagerTree"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("opsgenie", "OpsGenie"),
                    ("victorops", "VictorOps"),
                    ("discord", "Discord"),
                    ("telegram", "Telegram"),
                    ("sms", "SMS"),
                    ("zendesk", "Zendesk"),
                    ("trello", "Trello"),
                    ("matrix", "Matrix"),
                ],
                max_length=20,
            ),
        )
    ]
