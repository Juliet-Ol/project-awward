# Generated by Django 4.0.3 on 2022-04-10 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsproject', '0006_remove_rating_rate_rating_rating_rating_scale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='awwardsproject.post'),
        ),
    ]