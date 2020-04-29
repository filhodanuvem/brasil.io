# Generated by Django 2.2 on 2020-04-22 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("covid19", "0006_auto_20200415_1613"),
    ]

    operations = [
        migrations.AddField(
            model_name="statespreadsheet",
            name="peer_review",
            field=models.OneToOneField(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="covid19.StateSpreadsheet"
            ),
        ),
    ]
