# Generated by Django 2.0 on 2020-09-24 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_read_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Read_num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='read_num',
        ),
        migrations.AddField(
            model_name='read_num',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
        ),
    ]
