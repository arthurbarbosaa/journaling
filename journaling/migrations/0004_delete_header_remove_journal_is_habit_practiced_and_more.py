# Generated by Django 5.0.2 on 2024-04-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journaling', '0003_alter_goal_is_done_alter_header_highlight_type_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Header',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='is_habit_practiced',
        ),
        migrations.AddField(
            model_name='journal',
            name='is_habit_1_practiced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journal',
            name='is_habit_2_practiced',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='journal',
            name='highlight_text',
            field=models.CharField(max_length=255),
        ),
    ]