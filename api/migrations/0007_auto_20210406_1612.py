# Generated by Django 3.1 on 2021-04-06 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200816_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='work',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='work',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='work',
            name='height',
        ),
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
        migrations.AddField(
            model_name='work',
            name='skills',
            field=models.ManyToManyField(blank=True, to='api.Skill'),
        ),
    ]