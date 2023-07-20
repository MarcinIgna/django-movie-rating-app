# Generated by Django 4.2.3 on 2023-07-19 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("movie_db_api", "0011_movierating_alter_movie_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="rating",
        ),
        migrations.AddField(
            model_name="rating",
            name="movie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movie_ratings",
                to="movie_db_api.movierating",
            ),
        ),
    ]